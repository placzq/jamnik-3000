import pygame
from plansza import ROZMIAR_KRATKI, WIDTH, HEIGHT
from przycisk import Przycisk  
from muzyka import graj_muzyke, zatrzymaj_muzyke

class Gracz:
    def __init__(self):
        self.cialo = [(5, 5), (4, 5)]  # Głowa i pupa na starcie
        self.kierunek = (1, 0)
        self.rosnij = False
        graj_muzyke("assets/muzyka_gra.mp3")
        self.glowy = {
            "prawo": pygame.image.load("assets/jamnik_prawo.png").convert_alpha(),
            "lewo": pygame.image.load("assets/jamnik_lewo.png").convert_alpha(),
            "gora": pygame.image.load("assets/jamnik_gora.png").convert_alpha(),
            "dol": pygame.image.load("assets/jamnik_dol.png").convert_alpha()
        }

        self.tulow_poziom = pygame.image.load("assets/jamnik_tulow_poziom.png").convert_alpha()
        self.tulow_pion = pygame.image.load("assets/jamnik_tulow_pion.png").convert_alpha()

        self.tulow_zakrety = {
            ((1, 0), (0, -1)): pygame.image.load("assets/zakret_prawo_gora.png").convert_alpha(),
            ((0, -1), (1, 0)): pygame.image.load("assets/zakret_prawo_gora.png").convert_alpha(),
            ((1, 0), (0, 1)): pygame.image.load("assets/zakret_prawo_dol.png").convert_alpha(),
            ((0, 1), (1, 0)): pygame.image.load("assets/zakret_prawo_dol.png").convert_alpha(),
            ((-1, 0), (0, -1)): pygame.image.load("assets/zakret_lewo_gora.png").convert_alpha(),
            ((0, -1), (-1, 0)): pygame.image.load("assets/zakret_lewo_gora.png").convert_alpha(),
            ((-1, 0), (0, 1)): pygame.image.load("assets/zakret_lewo_dol.png").convert_alpha(),
            ((0, 1), (-1, 0)): pygame.image.load("assets/zakret_lewo_dol.png").convert_alpha()
        }

        self.dupy = {
            "prawo": pygame.image.load("assets/dupa_prawo.png").convert_alpha(),
            "lewo": pygame.image.load("assets/dupa_lewo.png").convert_alpha(),
            "gora": pygame.image.load("assets/dupa_gora.png").convert_alpha(),
            "dol": pygame.image.load("assets/dupa_dol.png").convert_alpha()
        }

    def kierunek_glowy(self):
        if self.kierunek == (1, 0):
            return "prawo"
        elif self.kierunek == (-1, 0):
            return "lewo"
        elif self.kierunek == (0, -1):
            return "gora"
        elif self.kierunek == (0, 1):
            return "dol"

    def obsluz_klawisze(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key in [pygame.K_UP, pygame.K_w]) and self.kierunek != (0, 1):
                self.kierunek = (0, -1)
            elif (event.key in [pygame.K_DOWN, pygame.K_s]) and self.kierunek != (0, -1):
                self.kierunek = (0, 1)
            elif (event.key in [pygame.K_LEFT, pygame.K_a]) and self.kierunek != (1, 0):
                self.kierunek = (-1, 0)
            elif (event.key in [pygame.K_RIGHT, pygame.K_d]) and self.kierunek != (-1, 0):
                self.kierunek = (1, 0)

    def rusz_sie(self):
        glowa = self.cialo[0]
        nowa_glowa = (glowa[0] + self.kierunek[0], glowa[1] + self.kierunek[1])

        if (nowa_glowa[0] < 0 or nowa_glowa[0] >= WIDTH // ROZMIAR_KRATKI or
            nowa_glowa[1] < 0 or nowa_glowa[1] >= HEIGHT // ROZMIAR_KRATKI or
            nowa_glowa in self.cialo):
            return False

        self.cialo.insert(0, nowa_glowa)

        if not self.rosnij:
            self.cialo.pop()
        else:
            self.rosnij = False

        return True

    def sprawdz_zjedzenie(self, owoc):
        if self.cialo[0] == owoc.pozycja:
            self.rosnij = True
            return True
        return False

    def rysuj(self, ekran):
        # ---------------------------------------------Głowa---------------------------------------------
        glowa_x = self.cialo[0][0] * ROZMIAR_KRATKI
        glowa_y = self.cialo[0][1] * ROZMIAR_KRATKI
        ekran.blit(self.glowy[self.kierunek_glowy()], (glowa_x, glowa_y))

        # ---------------------------------------------Tułów---------------------------------------------
        for i in range(1, len(self.cialo) - 1):
            segment = self.cialo[i]
            poprzedni = self.cialo[i - 1]
            nastepny = self.cialo[i + 1]

            kierunek1 = (segment[0] - poprzedni[0], segment[1] - poprzedni[1])
            kierunek2 = (segment[0] - nastepny[0], segment[1] - nastepny[1])

            obraz = None
            for klucz, sprite in self.tulow_zakrety.items():
                if (kierunek1, kierunek2) == klucz or (kierunek2, kierunek1) == klucz:
                    obraz = sprite
                    break

            if obraz is None:
                if kierunek1[0] == 0 and kierunek2[0] == 0:
                    obraz = self.tulow_pion
                else:
                    obraz = self.tulow_poziom

            x = segment[0] * ROZMIAR_KRATKI
            y = segment[1] * ROZMIAR_KRATKI
            ekran.blit(obraz, (x, y))

        # ---------------------------------------------Dupa jamnika---------------------------------------------
        if len(self.cialo) > 1:
            ogon = self.cialo[-1]
            przedostatni = self.cialo[-2]
            kierunek_ogona = (ogon[0] - przedostatni[0], ogon[1] - przedostatni[1])

            x = ogon[0] * ROZMIAR_KRATKI
            y = ogon[1] * ROZMIAR_KRATKI

            if kierunek_ogona == (1, 0):
                ekran.blit(self.dupy["prawo"], (x, y))
            elif kierunek_ogona == (-1, 0):
                ekran.blit(self.dupy["lewo"], (x, y))
            elif kierunek_ogona == (0, -1):
                ekran.blit(self.dupy["gora"], (x, y))
            elif kierunek_ogona == (0, 1):
                ekran.blit(self.dupy["dol"], (x, y))



