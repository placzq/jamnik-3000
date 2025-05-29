import pygame

class Przycisk:
    def __init__(self, tekst, x, y, szer, wys, kolor, kolor_hover, akcja, font):
        self.tekst = tekst
        self.rect = pygame.Rect(x, y, szer, wys)
        self.kolor = kolor
        self.kolor_hover = kolor_hover
        self.akcja = akcja
        self.font = font


    def rysuj(self, ekran):
        mysz = pygame.mouse.get_pos()
        klik = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mysz):
            pygame.draw.rect(ekran, self.kolor_hover, self.rect, border_radius=40)
            pygame.draw.rect(ekran, (122, 74, 65), self.rect, 5, border_radius=40)
            if klik[0]:  # ← Jeśli kliknięto LPM
                return self.akcja
        else:
            pygame.draw.rect(ekran, self.kolor, self.rect, border_radius=40)
            pygame.draw.rect(ekran, (122, 74, 65), self.rect, 5, border_radius=40)

        tekst_surf = self.font.render(self.tekst, True, (249, 198, 195)) # KOLOR TEKSTU NA PRZYCISKACH
        tekst_rect = tekst_surf.get_rect(center=self.rect.center)
        ekran.blit(tekst_surf, tekst_rect)
        return None
