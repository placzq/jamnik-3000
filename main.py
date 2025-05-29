import pygame
from plansza import WIDTH, HEIGHT
from gracz import ekran_startowy
from gra import uruchom_gre

if __name__ == "__main__":
    pygame.init()
    ekran = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jamnik 3000")

    wynik = ekran_startowy(ekran)
    if wynik == "nowa":
        uruchom_gre()

