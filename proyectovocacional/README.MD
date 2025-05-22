# API Autenticada con JWT

Este proyecto es una API protegida mediante autenticación con JSON Web Tokens (JWT). Aquí encontrarás la información necesaria para autenticarte y probar los endpoints protegidos.

---

## 🧑‍💻 Credenciales de Usuario

| Rol   | Usuario | Contraseña |
|-------|---------|-------------|
| Admin | admin   | 1234        |

---

## 🔐 Tokens JWT

### 🔄 Token de Refresh

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MDM4MTQwMywiaWF0IjoxNzQ3Nzg5NDAzLCJqdGkiOiIxNjVmNzIxNjljNGE0NTkwOWQ0YmNmYmU5ZTVlYmY3YiIsInVzZXJfaWQiOjF9.JRBRE8RQ6eq7CKfbE0pskekYuIns9-nx77GWRWw3-E4
```

### 🪪 Token de Acceso (Access Token)

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3MTgwNzU4LCJpYXQiOjE3NDcxODA0NTgsImp0aSI6IjU2MGE2MzA4YTg2YjQ2MzA5OTVhOTA4OTE3MDQxYTM5IiwidXNlcl9pZCI6MX0.7NIxPR8GwE9N40wOZVC2kTdwFZseE8Ft3-LaQud_odA
```

> ⚠️ Los tokens tienen tiempo de expiración. Asegúrate de solicitar un nuevo token de acceso cuando el actual haya expirado usando el refresh token.

---

## 🔁 Endpoint de Refresh Token

**POST** `/auth/refresh`

### Solicitud

```http
POST /auth/refresh HTTP/1.1
Content-Type: application/json

{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Respuesta esperada

```json
{
  "access_token": "nuevo_token_de_acceso",
  "refresh_token": "nuevo_refresh_token" // si es rotado
}
```

---

## 🔐 Acceso a Endpoints Protegidos

Para acceder a endpoints protegidos, añade el token de acceso en la cabecera:

```http
Authorization: Bearer {access_token}
```

---

## 🛠 Tecnologías usadas

- JWT para autenticación
- Node.js / Django / FastAPI (dependiendo de tu backend)
- JSON como formato de comunicación

---

## 📌 Notas

- No compartas estos tokens públicamente.
- En producción, los tokens deben ser generados dinámicamente y seguros.
- El refresh token debe guardarse de forma segura (por ejemplo, en cookies HttpOnly).

---

## 🧼 Cerrar sesión

Al cerrar sesión, asegúrate de invalidar el refresh token en el backend (si se guarda en base de datos o lista negra).
