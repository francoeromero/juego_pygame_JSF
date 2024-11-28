import pygame
from constantes import *
from funciones import *
import json

boton_salir = crear_diccionario_boton('img/boton_salir_game_over.png',(150, 500))
boton_salir_seleccionado = crear_diccionario_boton('img/boton_salir_game_over_seleccionado.png',(150, 500))
boton_cargar = crear_diccionario_boton('img/boton_cargar.png',(900, 500))
boton_cargar_seleccionado = crear_diccionario_boton('img/boton_cargar_seleccionado.png',(900, 500))
nombre = ''


def mostrar_game_over(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], datos_juego:dict)->str:
    global nombre
    pygame.display.set_caption('GAME_OVER')
    retorno = 'game_over'
    # GESTION DE EVENTOS
    
    fuente_game_over = pygame.font.SysFont(None, 40) 
    fuente_game_over_puntuacion = pygame.font.SysFont(None, 80) 
    mensaje_error = ''
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                boton_salir['superficie'] = boton_salir_seleccionado['superficie']
                reiniciar_datos_juego(datos_juego)
                retorno = 'menu'
            if boton_cargar['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if nombre.isalpha():
                    guardar_datos_en_json(FECHA_ACTUAL,nombre, datos_juego['puntuacion'])
                    reiniciar_datos_juego(datos_juego)
                    retorno = 'menu'
                else:
                    mensaje_error = "El nombre solo debe contener letras."
        #---------
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:  # Guarda al presionar enter
                if nombre.isalpha():
                    guardar_datos_en_json(FECHA_ACTUAL,nombre, datos_juego['puntuacion'])
                    reiniciar_datos_juego(datos_juego)
                    
                    retorno = 'menu'
                else:
                    mensaje_error = "El nombre solo debe contener letras."
            elif evento.key == pygame.K_BACKSPACE: 
                nombre = nombre[:-1]
            else:
                if len(nombre) < 12:
                    nombre += evento.unicode  # Agregar el carácter ingresado al nombre


    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla,'img/fondo_puntuacion.png',VENTANA,(0,0))
    # CARGAR BOTON SALIR
    cargar_y_mostrar_imagen(pantalla, 'img/boton_salir_game_over.png', (163,61), (150, 500))
    # CARGAR BOTON CARGAR
    cargar_y_mostrar_imagen(pantalla, 'img/boton_cargar.png', (163,61), (900, 500))
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil_game.png', VENTANA, (0, 0))
    
    #Puntaje
    puntaje_texto = fuente_game_over_puntuacion.render(f"{datos_juego['puntuacion']}", True, (COLOR_NEGRO))
    pantalla.blit(puntaje_texto, (470, 260))
    
    #Rectangulo nombre
    input_rect = pygame.Rect(770, 380, 200, 40)
    
    texto_nombre = fuente_game_over.render(nombre, True, (COLOR_NEGRO))
    pantalla.blit(texto_nombre, (input_rect.x + 5, input_rect.y + 5))
    
    if mensaje_error:
        error_texto = fuente_game_over.render(mensaje_error, True, (255, 100, 100))
        pantalla.blit(error_texto, (150, 440))

                    
    return retorno