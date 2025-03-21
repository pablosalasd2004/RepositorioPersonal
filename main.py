import collections
from os.path import join
from utilidades import Anime  # Debes utilizar esta nametupled


#####################################
#       Parte 1 - Cargar datos      #
#####################################
def cargar_animes(ruta_archivo: str) -> list:
    set_generos : set = set()
    lista_nametuples : list = []
    with open(ruta_archivo, 'rt', encoding = 'utf-8', ) as archivo:
        lista_lineas : list = archivo.readlines()
    for linea in lista_lineas:
        lista_split : list = linea.strip().split(',')
        lista_genero : list = lista_split[5].strip().split(';')
        for genero in lista_genero:
            set_generos.add(genero)
        objeto : None = Anime(nombre = lista_split[0], capitulos = int(lista_split[1]),
                              puntaje = int(lista_split[2]), estreno = int(lista_split[3]),
                              estudio = lista_split[4], generos = set_generos)
        lista_nametuples.append(objeto)
        set_generos = set()
    return lista_nametuples


#####################################
#        Parte 2 - Consultas        #
#####################################
def animes_por_estreno(animes: list) -> dict:
    dic_base : dir = {}
    lista_anos : list = []
    lista_animes_por_ano : list = []
    
    for anime in animes:
        ano : str = anime[3]
        lista_anos.append(ano)
    
    for anio in lista_anos:
        for anime_1 in animes:
            if anime_1[3] == anio:
                lista_animes_por_ano.append(anime_1[0])
            else:
                pass
        dic_base[anio] = lista_animes_por_ano
        lista_animes_por_ano : list = []
    
    return dic_base


def descartar_animes(generos_descartados: set, animes: list) -> list:
    
    lista_descartados : list = []
    no_descartado : int = 0
    
    for anime in animes:
        set_generos : set = anime[5]
        
        for genero in set_generos:
            if genero in generos_descartados:
                no_descartado : int = 1
            else:
                pass
        
        if no_descartado == 0:
            lista_descartados.append(anime[0])  
        else:
            no_descartado : int = 0    
                  
    return lista_descartados


def resumen_animes_por_ver(*animes: Anime) -> dict:
    
    dic_1 = {}
    suma_puntaje : float = 0
    suma_capitulos : int = 0
    set_generos : set = set()
    
    for anime in animes:
        suma_puntaje += float(anime[2])
        suma_capitulos += anime[1]
        set_generos = set_generos | anime[5]
    
    if len(animes) == 0:
        dic_1['puntaje promedio'] = 0
        
    else:
        dic_1['puntaje promedio'] = round(suma_puntaje/len(animes), 1)
        
    dic_1['capitulos total'] = suma_capitulos
    dic_1['generos'] = set_generos
    
    return dic_1


def estudios_con_genero(genero: str, **estudios: list) -> list:
    estudios_con_genero : list = []
    for estudio in estudios:
        objeto : None = estudios[estudio]
        


if __name__ == "__main__":
    #####################################
    #       Parte 1 - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte 2 - Consultas        #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
