#
# JUEGO PROGRAMACION 
#-----------------------

 
# ---------------------------
# Importacion de los módulos
# ---------------------------
 
import pygame
from pygame.locals import *
import os
import sys
import random 
# -----------
# Constantes
# -----------
NEGRO = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "game"

#---------------------------
# Clases y funiones
#---------------------------




def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print ("Error, no se puede cargar la imagen: ", ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image


class Hamburger(pygame.sprite.Sprite):
    "La hamburger y su comportamiento en la pantalla"
 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("hamb.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10,600)    
        self.rect.y = random.randrange(-300, -20) 


     
    def colision(self, objetivo):
        
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-300, -20) 
           
    def update(self):
        """ Llamada para cada fotograma. """
 
        # Desplaza el bloque un píxel hacia abajo.
        if self.rect.y > 500:
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-300, -20) 
            
        else:
            self.rect.y += 5
         
        # Si el bloque estuviera muy abajo, lo restablecemos a la parte superior de la pantalla.
        

class Goldburger (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("goldburger.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(20,620)    
        self.rect.y = random.randrange(-2500,-1900) 
        self.speed = [4,4]
    def colision(self, objetivo):
        
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-2000, -1500) 
           
    def update(self):
        """ Llamada para cada fotograma. """
        # Desplaza el bloque un píxel hacia abajo. s
        if self.rect.left < 50 or self.rect.right > 600:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 200:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1])) 
        if self.rect.y > 500:
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-400,-200)
        self.rect.y += 5

       
