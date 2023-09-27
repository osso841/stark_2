from f_salida import *
from f_normalizado import normalizar_lista_personajes
from data_stark import lista_personajes
from copy import deepcopy

lista_normalizada_personajes = deepcopy(lista_personajes)
lista_normalizada_personajes = normalizar_lista_personajes(lista_normalizada_personajes)

iniciar_consulta(lista_normalizada_personajes)