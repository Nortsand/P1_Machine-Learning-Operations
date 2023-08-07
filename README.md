# PROYECTO INDIVIDUAL  N°1 
## Machine Learning Operations
## Construcción de una API
*Autor: Yuri Díaz*

¡Bienvenido!

Basados en un dataset de videojuegos desplegaremos una API para realizar consultas específicas de negocios. También se podrá consultar un precio predictivo basado de un modelo de machine learning. 




# Índice

- [Objetivos del proyecto](#objetivos-del-proyecto)
- [Extracción de los datos](#extracción-de-los-datos)
- [Preparando el entorno](#preparando-el-entorno)
- [Carga, limpieza y transformación](#carga-limpieza-y-transformación)
- [Exportación de datos](#exportación-de-datos)
- [Análisis exploratorio de datos](#análisis-exploratorio-de-datos)
- [Feature engineering](#feature-engineering)
- [Modelo de machine learning](#modelo-de-machine-learning)
- [Desarrollo de la API](#desarrollo-de-la-api)
- [Deployment en Render](#deployment-en-render)
- [Tecnologías usadas](#tecnologías-usadas)

# Objetivos del proyecto
Con este propósito realizaremos los siguientes procesos:

* Extracción, Transformación y Limpieza de datos
* Desarrollo de la API
* EDA (Análisis exploratorio de datos)
* Feature engineering
* Modelo de machine learning (ML)

# Extracción de los datos
Para este proyecto utilizamos el archivo steam_games.json el cual se encuentra disponible en la carpeta "data" del repositorio. También puedes encontrarlo aquí: [Dataset.](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

Por otra parte, tienes a tu disposición el [Diccionario de datos.](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?pli=1#gid=0) del dataset.

# Preparando el entorno
Comenzaremos creando un entorno virtual de trabajo utilizando los siguientes comandos: 

*py -m venv venv* | Otras opciones en lugar de *py* pueden ser python o python3.

Activamos el entorno con uno de estos tres comandos:

* source venv/Scripts/activate
* source venv\Scripts\activate
* source venv/bin/activate | Linux y Mac

Por último instalamos las librerías necesarias para el proyecto:

pip install -r requirements.txt.

Con el entorno listo ya podemos empezar a trabajar

# Carga, limpieza y transformación
* Importamos los módulos *ast* y *os* y la librería *pandas*. 
* Cargamos el dataset

* Exploramos el dataset y en aquellas columnas en que lo creemos necesario efectuamos las siguientes operaciones: a. Transformación de tipos de datos. b.  Eliminación de valores nulos. c. Imputación de valores.  


# Exportación de datos
* Exportamos tres dataframe limpios. El primero es un csv y los otros son dos diccionarios. Esto último se realiza porque tener 2 columnas anidadas armamos un diccionario por cada columna que contiene los valores únicos. Les creamos un id y los exportamos. Estos diccionarios los utilizaremos para las siguientes etapas de construcción de funciones y feature engineering optimizando la velocidad de búsqueda dentro del dataset.


# Análisis exploratorio de datos
* Graficamos para encontrar tendencias, distribuciones, outliers, relaciones entre las variables.
* Extraemos métricas estadísticas.

# Feature engineering

* Elegimos las variables indepedientes y la variable dependendiente o target.
* Realizamos las siguientes transformaciones: a) Cambiar columnas booleanas a numéricas. b) Aplicamos one hot encoding a columnas categóricas.
* 
# Modelo de machine learning
* Elección de modelos de regresión.
* Divsión del dataset en sección de entrenamiento y prueba.
* Optimización de hiperparámetros.
* Entrenamiento del modelo.
* Evaluación del modelo.

# Desarrollo de la API
* En *main.py* cargamos los archivos limpios.
* Creamos los *endpoints* con FASTAPI. 

* Creamos las funciones:
* *def genero*: Se ingresa un año y devuelve una lista con los 5 géneros más ofrecidos en el orden correspondiente.
* *def juegos*: Se ingresa un año y devuelve una lista con los juegos lanzados en el año.
* *def specs*: Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.
* *def earlyacces*: Devuelve la cantidad de juegos lanzados en un año con early access.
* *def sentiment*: Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.
* *def metascore*: Top 5 juegos según año con mayor metascore.
 
* Se prueba la API y sus endpoints de manera local desde la terminal con los siguintes comandos (asegurarse de que la terminal está en la carpeta raíz del proyecto):

* *uvicorn main:app --reload*

Todo funciona de acuerdo a lo esperado y estamos listos para el deploy

# Deployment en Render

* Subir el repositorio a GitHub
* Entrar en render.com y crear un usuario.
* Elegir la opción Web Service
* Bajamos hasta el final y encontramos la opción Public Git Repository en la cual tendremos que ingresar el link de nuestro repositorio (asegurarse de que el mismo esté público).
* Completamos los campos requeridos (branch: main, runtime: python3, start command: 'uvicorn main:app --host 0.0.0.0 --port 10000')
* Le damos a la opción Create Web Service y esperamos unos minutos a que cargue e inicie la aplicación y la podremos acceder con el siguiente link

# Tecnologías usadas
* Pandas, Matplotlib, Seaborn, Sklearn.
* FastAPI, Uvicorn. 
* Render 