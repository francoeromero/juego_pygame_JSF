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

# Configuración inicial del botón de volumen (como tecla)
boton_volumen = {
    'superficie': None,  # No cargamos una imagen, lo haremos con texto
    'rectangulo': pygame.Rect(700, 420, 60, 40),  # Tamaño de la tecla (60x40)
    'texto': 'Volumen',  # Texto para el botón
    'color_normal': (200, 200, 200),  # Color cuando no está presionado
    'color_presionado': (150, 150, 150)  # Color cuando se presiona
}

# Configuración inicial de la barra y la pelota
pelota_volumen = pygame.image.load('img/icono_pelota.png')  # Imagen circular o personalizada para la pelota

# Coordenadas y límites de la barra
barra_pos = (380, 380)  # EJE X E EJE Y DE LA PELOTA
barra_tamano = (400, 20)  # Dimensiones de la barra
pelota_pos_x = barra_pos[0]  # La pelota empieza alineada con el inicio de la barra
pelota_pos_y = barra_pos[1] - (pelota_volumen.get_height() // 2)  # Centrada verticalmente en la barra

pelota_arrastrando = False  # Bandera del arrastre
volumen = 0.5  # Volumen inicial (50%)
sonido_muteado = False  # Bandera de muteo

# Crear fuente para el texto
fuente = pygame.font.SysFont('Arial', 20)

def dibujar_boton_volumen(pantalla):
    # Dibujar el rectángulo del botón
    pygame.draw.rect(pantalla, boton_volumen['color_normal'], boton_volumen['rectangulo'])
    # Renderizar el texto en el botón
    texto_superficie = fuente.render(boton_volumen['texto'], True, (0, 0, 0))  # Texto negro
    texto_rect = texto_superficie.get_rect(center=boton_volumen['rectangulo'].center)
    pantalla.blit(texto_superficie, texto_rect)

def mostrar_opciones(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    global pelota_pos_x, pelota_arrastrando, volumen, sonido_muteado

    pygame.display.set_caption('OPCIONES')
    retorno = 'opciones'

    # Gestión de eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = 'menu'

            elif boton_volumen['rectangulo'].collidepoint(evento.pos):
                # Alternar entre mute y volumen normal
                if sonido_muteado:
                    volumen = 0.5  # Restaurar volumen
                    pygame.mixer.music.set_volume(volumen)
                    boton_volumen['texto'] = 'Volumen'  # Texto para volumen
                    boton_volumen['color_normal'] = (200, 200, 200)  # Color normal
                else:
                    volumen = 0  # Muteamos el volumen
                    pygame.mixer.music.set_volume(volumen)
                    boton_volumen['texto'] = 'Muteado'  # Texto para mute
                    boton_volumen['color_normal'] = (255, 100, 100)  # Color para estado muteado
                sonido_muteado = not sonido_muteado  # Alternar mute con el no mute

            # Verificar si se hizo clic sobre la pelota
            pelota_rect = pygame.Rect(pelota_pos_x, pelota_pos_y, pelota_volumen.get_width(), pelota_volumen.get_height())
            if pelota_rect.collidepoint(evento.pos):
                pelota_arrastrando = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            pelota_arrastrando = False

    # Movimiento de la pelota
    if pelota_arrastrando:
        mouse_x, _ = pygame.mouse.get_pos()
        pelota_pos_x = max(barra_pos[0], min(mouse_x, barra_pos[0] + barra_tamano[0]))  # Limitar movimiento de la pelota
        volumen = (pelota_pos_x - barra_pos[0]) / barra_tamano[0]  # Calcular volumen (0.0 a 1.0)
        pygame.mixer.music.set_volume(volumen)  # Ajustar volumen global del juego

    # Dibujar elementos en pantalla
    cargar_y_mostrar_imagen(pantalla, 'img/fondo_opciones.png', VENTANA, (0, 0))  # Fondo del menú
    cargar_y_mostrar_imagen(pantalla, 'img/boton_volver.png', (163, 61), (150, 550))  # Botón volver

    pantalla.blit(pelota_volumen, (pelota_pos_x, pelota_pos_y))  # Dibujar la pelota sobre la barra

    # Dibujar el botón de volumen (como tecla)
    dibujar_boton_volumen(pantalla)

    # Actualizar botón volver seleccionado
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'], boton_volver['rectangulo'].topleft)
    # Reiniciar botón volver seleccionado
    boton_volver['superficie'] = pygame.image.load('img/boton_volver.png')
    boton_volver['rectangulo'] = pygame.Rect(150, 550, 163, 61)
    # CARGAR PORTATIL
    cargar_y_mostrar_imagen(pantalla, 'img/portatil_game.png', VENTANA, (0, 0))
    cargar_y_mostrar_imagen(pantalla,'img/messi_concentrado.png',(73,124),(570,580))
    return retorno
