import pygame
import random
from constantes import *
from preguntas import *
from funciones import *
from game_over import *

pygame.init()

# FUENTES DEL JUEGO
fuente_pregunta = pygame.font.SysFont('impact', 30) 
fuente_respuesta = pygame.font.SysFont('arial', 25) 
fuente_portatil = pygame.font.Font('fuentes/Minecraft.ttf', 30)

indice = 0

# datos_juego = {'puntuacion': 0,
#                 'vidas': CANTIDAD_VIDAS,
#                 'volumen_musica': 100,
#                 'acumulador_correctas': 0}

# OPCIONES RESPUESTAS
imagenes_respuestas = [
    'img/OPCION_1.png',
    'img/OPCION_2.png',
    'img/OPCION_3.png',
    'img/OPCION_4.png'
]

imagenes_respuestas_seleccionadas = [
    'img/OPCION_1_seleccionada.png',
    'img/OPCION_2_seleccionada.png',
    'img/OPCION_3_seleccionada.png',
    'img/OPCION_4_seleccionada.png'
]


posiciones_botones = [(650,290), (650,360), (650,430), (650,500)]


comodines = {"bomba": 1, "x2": 1, "doble_chance": 1, "pasar": 1}
comodin_usado = {"bomba": False, "x2": False, "doble_chance": False, "pasar": False}  # Estado de los comodines


def eliminar_respuesta_incorrecta(pregunta_actual, cartas_respuestas):
    # Encontrar las respuestas incorrectas
    respuestas_incorrectas = [i for i in range(4) if i + 1 != pregunta_actual['respuesta_correcta']]
    
    # Seleccionar una respuesta incorrecta al azar
    respuesta_a_eliminar = random.choice(respuestas_incorrectas)

    # PONGO UNA BARRA PARA "ELIMINAR" UNA RESPUESTA INCORRECTA
    cartas_respuestas[respuesta_a_eliminar]['superficie'].fill((169, 169, 169))  # Gris
    pregunta_actual[f'respuesta_{respuesta_a_eliminar + 1}'] = "Eliminada"

def activar_comodin(comodines, comodin_usado, tipo_comodin, clave_comodin, pregunta_actual):
    if comodines[clave_comodin] > 0 and not comodin_usado[clave_comodin]:
        comodines[clave_comodin] -= 1
        comodin_usado[clave_comodin] = True
        print(f"COMODIN {tipo_comodin} ACTIVADO")
        
        # Si es el comodín bomba, eliminamos una respuesta incorrecta
        if clave_comodin == "bomba":
            eliminar_respuesta_incorrecta(pregunta_actual, cartas_respuestas)
        return True
    return False


# CARGAR IMAGENES DE LAS RESPUESTAS Y POSICIONAR
cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas, posiciones_botones)
claves_botones = [OPCION_1, OPCION_2, OPCION_3, OPCION_4]

bandera_respuesta = False

