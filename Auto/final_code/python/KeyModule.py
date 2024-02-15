import pygame

# Initialisiere Pygame und erstelle ein Fenster
def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))

# Überprüfe, ob eine bestimmte Taste gedrückt wurde
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

# Hauptfunktion, die die Tastatureingaben überwacht
def main():
    if getKey('LEFT'):
        print('Taste Links wurde gedrückt')
    if getKey('RIGHT'):
        print('Taste Rechts wurde gedrückt')

if __name__ == '__main__':
    init()
    while True:
        main()
