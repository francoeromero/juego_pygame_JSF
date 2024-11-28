import pygame
pygame.init()


TAMANYO_BOTON = (250,250)
CUADRO_TEXTO = (250,250)
TAMANYO_BOTON_VOLUMEN = (60,60)
TAMANYO_BOTON_VOLVER = (100,40)
ANCHO = 1200
ALTO = 800
VENTANA = (ANCHO,ALTO)
FPS = 30

pantalla = pygame.display.set_mode((VENTANA))

TAMAÑO_PREGUNTA = (400,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

# Constantes de colores
COLOR_BLANCO = (255, 255, 255)  # Blanco
COLOR_NEGRO = (0, 0, 0)         # Negro
COLOR_VERDE = (0, 255, 0)       # Verde
COLOR_AZUL = (0, 0, 255)        # Azul
TRANSPARENTE = (0,0,0,0)

CLICK_SONIDO = pygame.mixer.Sound("sonidos/sonido_navegacion.mp3")
CLICK_PELOTAZO = pygame.mixer.Sound("sonidos/sonido_boton.mp3")
CLICK_CORRECTO = pygame.mixer.Sound("sonidos/sonido_correcto.mp3")
CLICK_INCORRECTO = pygame.mixer.Sound("sonidos/sonido_incorrecto.mp3")
CLICK_GAME_OVER = pygame.mixer.Sound("sonidos/anda_para_alla_bobo.mp3")
CLICK_GANASTE_VIDA = pygame.mixer.Sound("sonidos/goool.mp3")

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

BOTON_CARGAR_NOMBRE = 0
BOTON_SALIR_CANCELAR = 1

DELAY_BOTON = 6
VELOCIDAD_FONDO = 1
OPCION_1 = 0
OPCION_2 = 1
OPCION_3 = 2
OPCION_4 = 3
CANTIDAD_PREGUNTAS_POR_NIVEL = 10
CANTIDAD_NIVELES = 6