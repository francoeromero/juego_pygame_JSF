import pygame
from constantes import *
from preguntas import *
from funciones import *
from game_over import *

pygame.init()

# FUENTES DEL JUEGO
fuente_pregunta = pygame.font.SysFont('impact', 30) 
fuente_respuesta = pygame.font.SysFont('arial', 25) 
fuente_portatil = pygame.font.Font('fuentes/Minecraft.ttf', 30)

indice = 1

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

# Comodines disponibles
# Comodines disponibles
comodines = {
    'x2': True,
    'pasar': True
}


# Teclas numéricas para activar los comodines
TECLA_COMODINES = {
    'x2': pygame.K_2,           # Tecla '2' para X2
    'pasar': pygame.K_4         # Tecla '4' para Pasar
}


lista_preguntas = cargar_preguntas_csv('preguntas.csv')

posiciones_botones = [(650,290), (650,360), (650,430), (650,500)]

# CARGAR IMAGENES DE LAS RESPUESTAS Y POSICIONAR
cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
claves_botones = [OPCION_1, OPCION_2, OPCION_3, OPCION_4]

bandera_respuesta = False
contador_respuestas_correctas = 0
cronometro = 9
ultimo_tiempo = pygame.time.get_ticks()
contador_correctas_constantes = 0 # -----------------------


def activar_bomba(pregunta_actual):
    # Obtenemos las respuestas incorrectas
    respuestas_incorrectas = [i for i in range(4) if i != pregunta_actual['respuesta_correcta']]
    
    # Eliminar dos respuestas incorrectas (remover aleatoriamente o de alguna manera)
    if len(respuestas_incorrectas) > 2:
        respuestas_incorrectas = respuestas_incorrectas[:2]  # Dejamos solo dos respuestas incorrectas
    print("Respuestas incorrectas después de bomba: ", respuestas_incorrectas)

    return respuestas_incorrectas


def activar_x2(datos_juego):
    print(f"Puntuación duplicada: {datos_juego['puntuacion']}")



def activar_pasar():
    return True  # Saltar la pregunta



# FUENTES DEL JUEGO
fuente_comodines = pygame.font.SysFont('arial', 20)

def mostrar_comodines(pantalla, comodines):
    # Posición de los comodines en la esquina superior izquierda
    posicion_comodines = (10, 10)

    # Comodines disponibles
    texto_comodines = "Comodines: "
    
    if comodines['x2']:
        texto_comodines += "2: X2, "

    if comodines['pasar']:
        texto_comodines += "4: Pasar"

    if texto_comodines == "Comodines: ":
        texto_comodines = "No tiene comodines disponibles"
    # Mostrar los comodines disponibles
    mostrar_texto(pantalla, texto_comodines, posicion_comodines, fuente_comodines, COLOR_BLANCO)


def gestionar_comodines(cola_eventos, comodines, pregunta_actual, datos_juego):
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            print(f"Tecla presionada: {evento.key}")  # Verifica la tecla presionada
            # Verificar que la tecla presionada sea válida y que el comodín esté disponible
            for comodin, tecla in TECLA_COMODINES.items():
                if evento.key == tecla and comodines[comodin]:
                    comodines[comodin] = False  # Marcar como usado
                    
                    if comodin == 'x2':
                        activar_x2(datos_juego)
                        print("Comodín X2 activado.")
                    
                    elif comodin == 'pasar':
                        return True  # Indica que se salta la pregunta

    return False




def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    global indice
    global lista_preguntas
    global bandera_respuesta
    global cartas_respuestas
    global contador_respuestas_correctas
    global cronometro
    global ultimo_tiempo
    global contador_correctas_constantes # -----------------------

    salto_pregunta = gestionar_comodines(cola_eventos, comodines, lista_preguntas[indice], datos_juego)

    if salto_pregunta:
        indice += 1  # Saltar a la siguiente pregunta
        if indice == len(lista_preguntas):
            indice = 0  # Volver al inicio si se acaban las preguntas
        cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas, posiciones_botones)  # Reiniciar las respuestas gráficas
        bandera_respuesta = True  # Para indicar que se debe actualizar la pantalla



    pygame.display.set_caption('JUEGO')
    if bandera_respuesta == True:
        cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
        cronometro = 9 
        bandera_respuesta = False
    retorno = 'jugar'


    mostrar_comodines(pantalla,comodines)

    # ACTUALIZAR CRONOMETRO
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo >= 1000: 
        cronometro -= 1
        ultimo_tiempo = tiempo_actual
    # SI LLEGA A 0, INCORRECTA
    if cronometro <= 0:
        marcar_respuesta_incorrecta(datos_juego)
        indice += 1
        contador_correctas_constantes = 0 # -----------------------
        bandera_respuesta = True
        if indice == len(lista_preguntas):
            indice = 0

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
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    CLICK_PELOTAZO.play()
                    cartas_respuestas[i]['superficie'] = pygame.image.load(imagenes_respuestas_seleccionadas[i])
                    respuesta_actual = i + 1
                    if respuesta_actual == pregunta_actual['respuesta_correcta']:
                        if comodines ['x2']: 
                            datos_juego['puntuacion'] *= 2
                        else:
                            datos_juego['puntuacion'] += 10

                        marcar_respuesta_correcta(datos_juego)
                        # CONTAR CORRECTAS
                        contador_respuestas_correctas += 1
                        contador_correctas_constantes += 1# -----------------------

                        if contador_correctas_constantes == 5: # -----------------------
                                datos_juego['vidas'] += 1
                                contador_correctas_constantes = 0
                                CLICK_GANASTE_VIDA.play()

                        if contador_respuestas_correctas >= CANTIDAD_PREGUNTAS_POR_NIVEL:
                            contador_respuestas_correctas = 0
                            if datos_juego['nivel_actual'] <= CANTIDAD_NIVELES:
                                datos_juego['nivel_actual'] += 1
                            else:
                                retorno = 'game_over'

                    else:
                        marcar_respuesta_incorrecta(datos_juego)
                        contador_correctas_constantes = 0 # -----------------------
                    indice += 1
                    bandera_respuesta = True
                    if indice == len(lista_preguntas):
                        indice = 0
    
     # CARGAR FUTBOLISTA SEGUN EL NIVEL ACTUAL
    cargar_y_mostrar_imagen(pantalla, f'img/fondo_juego_{datos_juego['nivel_actual']}.png', VENTANA, (0, 0))

    # CONFIGURAR PREGUNTA
    carta_pregunta['superficie'] = pygame.Surface((615,200), pygame.SRCALPHA) 
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
    # CRONOMETRO
    mostrar_texto(pantalla,f"00:0{cronometro}",(580, 95), fuente_portatil,  COLOR_BLANCO) 

    # DIBUJAR LAS RESPUESTAS
    for i in range(len(cartas_respuestas)):
        pantalla.blit(cartas_respuestas[i]['superficie'],cartas_respuestas[i]['rectangulo'])

    mostrar_comodines(pantalla, comodines)
    
    
    if datos_juego['vidas'] <= 0:
        retorno = 'game_over'
        CLICK_GAME_OVER.play()
        indice = 0
        
    pygame.display.update()

    return retorno
