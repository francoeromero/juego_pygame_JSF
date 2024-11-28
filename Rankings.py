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

margen_puesto = 230   # X inicial para el puesto
margen_fecha = 320 # X inicial para el fecha
margen_nombre = 560  # X inicial para el nombre
margen_puntuacion = 864  # X inicial para la puntuación
def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event], lista_ranking_ordenado)->str:
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
 
    
    for i, jugador in enumerate(lista_ranking_ordenado[:10]):
        puesto = str(i + 1)  # El puesto es simplemente el índice + 1
        nombre = jugador['nombre']
        puntuacion = jugador['puntuacion']
        fecha = jugador['fecha']
        # Crear texto para cada columna (con espacios fijos)
        texto_puesto = fuente_ranking.render(f"{puesto:^6}", True, COLOR_NEGRO)
        texto_fecha = fuente_ranking.render(f"{fecha:^10}", True, COLOR_NEGRO)
        texto_nombre = fuente_ranking.render(f"{nombre:<30}", True, COLOR_NEGRO)  # Alineado a la izquierda
        texto_puntuacion = fuente_ranking.render(f"{int(puntuacion):05d}", True, COLOR_NEGRO)  # Relleno con ceros a la izquierda

        # Dibujar texto en la pantalla
        pantalla.blit(texto_puesto, (margen_puesto, 315 + (i * 25)))  # Colocar el puesto
        pantalla.blit(texto_fecha, (margen_fecha, 315 + (i * 25)))  # Colocar el fecha
        pantalla.blit(texto_nombre, (margen_nombre, 315 + (i * 25)))  # Colocar el nombre
        pantalla.blit(texto_puntuacion, (margen_puntuacion, 315 + (i * 25)))  # Colocar la puntuación

    
    # ACTUALIZAR BOTON VOLVER SELECCIONADO
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)
    # REINICIAR BOTON VOLVER SELECCIONADO
    boton_volver['superficie'] = pygame.image.load('img/boton_volver.png')
    boton_volver['rectangulo'] = pygame.Rect(150, 550, 163, 61)
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil_game.png', VENTANA, (0, 0))
    # CARGAR MESSI
    cargar_y_mostrar_imagen(pantalla,'img/messi_concentrado.png',(73,124),(570,580))
    return retorno