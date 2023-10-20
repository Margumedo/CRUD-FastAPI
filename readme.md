# CRUD con FastAPI

Mi primer CRUD usando FastAPI: este Crud te permite guardar una pregunta y con sus posibles respuesta.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Python (versión 3.9) o superior.
- Dependencias: se incluyen en el repo.

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar el proyecto:

1. Clona el repositorio desde GitHub:

```
git clone https://github.com/Margumedo/CRUD-FastAPI.git
```

2. Navega al directorio del proyecto:

cd tu-repositorio

3. Crea un entorno virtual (recomendado):

```
python -m venv venv
```

4. Activa el entorno virtual:

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En macOS y Linux:

  ```
  source venv/bin/activate
  ```

5. Instala las dependencias:

```
pip install -r requirements.txt
```

6. Inicia la aplicación FastAPI:

```
uvicorn main:app --reload
```

Esto iniciará tu aplicación FastAPI y estará disponible en la dirección http://localhost:8000 para interactuar con la API a través de la interfaz de documentación generada automáticamente por FastAPI.
