from settings import *
from head import Head
from segment import Segment
from food import Food

class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Snake")
        self.running = True
        
        # time
        self.time_now = pygame.time.get_ticks()
        self.time_then = self.time_now
        self.time_interval = 100

        # groups
        self.all_sprites = pygame.sprite.Group()
        
        self.snake_setup()

        # food
        self.food = Food(self.head.rect, self.all_sprites)
        
    def board_setup(self):
        
        for i in range(cell_number+1):
            pygame.draw.line(self.display_surface, "gray", (0,i*cell_size), (resolution[1], i*cell_size))
            pygame.draw.line(self.display_surface, "gray", (i*cell_size,0), (i*cell_size, resolution[1]))
            
    def snake_setup(self):
        self.head = Head(self.time_then, self.time_interval, self.all_sprites)
        self.start_length = 4
        self.segment_list = [self.head]

        for i in range(self.start_length):
            self.segment_list.append(Segment(self.all_sprites))
    
    def run(self):
        while self.running:
            self.time_now = pygame.time.get_ticks()
            self.display_surface.fill("black")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.board_setup()
            self.all_sprites.draw(self.display_surface)

            # snake moves
            if self.time_now - self.time_then >= self.time_interval:
                self.time_then = self.time_now

                # segments move
                for i in range(len(self.segment_list)-1, 0, -1):
                    self.segment_list[i].move(self.segment_list[i-1].rect.center)

                self.head.move() 

                if self.head.does_collide(self.segment_list):
                    self.running = False
                    #print("game over")
                
            # snake eats food
            if self.food.rect.colliderect(self.head.rect):
                self.food.rect.center = self.food.randomize_position()
                self.segment_list.append(Segment(self.all_sprites))

            self.all_sprites.update()
            
            pygame.display.update()
            
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()