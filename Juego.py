import pygame
from constantes import *
from preguntas import *
from funciones import *
from game_over import *

pygame.init()

# FUENTES DEL JUEGO
fuente_pregunta = pygame.font.SysFont('impact', 30) 
fuente_respuesta = pygame.font.SysFont('arial', 25) 
fuente_portatil = pygame.font.Font('fuentes/Minecraft.ttf', 28)
fuente_cronometro = pygame.font.Font('fuentes/Minecraft.ttf', 38)


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

lista_preguntas = cargar_preguntas_csv('preguntas.csv')

posiciones_botones = [(650,290), (650,360), (650,430), (650,500)]

# CARGAR IMAGENES DE LAS RESPUESTAS Y POSICIONAR
cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
claves_botones = [OPCION_1, OPCION_2, OPCION_3, OPCION_4]

bandera_respuesta = False
contador_respuestas_correctas = 0
cronometro = 15
ultimo_tiempo = pygame.time.get_ticks()
contador_correctas_constantes = 0 # -----------------------
mostrar_messi_feliz = 0
mostrar_messi_enojado = 0

# COMODINES
comodin_multiplicar = True  # Comodín de multiplicar disponible
comodin_pasar = True        # Comodín de pasar disponible
multiplicar_activado = False  # Estado de activación del comodín multiplicar
pasar_activado = False       # Estado de activación del comodín pasar

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    global indice
    global lista_preguntas
    global bandera_respuesta
    global cartas_respuestas
    global contador_respuestas_correctas
    global cronometro
    global ultimo_tiempo
    global contador_correctas_constantes # -----------------------
    global mostrar_messi_feliz
    global mostrar_messi_enojado
    global comodin_multiplicar   # Comodín de multiplicar disponible
    global comodin_pasar         # Comodín de pasar disponible
    global multiplicar_activado # Indica si el comodín multiplicar está activo
    global pasar_activado    
    
    pygame.display.set_caption('JUEGO')
    if bandera_respuesta == True:
        cartas_respuestas = cargar_botones_y_posicionar(imagenes_respuestas,posiciones_botones)
        cronometro = 15 
        bandera_respuesta = False
    retorno = 'jugar'

    # ACTUALIZAR CRONOMETRO
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo >= 1000: 
        cronometro -= 1
        ultimo_tiempo = tiempo_actual
    # SI LLEGA A 0, INCORRECTA
    if cronometro <= 0:
        marcar_respuesta_incorrecta(datos_juego)
        mostrar_messi_enojado = 30
        indice += 1
        contador_correctas_constantes = 0 # -----------------------
        bandera_respuesta = True
        if indice == len(lista_preguntas):
            indice = 0
        
        if indice >= len(lista_preguntas):
            reiniciar_datos_juego(datos_juego)
            retorno = 'game_over'

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
        
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_2 and comodin_multiplicar:
            comodin_multiplicar = False  # Marcar el comodín como usado
            multiplicar_activado = True  # Activar el efecto
            print("Comodín de multiplicar activado.")

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_4 and comodin_pasar:
            comodin_pasar = False
            pasar_activado = True
            print("Comodín de pasar activado.")
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pasar_activado:
                pasar_activado = False
                indice += 1
                bandera_respuesta = True
                cronometro = 15
                if indice >= len(lista_preguntas):
                    indice = 0
                    retorno = 'game_over'
                print("Pregunta pasada por comodín.")
                return retorno
            
            
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    CLICK_PELOTAZO.play()
                    cartas_respuestas[i]['superficie'] = pygame.image.load(imagenes_respuestas_seleccionadas[i])
                    respuesta_actual = i + 1
                    
                    if respuesta_actual == pregunta_actual['respuesta_correcta']:
                        marcar_respuesta_correcta(datos_juego)
                        mostrar_messi_feliz = 30
                        
                        # Multiplicar el puntaje si el comodín está activo
                        if multiplicar_activado:
                            datos_juego['puntuacion'] += 2 * PUNTOS_POR_PREGUNTA
                            multiplicar_activado = False
                            print("Puntaje multiplicado por comodín.")

                        # CONTAR CORRECTAS
                        contador_respuestas_correctas += 1
                        contador_correctas_constantes += 1

                        if contador_correctas_constantes == 5: 
                                CLICK_GANASTE_VIDA.play()
                                if datos_juego['vidas'] < 3:
                                    datos_juego['vidas'] += 1
                                    contador_correctas_constantes = 0

                        if contador_respuestas_correctas >= CANTIDAD_PREGUNTAS_POR_NIVEL:
                            contador_respuestas_correctas = 0
                            if datos_juego['nivel_actual'] <= CANTIDAD_NIVELES:
                                datos_juego['nivel_actual'] += 1
                            else:
                                datos_juego['nivel_actual'] = 1
                                retorno = 'game_over'

                    else:
                        marcar_respuesta_incorrecta(datos_juego)
                        mostrar_messi_enojado = 30
                        contador_correctas_constantes = 0 
                    indice += 1
                    bandera_respuesta = True
                    if indice == len(lista_preguntas):
                        indice = 0
                        datos_juego['nivel_actual'] = 1
                        retorno = 'game_over'
    
    # CARGAR FUTBOLISTA SEGUN EL NIVEL ACTUAL
    cargar_y_mostrar_imagen(pantalla, f'img/fondo_juego_{datos_juego["nivel_actual"]}.png', VENTANA, (0, 0))

    # CONFIGURAR PREGUNTA
    carta_pregunta['superficie'] = pygame.Surface((400,200), pygame.SRCALPHA) 
    carta_pregunta['superficie'].fill(TRANSPARENTE)

    # AGREGAR TEXTO ALA PREGUNTA
    mostrar_texto(carta_pregunta['superficie'],pregunta_actual['pregunta'],(20,20),fuente_pregunta,COLOR_NEGRO)
    # AGREGAR TEXTO ALAS RESPUESTAS
    mostrar_texto(cartas_respuestas[0]['superficie'],pregunta_actual['respuesta_1'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]['superficie'],pregunta_actual['respuesta_2'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]['superficie'],pregunta_actual['respuesta_3'],(120,20),fuente_respuesta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]['superficie'],pregunta_actual['respuesta_4'],(120,20),fuente_respuesta,COLOR_NEGRO)
    
    
    # DIBUJAR y UBICAR PREGUNTA
    pantalla.blit(carta_pregunta['superficie'], (680, 150))

    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil_game.png', VENTANA, (0, 0))
    # VIDAS
    dibujar_corazones_vidas(datos_juego['vidas'],pantalla)
    # PUNTUACION
    mostrar_texto(pantalla,f'Puntuacion:{datos_juego["puntuacion"]}',(835,630),fuente_portatil,COLOR_BLANCO)
    # CRONOMETRO
    mostrar_texto(pantalla,f"{cronometro}",(600, 64), fuente_cronometro,  COLOR_BLANCO) 
    # CARGAR MESSI
    if mostrar_messi_feliz > 0:
        cargar_y_mostrar_imagen(pantalla,'img/messi_feliz.png',(73,124),(570,580))
        # SE VA REDUCIENDO CADA IMPRESION HASTA CERO
        mostrar_messi_feliz -=1
    elif mostrar_messi_enojado> 0:
        cargar_y_mostrar_imagen(pantalla,'img/messi_enojado.png',(73,124),(570,580))
        # SE VA REDUCIENDO CADA IMPRESION HASTA CERO
        mostrar_messi_enojado-=1
    else:
        cargar_y_mostrar_imagen(pantalla,'img/messi_concentrado.png',(73,124),(570,580))
    
    # DIBUJAR LAS RESPUESTAS
    for i in range(len(cartas_respuestas)):
        pantalla.blit(cartas_respuestas[i]['superficie'],cartas_respuestas[i]['rectangulo'])
    
    if datos_juego['vidas'] <= 0:
        cargar_y_mostrar_imagen(pantalla,'img/messi_concentrado.png',(73,124),(570,580))
        retorno = 'game_over'
        CLICK_GAME_OVER.play()
        indice = 0
        
    return retorno

    