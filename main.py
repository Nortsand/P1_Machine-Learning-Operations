

from fastapi import FastAPI
import pandas as pd


steam = pd.read_csv("steam.csv")

dic_genres = pd.read_csv("data/genre_to_id.csv", index_col='genre').to_dict(
    orient='dict')['id']

dic_specs = pd.read_csv("data/spec_to_id.csv", index_col='spec').to_dict(
    orient='dict')['id']


app = FastAPI()

# 1
#Función para obtener los 5 géneros más ofrecidos por año.
@app.get('/genero/{year}')
def genero(Año: str):
    Año = int(Año)
    df_year = steam[steam['year'] == Año]
    genre_counts = {}

    for genre_id in dic_genres.values():
        # Inicializar la cuenta para cada género
        genre_counts[genre_id] = 0

        # Iterar sobre las filas del DataFrame del año especificado
        for _, row in df_year.iterrows():
            # Verificar si el ID del género está presente en la lista de IDs de géneros
            if str(genre_id) in row['genre_id']:
                # Incrementar la cuenta del género si está presente
                genre_counts[genre_id] += 1

    # Ordenar los géneros individuales según el número de repeticiones en orden descendente
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

    # Tomar los 5 géneros individuales más repetidos
    top_individual_genres = [genre_id for genre_id, _ in sorted_genres[:5]]

    # Obtener los nombres de géneros a partir de los IDs utilizando el diccionario dic_genres
    top_genres = [genre for genre, genre_id in dic_genres.items() if genre_id in top_individual_genres]

    # Formatear el resultado
    result = {'year': Año, 'top_genres': top_genres}

    return result



# 2
# Función que devuelve una lista con los juegos lanzados en un año. 
@app.get('/juegos/{year}')
def juegos(Año: str):
    # Convertir el año a entero para realizar la comparación
    Año = int(Año)

    # Filtrar el DataFrame para obtener los datos del año proporcionado
    df_year = steam[steam['year'] == Año]

    # Obtener la lista de juegos lanzados en el año
    juegos_lanzados = df_year['app_name'].tolist()

    # Formatear el resultado
    resultado = {'año': Año, 'juegos lanzados': juegos_lanzados}

    return resultado


# 3
# Función que devuelve una línea con los 5 specs que más se repiten por año.

@app.get('/specs/{year}')
def specs(Año: str):
    Año = int(Año)
    df_year = steam[steam['year'] == Año]
    spec_counts = {}

    for spec_id in dic_specs.values():
        # Inicializar la cuenta para cada género
        spec_counts[spec_id] = 0

        # Iterar sobre las filas del DataFrame del año especificado
        for _, row in df_year.iterrows():
            # Verificar si el ID del género está presente en la lista de IDs de géneros
            if str(spec_id) in row['spec_id']:
                # Incrementar la cuenta del género si está presente
                spec_counts[spec_id] += 1

     # Ordenar los géneros individuales según el número de repeticiones en orden descendente
    sorted_specs = sorted(spec_counts.items(), key=lambda x: x[1], reverse=True)

    # Tomar los 5 géneros individuales más repetidos
    top_individual_specs = [spec_id for spec_id, _ in sorted_specs[:5]]

    # Obtener los nombres de géneros a partir de los IDs utilizando el diccionario dic_genres
    top_specs = [spec for spec, spec_id in dic_specs.items() if spec_id in top_individual_specs]

    # Formatear el resultado
    result = {'year': Año, 'top_specs': top_specs}

    return result



# 4
# Función que retorna cantidad de juegos lanzados en un año con earlyaccess

@app.get('/earlyacces/{year}')
def earlyacces(Año: str):
    # Convertir el año a entero para realizar la comparación
    Año = int(Año)

    # Filtrar el DataFrame para obtener los datos del año proporcionado
    df_year = steam[steam['year'] == Año]

    # Contar la cantidad de juegos lanzados en el año con early access (valor True)
    cantidad_early_access = int(df_year['early_access'].sum())

    # Formatear el resultado
    resultado = {'año': Año, 'early_acces': cantidad_early_access}
    
    return resultado


# 5
# Función que devuelve una lista de registros categorizados con una análisis de sentimiento.

@app.get('/sentiment/{year}')
def sentiment(Año: str):
    # Convertir el año a entero para realizar la comparación
    Año = int(Año)

    # Filtrar el DataFrame para obtener los datos del año proporcionado
    df_year = steam[steam['year'] == Año]

    # Contar la cantidad de registros para cada categoría de sentimiento por año.
    sentiment_counts = {}
    for sentiment_category in df_year['sentiment'].unique():
        count = df_year[df_year['sentiment'] == sentiment_category].shape[0]
        sentiment_counts[sentiment_category] = count

    # Formatear el resultado
    resultado = {'año': Año, 'sentiment': sentiment_counts}

    return resultado


# 6
# Función que devuelve top 5 juegos con mayor metascore según año.

@app.get('/metascore/{year}')
def metascore(Año: str):
    # Convertir el año a entero para realizar la comparación
    Año = int(Año)

    # Filtrar el DataFrame para obtener los datos del año proporcionado
    df_year = steam[steam['year'] == Año]

    # Ordenar los juegos según el metascore en orden descendente
    top_5_juegos = df_year.nlargest(5, 'metascore')

    # Obtener la lista de juegos con mayor metascore y su respectivo metascore
    juegos_metascore = top_5_juegos[['app_name', 'metascore']].to_dict(orient='records')

    # Formatear el resultado
    resultado = {'año': Año, 'metascore': juegos_metascore}

    return resultado