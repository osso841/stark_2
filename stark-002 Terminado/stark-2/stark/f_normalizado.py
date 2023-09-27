def normalizar_lista_personajes(lista_personajes:list) -> list:
    """
    Normaliza los valores de 'fuerza', 'altura', 'peso', 'color_ojos', 'color_pelo' e 'inteligencia'  en la lista de personajes.

    Args:
        lista_personaje (list[dict]): Una lista de diccionarios respresentando personajes

    Returns:
        None

    Modifica la lista de personajes directamente, normalizando los valores de 'fuerza', 'altura', 'peso', 'color_ojos', 'color_pelo' e 'inteligencia'.

    """
    for personaje in lista_personajes:
        personaje['altura'] = float(personaje['altura'])
        personaje['peso'] = float(personaje['peso'])
        personaje['fuerza'] = float(personaje['fuerza'])
        personaje['color_ojos'] = str(personaje['color_ojos']).capitalize()
        personaje['color_pelo'] = str(personaje['color_pelo']).capitalize()
        personaje['inteligencia'] = str(personaje['inteligencia']).upper()

    return lista_personajes


def normalizar_mensaje_traduccion_superheroes(mensaje:str) -> str:
    """
    Normaliza un mensaje de traducción de superhéroes de inglés a español.

    Args:
        mensaje (str): El mensaje a normalizar.

    Returns:
        str: El mensaje traducido.
    """
    diccionario_traduccion = {  
                            "Brown":"Marron", 
                            "Yellow":"Amarillo",
                            "Blue":"Azul",
                            "Black":"Negro",
                            "Green":"Verde",
                            "Auburn":"Castaño",
                            "Yellow (without irises)":"Amarillo (sin iris)",
                            "Red / Orange":"rojo / naranja",
                            "Hazel":"Avellana",
                            "White":"Blanco",
                            "No Hair":"sin pelo",
                            "Blond":"Rubio",
                            "Silver":"Plateado",
                            "Brown / White":"Marrón / blanco",
                            "AVERAGE":"Promedio",
                            "GOOD":"Bueno",
                            "HIGH":"Alto", 
                            "Red": "Rojo"              
                            }

    for ingles, espanol in diccionario_traduccion.items():
        mensaje = mensaje.replace(ingles, espanol)
    return mensaje