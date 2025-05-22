from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from pymongo import MongoClient
from datetime import datetime

# Conexión a MongoDB Atlas
try:
    client = MongoClient('mongodb+srv://tarijuguete:9Ge7BCv6j0YCMe06@cluster0.ccj5v.mongodb.net/University?retryWrites=true&w=majority&appName=Cluster0')
    db = client['University']
    preguntas_collection = db['Question']
    usuarios_collection = db['usuarios_encuesta']
    print("Conexión a MongoDB Atlas establecida correctamente")
except Exception as e:
    print(f"Error conectando a MongoDB Atlas: {e}")

class PreguntaViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        try:
            preguntas = list(preguntas_collection.find())
            for pregunta in preguntas:
                pregunta['_id'] = str(pregunta['_id'])
            return Response(preguntas)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_usuario(request):
    try:
        data = request.data
        print(f"Datos recibidos: {data}")
        required_fields = ['nombre', 'email', 'telefono', 'carrera_recomendada', 'justificacion']
        for field in required_fields:
            if field not in data or not data[field]:
                return Response({'error': f'Campo {field} es requerido'}, status=400)
        usuario_documento = {
            'nombre': data['nombre'],
            'email': data['email'],
            'telefono': data['telefono'],
            'carrera_recomendada': data['carrera_recomendada'],
            'justificacion': data['justificacion'],
            'fecha_registro': datetime.now(),
            'activo': True
        }
        existing_user = usuarios_collection.find_one({'email': data['email']})
        if existing_user:
            return Response({'error': 'Ya existe un usuario con este email'}, status=400)
        result = usuarios_collection.insert_one(usuario_documento)
        print(f"Usuario guardado con ID: {result.inserted_id}")
        return Response({
            'success': True,
            'id': str(result.inserted_id),
            'message': 'Usuario guardado exitosamente en MongoDB Atlas'
        })
    except Exception as e:
        print(f"Error al guardar usuario: {e}")
        return Response({'error': f'Error interno del servidor: {str(e)}'}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuarios(request):
    try:
        usuarios = list(usuarios_collection.find())
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
            if 'fecha_registro' in usuario:
                usuario['fecha_registro'] = usuario['fecha_registro'].isoformat()
        return Response(usuarios)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
