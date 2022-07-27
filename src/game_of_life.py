import sys
import pygame 
import numpy as np

class Game():
    def __init__(self):
        pygame.init()

        self.set_window()
        self.set_cells()

        self.generation = 0
        self.population = 0

    def set_cells(self):
        self._dimx,self._dimy = self._width//10, self._height//10
        
        self.cells = np.zeros((self._dimx,self._dimy))        
        self.new_cells = np.copy(self.cells)
    
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
                    if keys[pygame.K_ESCAPE] ==  True:
                        life = False
                        self.population = 0
                        self.generation = 0
                        self.cells = np.zeros((self._dimx,self._dimy))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_cell()
                    if life == True:
                        life = False


            self.screen.fill('black')
            self.new_cells = np.copy(self.cells)

            for i in range(self._dimx):
                for j in range(self._dimy):
                    neighbours = self.check_neighbours(i,j)

                    if life:
                        if self.cells[i][j] == 0 and neighbours == 3:
                            self.new_cells[i][j] = 1
                        
                        if self.cells[i][j] == 1 and (neighbours < 2 or neighbours > 3):
                            self.new_cells[i][j] = 0

                        if self.new_cells[i][j] == 1:
                            pygame.draw.rect(self.screen,'white',(i*10,j*10,10,10))
                        
                        self.population = int(np.sum(self.new_cells))
                        self.generation += 1
                        
                    else:
                        if self.new_cells[i][j] == 1:
                            pygame.draw.rect(self.screen,[120,120,120],(i*10,j*10,10,10))
                
            
            
            self.cells = np.copy(self.new_cells)

            self.display_generation()
            self.display_population()    

            pygame.display.flip()
            self.clock.tick(20)
              
    def close(self):
        pygame.quit()
        sys.exit()

    def display_generation(self):
        generation_text = pygame.font.Font(None,20).render(f'Generation: {self.generation}', True, 'white')
        generation_rect = generation_text.get_rect(topleft=(20,20))

        self.screen.blit(generation_text,generation_rect)
    
    def display_population(self):
        population_text = pygame.font.Font(None,20).render(f'Population: {self.population}', True, 'white')
        population_rect = population_text.get_rect(topleft=(20,35))

        self.screen.blit(population_text,population_rect)

    def check_cell(self):
        mx,my = pygame.mouse.get_pos()
        mbuttons = pygame.mouse.get_pressed()
        i,j = mx//10,my//10

        if mbuttons[0]:    
            self.cells[i][j] = not self.cells[i][j]
        if mbuttons[2]:
            self.cells[i][j] = False

        self.population = int(np.sum(self.cells))

    def check_neighbours(self,x,y):
        neighbours = 0

        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i>=0 and j>=0 and i<self._dimx and j<self._dimy:
                    if self.cells[i][j] and not (i==x and j==y): 
                        neighbours += 1

        return neighbours

if __name__ == '__main__':
    game = Game()
    game.run()
    game.close()
    
    