#---------------------------------------------MENU STARTOWE---------------------------------------------
def ekran_startowy(ekran):
    zegar = pygame.time.Clock()
    graj_muzyke("assets/muzyka_menu.mp3")
    tlo = pygame.image.load("assets/tlo_gra2.png").convert()
    pixel_font = pygame.font.Font("assets/pixeloid.ttf", 45)

    przyciski = [
        Przycisk("Nowa gra", WIDTH // 2 - 150, HEIGHT // 2 -25, 300, 70,
                 (203, 136, 96), (255, 166, 159), "nowa", font=pixel_font),
        Przycisk("Wyjdź", WIDTH // 2 - 150, HEIGHT // 2 +88, 300, 70,
                 (203, 136, 96), (255, 166, 159), "wyjdz", font=pixel_font)
    ]

    while True:
        ekran.blit(tlo, (0, 0))

        for przycisk in przyciski:
            przycisk.rysuj(ekran)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for przycisk in przyciski:
                    if przycisk.rect.collidepoint(event.pos):
                        if przycisk.akcja == "nowa":
                            return "nowa"
                        elif przycisk.akcja == "wyjdz":
                            pygame.quit()
                            exit()

        pygame.display.flip()
        zegar.tick(60)
#---------------------------------------------EKRAN PRZEGRANEJ---------------------------------------------

import pygame
from plansza import WIDTH, HEIGHT

def ekran_przegranej(wynik, ekran):
    zegar = pygame.time.Clock()
    graj_muzyke("assets/muzyka_koniec.mp3")

    tlo = pygame.image.load("assets/tlo_gra3.png").convert()
    pixel_font = pygame.font.Font("assets/pixeloid.ttf", 32)
    pixel_font_big = pygame.font.Font("assets/pixeloid.ttf", 65)


    # Tytuł: przegrana
    przegrana_napis = pixel_font_big.render("Koniec gry", True, (250, 100, 125))
    wynik_napis = pixel_font_big.render(f"Twój wynik: {wynik}", True, (122, 74, 65))

    # Przyciski
    przyciski = [
        Przycisk("Zagraj ponownie", WIDTH // 2 - 178, HEIGHT // 2 , 370, 70,
                  (203, 136, 96), (255, 166, 159), "nowa", font=pixel_font),
        Przycisk("Wyjdź",  WIDTH // 2 - 150, HEIGHT // 2 +88, 300, 70,
                 (203, 136, 96), (255, 166, 159), "wyjdz", font=pixel_font)
    ]

    while True:
        ekran.blit(tlo, (0, 0))
        ekran.blit(przegrana_napis, (WIDTH // 2 - przegrana_napis.get_width() // 2, HEIGHT // 20))
        ekran.blit(wynik_napis, (WIDTH // 2 - wynik_napis.get_width() // 2, HEIGHT // 4 + 10))

        for przycisk in przyciski:
            akcja = przycisk.rysuj(ekran)
            if akcja == "nowa":
                return "nowa"
            elif akcja == "wyjdz":
                pygame.quit()
                exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        zegar.tick(60)
