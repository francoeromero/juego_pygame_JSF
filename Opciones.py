import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

boton_volver = {
    'superficie': pygame.image.load('img/boton_volver.png'),
    'rectangulo': pygame.Rect(150, 550, 163, 61)
}

# Configuración inicial de la barra y la pelota
pelota_volumen = pygame.image.load('img/icono_pelota.png')  # Imagen de la pelota


            #EJE(x), EJE(y)
posicion_barra = (380, 380)  # Coordenadas de la esquina superior izquierda de la barra
tamanio_barra = (400, 20)  # Dimensiones de la barra
pelota_pos_x = posicion_barra[0]  # La pelota empieza alineada con el inicio de la barra
pelota_pos_y = posicion_barra[1] - (pelota_volumen.get_height() // 2)  # Centrada verticalmente en la barra

pelota_arrastrando = False  # Estado de arrastre
volumen = 0.5  # Volumen inicial

def mostrar_opciones(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    global pelota_pos_x, pelota_arrastrando, volumen

    pygame.display.set_caption('OPCIONES')
    retorno = 'opciones'

    # Gestión de eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                boton_volver['superficie'] = pygame.image.load('img/boton_volver_seleccionado.png')
                retorno = 'menu'
            else:
                # Detectar si se hizo clic sobre la pelota
                pelota_rect = pygame.Rect(pelota_pos_x, pelota_pos_y, pelota_volumen.get_width(), pelota_volumen.get_height())
                if pelota_rect.collidepoint(evento.pos):
                    pelota_arrastrando = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            pelota_arrastrando = False

    # Movimiento de la pelota
    if pelota_arrastrando:
        mouse_x, _ = pygame.mouse.get_pos()
        pelota_pos_x = max(posicion_barra[0], min(mouse_x, posicion_barra[0] + tamanio_barra[0]))
        volumen = (pelota_pos_x - posicion_barra[0]) / tamanio_barra[0]  # Calcular volumen (0 a 1.0)
        pygame.mixer.music.set_volume(volumen)  # Ajustar volumen global del juego

    # Cargar fondo y mostrar en pantalla
    cargar_y_mostrar_imagen(pantalla,'img/fondo_opciones.png', VENTANA, (0, 0))

    # Cargar y mostrar el botón de volver
    cargar_y_mostrar_imagen(pantalla, 'img/boton_volver.png', (163, 61), (150, 550))

    # Cargar y mostrar el icono del portátil
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))

    # Cargar y mostrar la pelota en la posición actual
    pantalla.blit(pelota_volumen, (pelota_pos_x, pelota_pos_y))

    # Actualizar el botón de volver
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)

    return retorno