def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    global indice
    global bandera_respuesta
    global cartas_respuestas
    
    pygame.display.set_caption('JUEGO')
    if bandera_respuesta == True:
        cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas, posiciones_botones)
        bandera_respuesta = False
    retorno = 'jugar'

    # CREAR LA PREGUNTA
    carta_pregunta = {}
    carta_pregunta['superficie'] = pygame.Surface(TAMAÑO_PREGUNTA)
    carta_pregunta['rectangulo'] = carta_pregunta['superficie'].get_rect()


    # PREGUNTA inicializar
    pregunta_actual = lista_preguntas[indice]

    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'

        if evento.type == pygame.KEYDOWN:  # Eventos de teclas para comodines
            if evento.key == pygame.K_c:  # COMODIN bomba
                if activar_comodin(comodines, comodin_usado, "BOMBA", "bomba", pregunta_actual):
                    eliminar_respuesta_incorrecta(pregunta_actual, cartas_respuestas)
                    
            elif evento.key == pygame.K_x:  # Comodín X2
                if activar_comodin(comodines, comodin_usado, "X2", "x2", pregunta_actual):
                    # LOGICA DEL X2
                    pass
            elif evento.key == pygame.K_d:  # Comodín doble chance
                if activar_comodin(comodines, comodin_usado, "DOBLE CHANCE", "doble_chance", pregunta_actual):
                    # LOGICA DEL DOBLE CHANCE
                    pass
            elif evento.key == pygame.K_p:  # Comodín pasar
                if activar_comodin(comodines, comodin_usado, "PASAR", "pasar", pregunta_actual):
                    # LOGICA DEL PASAR
                    pregunta_actual, cartas_respuestas = mostrar_texto()
                    bandera_respuesta = True
                    continue

        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    CLICK_PELOTAZO.play()
                    cartas_respuestas[i]['superficie'] = pygame.image.load(imagenes_respuestas_seleccionadas[i])
                    if i + 1 == pregunta_actual['respuesta_correcta']:
                        marcar_respuesta_correcta(datos_juego)
                        datos_juego['nivel_actual'] = 2
                    else:
                        marcar_respuesta_incorrecta(datos_juego)
                    indice += 1
                    bandera_respuesta = True
                    if indice == len(lista_preguntas):
                        indice = 0
    
    if datos_juego['nivel_actual'] == 1:
        cargar_y_mostrar_imagen(pantalla, 'img/fondo_juego_1.png', VENTANA, (0, 0))
    elif datos_juego['nivel_actual'] == 2:
        cargar_y_mostrar_imagen(pantalla, 'img/fondo_juego_2.png', VENTANA, (0, 0))

    # CONFIGURAR PREGUNTA
    carta_pregunta['superficie'] = pygame.Surface((650,200), pygame.SRCALPHA) 
    carta_pregunta['superficie'].fill(TRANSPARENTE)

    # AGREGAR TEXTO ALA PREGUNTA
    mostrar_texto(carta_pregunta['superficie'],pregunta_actual['pregunta'],(20,20),fuente_pregunta,COLOR_NEGRO)
    # AGREGAR TEXTO ALAS RESPUESTAS
    mostrar_texto(cartas_respuestas[0]['superficie'],pregunta_actual['respuesta_1'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]['superficie'],pregunta_actual['respuesta_2'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]['superficie'],pregunta_actual['respuesta_3'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]['superficie'],pregunta_actual['respuesta_4'],(120,20),fuente_respuesta,COLOR_NEGRO)
    
    # DIBUJAR y UBICAR PREGUNTA
    pantalla.blit(carta_pregunta['superficie'], (500, 150))

    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))
    # VIDAS
    dibujar_corazones_vidas(datos_juego['vidas'],pantalla)
    # PUNTUACION
    mostrar_texto(pantalla,f'{datos_juego["puntuacion"]}',(830,643),fuente_portatil,COLOR_BLANCO)

    # DIBUJAR LAS RESPUESTAS
    for i in range(len(cartas_respuestas)):
        pantalla.blit(cartas_respuestas[i]['superficie'],cartas_respuestas[i]['rectangulo'])

    #AGREGAR TEXTO COMODINES
    mostrar_texto(pantalla, f"Bomba: {comodines['bomba']}", (10, 10), fuente_portatil, COLOR_BLANCO)
    mostrar_texto(pantalla, f"X2: {comodines['x2']}", (10, 40), fuente_portatil, COLOR_BLANCO)
    mostrar_texto(pantalla, f"Doble Chance: {comodines['doble_chance']}", (10, 70), fuente_portatil, COLOR_BLANCO)
    mostrar_texto(pantalla, f"Pasar: {comodines['pasar']}", (10, 100), fuente_portatil, COLOR_BLANCO)

    if datos_juego['vidas'] <= 0:
        retorno = 'game_over'
        CLICK_GAME_OVER.play()
        
    return retorno
