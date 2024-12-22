from pgzero.actor import Actor
import random
class Enemy:
    def __init__(self, x, y, speed=3, x_boundary=(100,500),y_boundary=(100,500)):
        self.pos = (x,y)
        self.speed = speed
        self.walk1 = Actor('enemy/walk1',self.pos)
        self.walk2 = Actor('enemy/walk2', self.pos)

        self.up1 = Actor('enemy/climb1', self.pos)
        self.up2 = Actor('enemy/climb2', self.pos)

        self.current_pose = 'walking'
        self.walk_cycle = 0
        self.up_cycle = 0
        self.direction = 1
        self.animation_speed = 10
        self.frame_count = 0
        # movement boundary
        self.x_boundary = x_boundary  
        self.y_boundary = y_boundary  
        
        self.move_counter = 0
        self.move_interval = 120
        self.move_timer = 0
        
    def random_move(self):
        if self.move_counter >= self.move_interval:
            self.move_counter = 0 
            self.current_pose = random.choice(['walking', 'climbing'])
            if self.current_pose == 'walking':
                self.direction = random.choice([1, -1]) 
            if self.current_pose == 'climbing':
                self.climb_speed = random.choice([2, -2])  
        self.move_counter += 1  

    def move(self):
        if self.current_pose == 'walking':
            self.pos = (self.pos[0] + self.speed * self.direction, self.pos[1])
            # reverse movement direction if enemy hits boundar
            if self.pos[0] <= self.x_boundary[0] or self.pos[0] >= self.x_boundary[1]:
                self.direction *= -1 

        elif self.current_pose == 'climbing':
            self.pos = (self.pos[0], self.pos[1] + self.climb_speed)
            if self.pos[1] <= self.y_boundary[0] or self.pos[1] >= self.y_boundary[1]:
                self.climb_speed *= -1  

    def update(self):
        self.random_move()

        if self.current_pose == 'walking':
            self.frame_count += 1
            if self.frame_count % self.animation_speed == 0:
                if self.walk_cycle == 0:
                    self.walk_cycle = 1
                else:
                    self.walk_cycle = 0

        elif self.current_pose == 'climbing':
            self.frame_count += 1
            if self.frame_count % self.animation_speed == 0:
                if self.up_cycle == 0:
                    self.up_cycle = 1
                else:
                    self.up_cycle = 0


    def draw(self):
        self.walk1.pos = self.pos
        self.walk2.pos = self.pos
        self.up1.pos = self.pos
        self.up2.pos = self.pos

        if self.current_pose == 'walking':
            if self.walk_cycle == 0:
                self.walk1.draw()
            elif self.walk_cycle == 1:
                self.walk2.draw()
        elif self.current_pose == 'climbing':
            if self.up_cycle == 0:
                self.up1.draw()
            elif self.up_cycle == 1:
                self.up2.draw()


        