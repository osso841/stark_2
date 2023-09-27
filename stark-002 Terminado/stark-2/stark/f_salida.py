from f_calculos import *

def mostrar_nombres_genero_NB(lista_personajes:list) -> None: #A
    """
    muestra por consola una lista completa de todos los personajes por genero NB
    Args:
        lista_personajes: lista de diccionarios que representa los superheroes
    Return: 
        None
    """
    lista_personajes_NB = listar_personajes_caracteristica(lista_personajes, "NB", "genero")

    mensaje = f"PERSONAJES GENERO NB:\n {obtener_mensaje_lista_heroes(lista_personajes_NB)}"
    print(mensaje)


def mostrar_superheroe_mas_alto_genero_F(lista_personajes:list) -> None: #B
    """
    muestra por consola los superheroes mas altos por genero Femenino
    Args:
        lista_personajes: lista de diccionarios que representa los superheroes
    Return: 
        None
    """
    lista_personajes_F = listar_personajes_caracteristica(lista_personajes, "F", "genero")
    lista_personajes_F_altos = listar_personajes_caracteristica(lista_personajes_F, obtener_maximo(lista_personajes_F, 'altura'), 'altura')
    mensaje = f"PERSONAJES GENERO F MAS ALTO:\n {obtener_mensaje_lista_heroes(lista_personajes_F_altos)}"
    print(mensaje)


def mostrar_superheroe_mas_alto_genero_M(lista_personajes:list) -> None: #C
    """
    muestra por consola los superheroes mas altos por genero Masculino
    Args:
        lista_personajes: lista de diccionarios que representa los superheroes
    Return: 
        None
    """
    lista_personajes_M = listar_personajes_caracteristica(lista_personajes, "M", "genero")
    lista_personajes_M_altos = listar_personajes_caracteristica(lista_personajes_M, obtener_maximo(lista_personajes_M, 'altura'), 'altura')
    mensaje = f"PERSONAJES GENERO M MAS ALTO:\n {obtener_mensaje_lista_heroes(lista_personajes_M_altos)}"
    print(mensaje)


def mostrar_superheroe_mas_debil_genero_M(lista_personajes:list) -> None: #D
    """
    muestra por consola los superheroes mas debiles por genero Masculino
    Args:
        lista_personajes: lista de diccionarios que representa los superheroes
    Return: 
        None
    """
    lista_personajes_M = listar_personajes_caracteristica(lista_personajes, "M", "genero")
    lista_personajes_M_debil = listar_personajes_caracteristica(lista_personajes_M, obtener_minimo(lista_personajes_M, 'fuerza'), 'fuerza')
    mensaje = f"PERSONAJES GENERO M MAS DEBIL:\n {obtener_mensaje_lista_heroes(lista_personajes_M_debil)}"
    print(mensaje)


def mostrar_superheroe_mas_debil_genero_NB(lista_personajes:list) -> None: #E
    """
    muestra por consola los superheroes mas debiles por genero No Binario
    Args:
        lista_personajes: lista de diccionarios que representa los superheroes
    Return: 
        None
    """
    lista_personajes_NB = listar_personajes_caracteristica(lista_personajes, "NB", "genero")
    lista_personajes_NB_debil = listar_personajes_caracteristica(lista_personajes_NB, obtener_minimo(lista_personajes_NB, 'fuerza'), 'fuerza')
    mensaje = f"PERSONAJES GENERO NB MAS DEBIL:\n {obtener_mensaje_lista_heroes(lista_personajes_NB_debil)}"
    print(mensaje)


def mostrar_fuerza_promedio_genero_NB(lista_personajes:list) -> None: #F
    """
    muestra por consola el promedio de fuerza de genero NB

    Args:
        lista_personajes(list): lista de diccionarios que representan los personajes

    Return:
        None
    """
    lista_personajes_NB = listar_personajes_caracteristica(lista_personajes, "NB", "genero")
    fuerza_promedio_genero_NB = calcular_promedio(lista_personajes_NB, "fuerza")
    mensaje = f"Fuerza Promedio de Genero NB: {fuerza_promedio_genero_NB:.2f}"
    print(mensaje)