class Birra(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("duff.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10,600)    
        self.rect.y = random.randrange(-1200,-700)

    def colision(self, objetivo):
        
        if self.rect.colliderect(objetivo.rect): # con eso mira si choco con el objetivo
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-300, -20) 
    def update(self):
        """ Llamada para cada fotograma. """
        if self.rect.y > 500:
            self.rect.x = random.randrange(10,600)    
            self.rect.y = random.randrange(-1000,-700)
        else:
            self.rect.y += 6
         
    
        
class Protagonista(pygame.sprite.Sprite):
    
    def __init__(self, X):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("homer.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 440
        
    
    def humano(self):
        # Controlar que protagonista no salga de la pantalla
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
     
         
#
#Funcion principal del juego
#






def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Homer vs. Hamburger")
    fondo = load_image("fondo.png", IMG_DIR, alpha=False)
    
    hecho = False
  
# Usado para gestionar cuán rápido se actualiza la pantalla
    clock = pygame.time.Clock()
 
# Esta es la fuente que usaremos para. el textoo que aparecerá en pantalla (tamaño 25)
    fuente = pygame.font.Font(None, 25)
    numero_de_fotogramas = 0
    tasa_fotogramas = 60
    instante_de_partida = 90
 
    # -------- Bucle Principal del Programa -----------
    while not hecho:    
        for evento in pygame.event.get():  # El usuario hizo algo
            if evento.type != pygame.QUIT: # Si el usuario hace click sobre cerrar
                hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
  
    # Limpia la pantalla y establece su color de fondo
    
  
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
     
    # --- El temporizador avanza ---
    # Calculamos los segundos totales
    
 
    # --- El temporizador retrocede ---
    # --- El temporizador avanza ---
    # Calculamos los segundos totales 
        segundos_totales = instante_de_partida - (numero_de_fotogramas // tasa_fotogramas)
        if segundos_totales < 0:
            segundos_totales = 0
     
    # Dividimos por 60 para obtener los minutos totales
        minutos = segundos_totales // 60
     
    # Usamos el módulo (resto) para obtener los segundos
        segundos = segundos_totales % 60
     
    # Usamos el formato de cadenas de texto para formatear los ceros del principio
        texto_de_salida = "Time left: {0:02}:{1:02}".format(minutos, segundos)
             
    # Volcamos en pantalla
        texto = fuente.render(texto_de_salida, True, NEGRO)
     
        screen.blit(texto, [250, 280])
     
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
        numero_de_fotogramas += 1
     
    # Limitamos a 20 fotogramas por segundo
        clock.tick(60)
  
    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    #pygame.display.flip()


    hamb = Hamburger()
    homer = Protagonista(300)
    beer = Birra ()
    gold = Goldburger()
    hamb_lista = pygame.sprite.Group()
    beer_lista = pygame.sprite.Group()
    gold_lista = pygame.sprite.Group ()
# Esta es una lista de cada sprite, así como de los bloques y del protagonista.rojo
    listade_todoslos_sprites= pygame.sprite.Group()

    for i in range(50):
    # Esto representa una hamb
        hamb = Hamburger ()
        hamb2 = Hamburger()
        hamb3 = Hamburger()
        hamb4 = Hamburger()
        hamb5 = Hamburger()
        beer = Birra ()
        gold = Goldburger ()
        gold2 = Goldburger()
    # Añade hamb a la lista de objetos
        hamb_lista.add(hamb)
        hamb_lista.add(hamb2)
        hamb_lista.add(hamb3)
        hamb_lista.add(hamb4)
        hamb_lista.add(hamb5)
        gold_lista.add(gold)
        gold_lista.add(gold2)
        beer_lista.add(beer)
        listade_todoslos_sprites.add(hamb)
        listade_todoslos_sprites.add(hamb2)
        listade_todoslos_sprites.add(hamb3)
        listade_todoslos_sprites.add(hamb4)
        listade_todoslos_sprites.add(hamb5)
        listade_todoslos_sprites.add(homer)
        listade_todoslos_sprites.add(beer)
        listade_todoslos_sprites.add(gold)
        listade_todoslos_sprites.add(gold2)
      
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 50)  # Activa repeticion de teclas
    pygame.mouse.set_visible(False)
    puntuacion = 0
    while True:
        clock.tick(30)
        homer.humano()
        hamb.colision(homer)
        hamb2.colision(homer)
        hamb3.colision(homer)
        hamb4.colision(homer)
        hamb5.colision(homer)
        
        # Actualizamos los obejos en pantalla
        hamb.update()
        hamb2.update()
        hamb3.update()
        hamb4.update()
        hamb5.update()

        beer.colision(homer)
        beer.update()
        gold.colision(homer)
        gold2.colision(homer)
        gold.update()
        gold2.update()       
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    homer.image = load_image("homer.png", IMG_DIR, alpha=True)
                    homer.rect.centerx -= 20
                elif event.key == K_RIGHT:
                    homer.image = load_image("homer right.png", IMG_DIR, alpha=True)
                    homer.rect.centerx += 20
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == K_UP:
                    homer.rect.centery += 0
                elif event.key == K_DOWN:
                    homer.rect.centery += 0
            
    
        lista_impactos_hamb = pygame.sprite.spritecollide(homer, hamb_lista, False)
        lista_impactos_beer = pygame.sprite.spritecollide(homer,beer_lista, False)
        lista_impactos_gold = pygame.sprite.spritecollide(homer, gold_lista, False) 
        # Comprobamos la lista de colisiones
        
        if pygame.sprite.spritecollide(homer, hamb_lista, False):
            for hamb in lista_impactos_hamb:
                puntuacion += 1
                print( puntuacion )
        if pygame.sprite.spritecollide(homer, beer_lista, False):
            for beer in lista_impactos_beer:
                puntuacion += 10
                print (puntuacion)
        if pygame.sprite.spritecollide(homer, gold_lista, False):
                for gold in lista_impactos_gold:
                    puntuacion += 50
                    print (puntuacion)

        screen.blit(fondo, (0, 0))
        screen.blit(texto, [510, 5])
        screen.blit(hamb.image, hamb.rect)
        screen.blit(homer.image, homer.rect)
        screen.blit(hamb2.image, hamb2.rect)
        screen.blit(hamb3.image, hamb3.rect)
        screen.blit(hamb4.image, hamb4.rect)
        screen.blit(hamb5.image, hamb5.rect)
        screen.blit(beer.image, beer.rect)
        screen.blit(gold.image, gold.rect)
        screen.blit(gold2.image, gold2.rect)
        # Limitamos a 20 fotogramas por segundo

        numero_de_fotogramas += 1
     
        
        pygame.display.flip()



if __name__ == "__main__":
    main()

pygame.quit()
