import pygame

def graj_muzyke(sciezka, zapetlenie=True, glosnosc=0.5):
    pygame.mixer.music.load(sciezka)
    pygame.mixer.music.set_volume(glosnosc)
    pygame.mixer.music.play(-1 if zapetlenie else 0)

def zatrzymaj_muzyke():
    pygame.mixer.music.stop()

def dzwiek_zjadania():
    dzwiek = pygame.mixer.Sound("assets/zjadanie.wav")
    dzwiek.set_volume(1)  
    dzwiek.play()
