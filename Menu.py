import pygame
from constantes import *
from preguntas import *
from funciones import *
from Juego import *
pygame.init()

fuente_menu = pygame.font.SysFont('courier', 30) 

lista_botones = []

imagenes_botones = [
    'img/boton_iniciar.png',
    'img/boton_opciones.png',
    'img/boton_top10.png',
    'img/boton_salir.png'
]
posiciones_botones = [(750,180), (750,280), (750,380), (750,480)]

imagenes_botones_seleccionados = [
    'img/boton_iniciar_seleccionado.png',
    'img/boton_opciones_seleccionado.png',
    'img/boton_top10_seleccionado.png',
    'img/boton_salir_seleccionado.png'
]

# CARGAR IMAGENES DE LOS BOTONES SIN SELECCIONAR
# for nombre_imagen in imagenes_botones:
#     boton = {}
#     boton['superficie'] = pygame.image.load(nombre_imagen)
#     boton['rectangulo'] = boton['superficie'].get_rect()
#     lista_botones.append(boton)

contador_impresiones = 0
boton_seleccionado = None

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])->str:
    global contador_impresiones
    global boton_seleccionado

    pygame.display.set_caption('MENU')
    retorno = 'menu'

    lista_botones = cargar_botones_y_posicionar(imagenes_botones,posiciones_botones)
    # GESTION DE EVENTOS
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        # EVENTO CLICKS BOTONES
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            for i in range(len(lista_botones)):
                if lista_botones[i]['rectangulo'].collidepoint(evento.pos):
                    # COLOREAR EL BOTON SELECCIONADO
                    lista_botones[i]['superficie'] = pygame.image.load(imagenes_botones_seleccionados[i])
                    CLICK_SONIDO.play()
                    contador_impresiones += 1
                    boton_seleccionado = i

    # DELAY BOTON SELECCIONADO
    # CONTAR IMPRESIONES LUEGO DE SER SELECCIONADO 
    if contador_impresiones > 0:
        contador_impresiones += 1
    # CUANDO SUPERE EL LIMITE DE IMPRESIONES RECIEN RETORNA
    if contador_impresiones > DELAY_BOTON:
        # Reiniciar la lista de botones a su estado inicial (QUIZAS ESTO PUEDA HACER UNA FUNCION REINICIAR BOTONES)
        lista_botones.clear()
        for nombre_imagen in imagenes_botones:
            boton = {}
            boton['superficie'] = pygame.image.load(nombre_imagen)
            boton['rectangulo'] = boton['superficie'].get_rect()
            lista_botones.append(boton)

        contador_impresiones = 0
        if boton_seleccionado == BOTON_JUGAR:
            retorno = 'jugar'
        elif boton_seleccionado == BOTON_CONFIG:
            retorno = 'opciones'
        elif boton_seleccionado == BOTON_RANKINGS:
            retorno = 'rankings'
        elif boton_seleccionado == BOTON_SALIR:
            retorno = 'salir'



    # ACTUALIZACION DEL JUEGO
    
    # DIBUJAR EN PANTALLA
    # pintar el fondo de la pantalla

    # CARGAR FONDO PANTALLA
    cargar_y_mostrar_imagen(pantalla,'img/fondo_menu_ppal.png',VENTANA,(0,0))

    # UBICAR LOS BOTONES Y SELECCIONARLOS
    
    claves_botones = [BOTON_JUGAR, BOTON_CONFIG, BOTON_RANKINGS, BOTON_SALIR]
    for i in range(len(posiciones_botones)):
        lista_botones[claves_botones[i]]['rectangulo'] = pantalla.blit(lista_botones[claves_botones[i]]['superficie'], posiciones_botones[i])
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil_game.png', VENTANA, (0, 0))
    # CARGAR MESSI
    cargar_y_mostrar_imagen(pantalla,'img/messi_concentrado.png',(73,124),(570,580))

    return retorno