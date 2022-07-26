import sys
import pygame 

class Cell():
    def __init__(self,top,left,width,height,alive):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.alive = alive
    
    def draw(self,screen):
        if self.alive:
            pygame.draw.rect(
                surface=screen,
                color='white',
                rect = pygame.Rect(self.left,self.top,self.width,self.height)
            )

class Game():
    def __init__(self):
        pygame.init()

        self.set_window()

        self.generation = 0
        self.population = 0

        self.cells = []
        for i in range(self._width/10):
            for j in range(self._height/10):
                cell = Cell(i*10,j*10,10,10,False)
                self.cells.append(cell)
    
    def set_window(self):
        self._width = 600
        self._height = 600

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self._width,self._height))
        pygame.display.set_caption("El juego de la vida")
    
    def run(self):

        quit = False
        life = False

        while quit == False:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE] == True:
                        life = not life  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    self.check_cell(mouse)

                    if life == True:
                        life = False


            if life:
                self.screen.fill('black')
                self.update_cells()
                for cell in self.cells:
                    cell.draw(self.screen)
                    
                    

            self.display_generation()
            self.display_population()    

            self.clock.tick(60)
              
    def close(self):
        pygame.quit()
        sys.exit()

    def display_generation(self):
        generation_text = pygame.font.Font(None,15).render(f'Generation: {self.generation}', True, 'white')
        generation_rect = generation_text.get_rect(topleft=(50,50))

        self.screen.blit(generation_text,generation_rect)
    
    def display_population(self):
        population_text = pygame.font.Font(None,15).render(f'Population: {self.population}', True, 'white')
        population_rect = population_text.get_rect(topleft=(50,60))

        self.screen.blit(population_text,population_rect)

    def check_cell(self):
        pass

    def update_cells(self):
        pass

    
    