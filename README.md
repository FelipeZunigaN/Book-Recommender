# Semantic Book Recommender

Este proyecto es un sistema de recomendación de libros basado en búsqueda semántica usando embeddings de OpenAI y almacenamiento en Chroma vectorstore. Permite buscar libros por descripción, filtrar por categoría y tono emocional, y obtener recomendaciones relevantes con una interfaz web interactiva construida con Gradio.

---

## Características

- Carga y procesamiento eficiente del dataset de libros con imágenes y metadata.
- Uso de embeddings semánticos OpenAI para búsqueda avanzada.
- Vectorstore Chroma para almacenamiento y búsqueda rápida.
- Filtros por categoría y tono emocional (feliz, triste, sorprendente, etc.).
- Interfaz web moderna e interactiva con Gradio.
- Arquitectura modular para facilitar mantenimiento y extensión.
- Tests básicos para asegurar calidad del código.

---

## Estructura del proyecto

```bash
book-recommender/
│
├── data/ # Datos: CSV con metadata de libros, archivos txt para embeddings
├── book_recommender/ # Código fuente modularizado
│ ├── config.py # Path para dataset y vectorDB
│ ├── data_loader.py # Funciones para cargar dataset
│ ├── vectorstore.py # Creación y carga de Chroma DB
│ ├── recommender.py # Lógica de recomendaciones semánticas
│ ├── ui.py # Interfaz Gradio
│ └── config.py # Variables y paths configurables
├── data/ # csv files
├── tests/ # Tests unitarios
├── main.py # Script principal que lanza la app
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo
```


---

## Instalación

Se recomienda crear un entorno virtual para instalar las dependencias.

```bash
python -m venv .venv
source .venv/bin/activate    # Linux / MacOS
# o
.venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

## Configuración
Crear un archivo .env con las variables necesarias, por ejemplo:

```bash
OPENAI_API_KEY=tu_api_key_aqui
```

## Uso
Para ejecutar la aplicación:

```bash
python main.py
```
Esto lanzará la interfaz web de Gradio en el navegador, donde podrás ingresar una descripción, seleccionar categoría y tono, y obtener recomendaciones de libros.


## Testing
Para ejecutar los tests con pytest:

```bash
pytest tests/
```

## Tecnologías y librerías
- LangChain

- OpenAI Embeddings

- Chroma Vectorstore

- Gradio

## Futuras Mejoras

- Incorporar autenticación y perfiles de usuario.

- Añadir métricas y analítica de uso.

- Mejorar la UI con filtros adicionales y visualización enriquecida.

- Dockerizar la aplicación para despliegue sencillo.