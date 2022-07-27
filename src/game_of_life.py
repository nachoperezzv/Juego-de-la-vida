import sys
import pygame 
import numpy as np

class Cell():
    def __init__(self,i,j,top,left,width,height,alive):
        self.i = i
        self.j = j

        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.alive = alive

        self.neighbours_alive = 0
    
    def draw(self,screen,running,cells):

        if running:            
            # if self.alive == True:                
            #     if neighbours_alive >= 2 and neighbours_alive <=3:
            #         print('sigue vivo {}'.format(neighbours_alive))
            #         pass
            #     else:
            #         print('muere')
            #         self.alive = False
                
            if self.alive == False and self.neighbours_alive == 3:
                    self.alive = True
                
        
        if self.alive:
            pygame.draw.rect(
                surface=screen,
                color='white',
                rect = pygame.Rect(self.left,self.top,self.width,self.height)
            )
        
        return 1 if self.alive else 0
    
    def check_neighbours(self,cells):
        neighbours_alive = 0
        for i in range(self.i-1,self.i+2):
            for j in range(self.j-1,self.j+2):
                if not (i == self.i and j == self.j):
                    if i>=0 and j>=0 and i<60 and j<60:
                        if cells[i][j].alive:
                            neighbours_alive += 1
                
        if self.alive: print(self.i,self.j,neighbours_alive)
        
        return neighbours_alive


class Game():
    def __init__(self):
        pygame.init()

        self.set_window()

        self.generation = 0
        self.population = 0

        self.set_cells()
    
    def set_cells(self):
        self.cells = []
        self.new_cells = []
        for i in range(int(self._width/10)):
            row = []
            for j in range(int(self._height/10)):
                cell = Cell(i,j,i*10,j*10,10,10,False)
                row.append(cell)
            self.cells.append(row)
            self.new_cells.append(row)

        
    
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
                        self.set_cells()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_cell()
                    if life == True:
                        life = False


            self.screen.fill('black')

            self.population = 0

            
            for j in range(60):
                for i in range(60):
                    self.population += self.cells[i][j].draw(self.screen,life,self.cells)

            # for row in self.cells:
            #     for cell in row:
            #         self.population += cell.draw(self.screen,life,self.cells)
            
            if life: 
                self.generation += 1   
                print('----')   
                    
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
            self.cells[j][i].alive = not self.cells[j][i].alive
        if mbuttons[2]:
            self.cells[j][i].alive = False


if __name__ == '__main__':
    game = Game()
    game.run()
    game.close()
    
    