# API de Facturas - Proyecto de Integración

Este proyecto consiste en una **API REST** desarrollada en Python con **FastAPI**, que permite gestionar y consultar facturas de manera sencilla. Está pensada para aprender sobre APIs y pruebas de integración con clientes externos.

---

## 🛠 Tecnologías

- **Python 3.11+**
- **FastAPI**: Framework web para APIs REST.
- **Uvicorn**: Servidor ASGI para ejecutar la API.
- **Requests**: Para pruebas de cliente.
- **Render** / **Localhost**: Despliegue del servicio.

---

## 🚀 Funcionalidades

- Exposición de endpoints para consultar y registrar facturas.
- Estructura de datos en **JSON**, incluyendo:
  - Información general de carga.
  - Detalles de terceros.
  - Tipos de tasas.
  - Tasas asociadas a terceros.
  - Detalle de cada tasa.

- Ejemplo de endpoint disponible:
  - `GET /facturas` → Lista de facturas.
  - `POST /facturas` → Crear nueva factura.

---

## ⚙ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/alexv6v6/api-facturas.git
cd api-facturas
```

2. Crear y activar el entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Ejecución

Para ejecutar la API localmente:

```bash
uvicorn main:app --reload
```

- La API estará disponible en `http://127.0.0.1:8000`.
- La documentación interactiva de Swagger estará en `http://127.0.0.1:8000/docs`.

---

## 📡 Pruebas con Cliente

Se puede consumir la API usando:

- **Python**:

```python
import requests

url = "http://127.0.0.1:8000/facturas"
response = requests.get(url)
print(response.json())
```

- **Postman**: Crear una request usando la URL del endpoint con el método `GET` o `POST`.

---

## ☁ Despliegue en la nube

- El proyecto puede ser desplegado en servicios como **Render**, **Railway**, **Azure** o **AWS**.
- Render proporciona una URL pública para consumir la API externamente.

---

## 📄 Ejemplo de JSON

```json
{
  "NitProveedor": "8300148789",
  "NumeroCarga": "2025-10154",
  "CantidadRegistros": 1,
  "FechaCarga": "31/01/2025",
  "IdComEntidad": 0,
  "Terceros": [
    {
      "NitTercero": "80401720",
      "TipoDocumento": "C",
      "NomTercero": "PEDRO JOSE PEREZ",
      "CodNaturaleza": "1",
      "TipoTercero": "1",
      "PrimerNombre": "PEDRO",
      "OtrosNombres": "JOSE",
      "PrimerApellido": "PEREZ",
      "OtrosApellidos": "",
      "Telefono": "3158965487",
      "Email": "jperez@hotmail.com",
      "Direccion": "Carrera 35N #58-59"
    }
  ]
}
```

---

## ✅ Contribuciones

Este proyecto es **para aprendizaje**, por lo que cualquier mejora, ejemplo o prueba es bienvenida.

---

## 📄 Licencia

MIT License

