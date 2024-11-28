import pygame
from constantes import *
from funciones import *
from Menu import mostrar_menu
from Juego import mostrar_juego
from Opciones import mostrar_opciones
from Rankings import mostrar_rankings
from game_over import mostrar_game_over

pygame.init()

datos_juego = {'puntuacion': 0,
                'vidas': CANTIDAD_VIDAS,
                'volumen_musica': 100,
                'acumulador_correctas': 0,
                'nivel_actual' : 1}

lista_ranking_ordenado = quick_sort(cargar_datos_json("puntajes.json"), 'puntuacion')
#----------------------------------------------------
# Configuraciones basicas de mi juego
pygame.display.set_caption('PREGUNTA Y GOL!!')
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)

# MUSICA DE FONDO
pygame.mixer.music.load('sonidos/musica.mp3')
pygame.mixer.music.set_volume(0.1) 
pygame.mixer.music.play(-1)

# Configurar la pantalla
# pantalla = pygame.display.set_mode((VENTANA))
corriendo = True
reloj = pygame.time.Clock()



ventana_actual = 'menu'
#----------------------------------------------------
# CARGAR FONDO ANIMADO
fotogramas = []
fotogramas = cargar_fondo_animado('fondo_animado', 20)



while corriendo:
    # CARGAR FONDO ANIMADO
    actualizar_fotograma(pantalla,fotogramas,VELOCIDAD_FONDO)

    cola_eventos = pygame.event.get()
    reloj.tick(FPS)


    if ventana_actual == 'menu':
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == 'jugar':
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == 'opciones':
        ventana_actual = mostrar_opciones(pantalla,cola_eventos)
    elif ventana_actual == 'rankings':
        ventana_actual = mostrar_rankings(pantalla,cola_eventos, lista_ranking_ordenado[:10])
    elif ventana_actual == 'game_over':
        ventana_actual = mostrar_game_over(pantalla,cola_eventos, datos_juego)
    elif ventana_actual == 'salir':
        print('SALIENDO')
        corriendo = False

    pygame.display.flip()

pygame.quit()