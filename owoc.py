import pygame
import random
from plansza import ROZMIAR_KRATKI, WIDTH, HEIGHT

class Owoc:
    def __init__(self):
        self.pozycja = (0, 0)
        self.grafiki = {
            "jablko": pygame.image.load("assets/jablko64grube.png").convert_alpha(),
            "truskawka": pygame.image.load("assets/truskawka64.png").convert_alpha(),
            "banan": pygame.image.load("assets/banan64.png").convert_alpha()
        }

        self.obraz = None
        self.generuj_nowy()

    def generuj_nowy(self, gracz=None):
        max_x = WIDTH // ROZMIAR_KRATKI
        max_y = HEIGHT // ROZMIAR_KRATKI

        while True:
            nowa = (random.randint(0, max_x - 1), random.randint(0, max_y - 1))
            if gracz is None or nowa not in gracz.cialo:
                self.pozycja = nowa
                break

        self.obraz = random.choice(list(self.grafiki.values()))  # Wybór obrazka

    def rysuj(self, ekran):
        ekran.blit(self.obraz, (
            self.pozycja[0] * ROZMIAR_KRATKI,
            self.pozycja[1] * ROZMIAR_KRATKI
        ))
