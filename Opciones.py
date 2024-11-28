import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

# Configuración inicial del botón "volver"
boton_volver = {
    'superficie': pygame.image.load('img/boton_volver.png'),
    'rectangulo': pygame.Rect(150, 550, 163, 61)
}

# Configuración inicial de la barra y la pelota
pelota_volumen = pygame.image.load('img/icono_pelota.png')  # Imagen circular o personalizada para la pelota

# Coordenadas y límites de la barra
barra_pos = (380, 380)  # EJE X E EJE Y DE LA PELOTA
barra_tamano = (400, 20)  # Dimensiones de la barra
pelota_pos_x = barra_pos[0]  # La pelota empieza alineada con el inicio de la barra
pelota_pos_y = barra_pos[1] - (pelota_volumen.get_height() // 2)  # Centrada verticalmente en la barra

pelota_arrastrando = False #bandera del arrastre
volumen = 0.5  # Volumen inicial (50%)

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
                # si se hizo clic sobre la pelota
                pelota_rect = pygame.Rect(pelota_pos_x, pelota_pos_y, pelota_volumen.get_width(), pelota_volumen.get_height())
                if pelota_rect.collidepoint(evento.pos):
                    pelota_arrastrando = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            pelota_arrastrando = False

    # Movimiento de la pelota
    if pelota_arrastrando:
        mouse_x, _ = pygame.mouse.get_pos()
        pelota_pos_x = max(barra_pos[0], min(mouse_x, barra_pos[0] + barra_tamano[0]))
        volumen = (pelota_pos_x - barra_pos[0]) / barra_tamano[0]  # Calcular volumen (0.0 a 1.0)
        pygame.mixer.music.set_volume(volumen)  # Ajustar volumen global del juego

    # Dibujar elementos en pantalla
    cargar_y_mostrar_imagen(pantalla, 'img/fondo_opciones.png', VENTANA, (0, 0))  # Fondo del menú
    cargar_y_mostrar_imagen(pantalla, 'img/boton_volver.png', (163, 61), (150, 550))  # Botón volver

    pantalla.blit(pelota_volumen, (pelota_pos_x, pelota_pos_y))  # Dibujar la pelota sobre la barra

    # Actualizar botón volver seleccionado
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)
    # Reiniciar botón volver seleccionado
    boton_volver['superficie'] = pygame.image.load('img/boton_volver.png')
    boton_volver['rectangulo'] = pygame.Rect(150, 550, 163, 61)

    return retorno
