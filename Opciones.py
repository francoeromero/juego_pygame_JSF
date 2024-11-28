import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

boton_volver = {
    'superficie': pygame.image.load('img/boton_volver.png'),
    'rectangulo': pygame.Rect(150, 550, 163, 61)
}


def mostrar_opciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])->str:
    pygame.display.set_caption('OPCIONES')
    retorno = 'opciones'
    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                boton_volver['superficie'] = pygame.image.load('img/boton_volver_seleccionado.png')
                retorno = 'menu'

    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla,'img/fondo_opciones.png',VENTANA,(0,0))
    # CARGAR BOTON VOLVER
    cargar_y_mostrar_imagen(pantalla, 'img/boton_volver.png', (163,61), (150, 550))
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))
    
    # ACTUALIZAR BOTON VOLVER SELECCIONADO
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)
    # REINICIAR BOTON VOLVER SELECCIONADO
    boton_volver['superficie'] = pygame.image.load('img/boton_volver.png')
    boton_volver['rectangulo'] = pygame.Rect(150, 550, 163, 61)

    return retorno