def mostrar_cantidad_superheroes_por_color_ojos(lista_personajes:list) -> None: #G ---
    """
    muestra la cantidad de superheroes por color de ojos de una lista de personajes

    Args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        None
    """

    print("MOSTRAR CANTIDAD HEROES POR COLOR DE OJOS:")
    diccionario_superheroes_por_color_ojos = agrupar_superheroes_segun_caracteristica(lista_personajes, "color_ojos")
    mensaje = armar_mensaje_cantidad_superheroes_por_caracteristica(diccionario_superheroes_por_color_ojos)
    print(mensaje)


def mostrar_cantidad_superheroes_por_color_pelo(lista_personajes:list) -> None: #H
    """
    Muestra la cantidad de superheroes por color de pelo de una lista de personajes

    Args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        None
    """

    print("MOSTRAR CANTIDAD HEROES POR COLOR DE PELO:")
    diccionario_superheroes_por_color_pelo = agrupar_superheroes_segun_caracteristica(lista_personajes, "color_pelo")
    mensaje = armar_mensaje_cantidad_superheroes_por_caracteristica(diccionario_superheroes_por_color_pelo)
    print(mensaje)


def mostrar_superheroes_segun_color_ojos(lista_personajes:list) -> None: #I
    """
    muestra una lista de  superheroes agrupados por color de ojos

    Args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        None
    """


    print("PERSONAJES SEGUN COLOR DE OJOS:")
    diccionario_superheroes_por_color_ojos = agrupar_superheroes_segun_caracteristica(lista_personajes, "color_ojos")
    mensaje = armar_mensaje_superheroes_segun_caracteristica(diccionario_superheroes_por_color_ojos)
    print(mensaje)


def mostrar_superheroes_segun_inteligencia(lista_personajes:list) -> None: #J
    """
    Muestra una lista de personajes agrupados segun su inteligencia
    
    Args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        None
    """


    print("PERSONAJES SEGUN INTELIGENCIA:")
    diccionario_superheroes_por_color_pelo = agrupar_superheroes_segun_caracteristica(lista_personajes, "inteligencia")
    mensaje = armar_mensaje_superheroes_segun_caracteristica(diccionario_superheroes_por_color_pelo)
    print(mensaje)


def mostrar_menu():
    '''
    Imprime el menu en consola

    Args:
        None

    Return:
        None
    '''
    mi_menu = '''
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
    B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
    E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
    F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
    G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    I. Listar todos los superhéroes agrupados por color de ojos.
    J. Listar todos los superhéroes agrupados por tipo de inteligencia
    '''    
    print(mi_menu)


def iniciar_consulta(lista_personajes:list) ->None: #inicializar consulta
    """
    Inicia el programa de consultas sobre la lista de superhéroes.

    Args:
        lista_personajes (list): Lista de superhéroes.

    Returns:
        None
    """
    """
    Diccionario que mapea las opciones del menú a las funciones correspondientes.

    Cada clave representa una opción del menú y su valor es la función que se debe ejecutar
    al seleccionar esa opción.
    """
    diccionario_consultas = {
                            'a': mostrar_nombres_genero_NB,
                            'b': mostrar_superheroe_mas_alto_genero_F,
                            'c': mostrar_superheroe_mas_alto_genero_M,
                            'd': mostrar_superheroe_mas_debil_genero_M,
                            'e': mostrar_superheroe_mas_debil_genero_NB,
                            'f': mostrar_fuerza_promedio_genero_NB,
                            'g': mostrar_cantidad_superheroes_por_color_ojos,
                            'h': mostrar_cantidad_superheroes_por_color_pelo,
                            'i': mostrar_superheroes_segun_color_ojos,
                            'j': mostrar_superheroes_segun_inteligencia,
                            'x': lambda x: print('salir programa')
                            }


    while True:
        mostrar_menu()
        opcion = input('opcion: ').lower()
        if opcion in diccionario_consultas.keys():
            diccionario_consultas[opcion](lista_personajes)
            if opcion == 'x':
                break
        else:
            print('ERROR. INGRESE OTRA OPCION')
        