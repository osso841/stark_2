from f_normalizado import normalizar_mensaje_traduccion_superheroes #aplicado armar_mensaje_superheroes_segun_caracteristica()

#----------------------------------------------------------------------------------

def obtener_maximo(lista_personajes:list, caracteristica:str) -> int | float:
    """
    Obtiene el máximo valor de una característica específica en una lista de personajes.

    Args:
        lista_personajes (list[dict]): Una lista de diccionarios representando personajes, donde cada diccionario
                                 debe contener la clave especificada en 'caracteristica'.
        caracteristica (str): La clave que se utilizará para obtener el valor máximo.

    Returns:
        int: El valor máximo de la característica especificada.
    """

    bandera_primer_valor = True
    maximo = None

    for personaje in lista_personajes:
        if bandera_primer_valor or personaje[caracteristica] > maximo:
            maximo = personaje[caracteristica]
            bandera_primer_valor = False
    
    return maximo


def obtener_minimo(lista_personajes:list, caracteristica:str) -> int | float:
    """
    Obtiene el minimo valor de una caracteristica espeficifica en una lista de personajes

    Args:
        lista_personajes (list[dict]): Una lista de diccionarios representando personajes, donde cada diccionario
                                 debe contener la clave especificada en 'caracteristica'.
        caracteristica (str): La clave que se utilizará para obtener el valor minimo.

    Returns:
        int: El valor minimo de la característica especificada.
    """

    bandera_primer_valor = True
    minimo = None

    for personaje in lista_personajes:
        if bandera_primer_valor or personaje[caracteristica] > minimo:
            minimo = personaje[caracteristica]
            bandera_primer_valor = False
    
    return minimo


def listar_personajes_caracteristica(lista_personajes:list, valor:str|int, caracteristica:str) -> list:
    """
    Obtiene una lista de personajes que tienen una característica específica y valor.

    Args:
        lista_personajes (List[dict]): Lista de personajes representados como diccionarios.
        valor : Valor que se busca en la característica.
        caracteristica (str): Característica a evaluar.

    Returns:
        List[dict]: Lista de personajes que cumplen con la condición.
    """
    
    lista_salida = []

    for personaje in lista_personajes:
        if valor == personaje[caracteristica]:
            lista_salida.append(personaje)

    return lista_salida

#----------------------------------------------------------------------------------

def calcular_promedio(lista_personajes:list, caracteristica:str) -> float: #aplicado f
    """
    Calcula el promedio de una característica específica en una lista de personajes.

    Args:
        lista_personajes (list[dict]): Lista de personajes representados como diccionarios.
        tipo_promedio (str): Característica para la cual se calculará el promedio.

    Returns:
        float: Promedio de la característica especificada.
    """

    acumulador_fuerza = 0
    contador_genero = 0
    promedio_fuerza_genero = 0

    for personaje in lista_personajes:
            acumulador_fuerza += personaje[caracteristica]
            contador_genero += 1

    if contador_genero != 0:
        promedio_fuerza_genero = acumulador_fuerza / contador_genero
        
    return promedio_fuerza_genero

#----------------------------------------------------------------------------------
def agrupar_superheroes_segun_caracteristica(lista_personajes:list, caracteristica_a_listar:str) -> dict:  #aplicado I j g h
    """
    Agrupa a los superhéroes según una característica especificada y devuelve un diccionario.

    Args:
        lista_personajes (list[dict]): Lista de diccionarios de personajes.
        caracteristica_a_listar (str): La característica por la cual se va a agrupar.

    Returns:
        dict: Un diccionario donde las claves son los valores de la característica y los valores son listas de nombres de superhéroes.

    """

    diccionario_caracteristica_salida = {}

    for personaje in lista_personajes:

        if personaje[caracteristica_a_listar] == "":
            continue

        if personaje[caracteristica_a_listar] not in diccionario_caracteristica_salida.keys():
            diccionario_caracteristica_salida[personaje[caracteristica_a_listar]] = []
        diccionario_caracteristica_salida[personaje[caracteristica_a_listar]].append(personaje['nombre'])

    return diccionario_caracteristica_salida


def armar_mensaje_cantidad_superheroes_por_caracteristica(superheroes_agrupados_por_caracteristicas:dict) -> str:  #aplicado g h
    """
    Arma un mensaje con la cantidad de superhéroes por cada característica y lo devuelve.

    Args:
        superheroes_agrupados_por_caracteristicas (dict): Un diccionario donde las claves son características y los valores son listas de nombres de superhéroes.

    Returns:
        str: Un mensaje con la cantidad de superhéroes por cada característica.

    """
    mensaje = ""
    for clave, valor in superheroes_agrupados_por_caracteristicas.items():
        mensaje += clave + f": {len(valor)} heroes.\n"

    mensaje = normalizar_mensaje_traduccion_superheroes(mensaje)

    return mensaje


def armar_mensaje_superheroes_segun_caracteristica(diccionario_superheroes_segun_caracteristica:dict) -> str: #aplicado I j
    """
    Arma un mensaje con superhéroes agrupados por característica y lo devuelve.

    Args:
        diccionario_superheroes_segun_caracteristica (dict): Un diccionario donde las claves son características y los valores son listas de nombres de superhéroes.

    Returns:
        str: Un mensaje con los superhéroes agrupados por característica.
    """
    mensaje = ""
    for caracteristica in list(diccionario_superheroes_segun_caracteristica.keys()):
        mensaje += f"\n{caracteristica}: {' - '.join(diccionario_superheroes_segun_caracteristica[caracteristica])}"

    mensaje = normalizar_mensaje_traduccion_superheroes(mensaje)

    return mensaje


def obtener_mensaje_lista_heroes(Lista_personajes:list[dict]) -> str:
    """
    devuelve un mensaje estructurado de una lista de diccionarios que representa los personajes

    args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Retunr:
        str: datos completos de los diccionarios de una lista
    """
    mensaje = ""
    for personaje in Lista_personajes:
        for clave, valor in personaje.items():
            if clave == 'nombre':
                mensaje += f"\n\n\t{valor.upper()}"
                continue

            mensaje += F"\n{clave:14} : {valor}"
    return mensaje