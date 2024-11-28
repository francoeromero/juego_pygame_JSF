import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

fuente_ranking = pygame.font.Font('fuentes/Minecraft.ttf', 30)

boton_volver = {
    'superficie': pygame.image.load('img/boton_volver.png'),
    'rectangulo': pygame.Rect(150, 550, 163, 61)
}


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], lista_top_10: list)->str:
    pygame.display.set_caption('RANKINGS')
    retorno = 'rankings'
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
    cargar_y_mostrar_imagen(pantalla,'img/fondo_top10.png',VENTANA,(0,0))
    # CARGAR BOTON VOLVER
    cargar_y_mostrar_imagen(pantalla, 'img/boton_volver.png', (163,61), (150, 550))
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil.png', VENTANA, (0, 0))
    
    for i, jugador in enumerate(lista_top_10):
        puesto = str(i + 1)
        nombre = jugador['nombre']
        puntuacion = str(jugador['puntuacion'])
        
        
        texto = f"{puesto:^10}           {nombre:30}        {puntuacion:10}"

        
        # Renderizar el texto
        texto_surface = fuente_ranking.render(texto, True, COLOR_NEGRO)
        
        # Mostrar cada fila en la pantalla
        pantalla.blit(texto_surface, (260, 315 + (i * 25)))  
    
    # ACTUALIZAR BOTON VOLVER SELECCIONADO
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)
    # REINICIAR BOTON VOLVER SELECCIONADO
    boton_volver['superficie'] = pygame.image.load('img/boton_volver.png')
    boton_volver['rectangulo'] = pygame.Rect(150, 550, 163, 61)

    return retorno