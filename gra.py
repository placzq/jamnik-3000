import pygame
import sys
from gracz import Gracz, ekran_przegranej  # Dodane
from owoc import Owoc
from plansza import WIDTH, HEIGHT, ROZMIAR_KRATKI
from muzyka import graj_muzyke, zatrzymaj_muzyke
from muzyka import dzwiek_zjadania

def uruchom_gre():
    pygame.init()
    ekran = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jamnik 3000")
    zegar = pygame.time.Clock()

    

    tlo = pygame.image.load("assets/tlo_gra.png").convert()
    font = pygame.font.Font("assets/pixeloid.ttf", 45)

    gracz = Gracz()
    owoc = Owoc()
    punkty = 0
    stan_gry = "gra"

    while True:
        if stan_gry == "gra":
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                gracz.obsluz_klawisze(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stan_gry = "pauza"

            if not gracz.rusz_sie():
                stan_gry = "koniec"

            if gracz.sprawdz_zjedzenie(owoc):
                dzwiek_zjadania()
                owoc.generuj_nowy(gracz)
                punkty += 1

            ekran.blit(tlo, (0, 0))
            gracz.rysuj(ekran)
            owoc.rysuj(ekran)

            tekst = font.render(f"Punkty: {punkty}", True, (122, 74, 65))
            pauza_tekst = font.render(f"Pauza = Esc" , True, (122, 74, 65))
            ekran.blit(tekst, (10, 10))
            ekran.blit(pauza_tekst, (WIDTH - pauza_tekst.get_width() - 10, 10))

            pygame.display.flip()
            zegar.tick(10)

        elif stan_gry == "koniec":
            wynik = len(gracz.cialo) - 2
            rezultat = ekran_przegranej(wynik, ekran) 
            if rezultat == "nowa":
                gracz = Gracz()
                owoc = Owoc()
                punkty = 0
                stan_gry = "gra"

        elif stan_gry == "pauza":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC wraca do gry
                        stan_gry = "gra"

            # Rysuj tło i komunikat o pauzie
            ekran.blit(pygame.image.load("assets/tlo_gra.png").convert(), (0, 0))

            font = pygame.font.Font("assets/pixeloid.ttf", 48)
            tekst = font.render("PAUZA", True, (122, 74, 65))
            ekran.blit(tekst, (WIDTH // 2 - tekst.get_width() // 2, HEIGHT // 2 - 50))

            mniejszy = pygame.font.Font("assets/pixeloid.ttf", 24)
            podtekst = mniejszy.render("Wciśnij ESC, aby wrócić do gry", True, (122, 74, 65))
            ekran.blit(podtekst, (WIDTH // 2 - podtekst.get_width() // 2, HEIGHT // 2 + 10))

            pygame.display.flip()
            zegar.tick(10)

