from pgzero.actor import Actor  # Import Actor from pgzero.actor
from pgzero.loaders import sounds

class Hero:

    def __init__(self, x, y, speed=5):
        self.pos = (x,y)
        self.speed = speed

        # hero sprites
        self.idle1 = Actor('hero/idle1', self.pos)
        self.idle2 = Actor('hero/idle2', self.pos)
        self.walk1 = Actor('hero/walk1', self.pos)
        self.walk2 = Actor('hero/walk2', self.pos)
        self.up1 = Actor('hero/climb1', self.pos)
        self.up2 = Actor('hero/climb2', self.pos)
        self.hurt = Actor('hero/hurt', self.pos)

        self.current_pose = 'idle'

        # to cycle between sprites
        self.walk_cycle = 0
        self.up_cycle = 0    
        self.idle_cycle = 0

        self.animation_speed = 10  
        self.frame_count = 0 
        self.is_hit = False
        self.hit_timer = 0

    def move(self, left, right, up, down):

        if not self.is_hit:
            if left:
                self.pos = (self.pos[0] - self.speed, self.pos[1])
                self.current_pose = 'walking'
            elif right:
                self.pos = (self.pos[0] + self.speed, self.pos[1])
                self.current_pose = 'walking'
            elif up:
                self.pos = (self.pos[0], self.pos[1] - self.speed)
                self.current_pose = 'up'
            elif down:
                self.pos = (self.pos[0], self.pos[1] + self.speed)
                self.current_pose = 'walking'
            else:
                self.current_pose = 'idle'  # Default to idle when not moving

    def update(self):
        # Cycle through animations
        if self.current_pose == 'walking':
            self.frame_count += 1
            if self.frame_count % self.animation_speed == 0:  # Change every 10 frames for smooth transition
                if self.walk_cycle % 2 == 0:
                    self.walk_cycle = 1
                else:
                    self.walk_cycle = 0

        elif self.current_pose == 'up':
            self.frame_count += 1
            if self.frame_count % self.animation_speed == 0:
                if self.up_cycle == 0:
                    self.up_cycle = 1
                else:
                    self.up_cycle = 0

        elif self.current_pose == 'idle':
            self.frame_count += 1
            if self.frame_count % self.animation_speed == 0:
                if self.idle_cycle == 0:
                    self.idle_cycle = 1
                else:
                    self.idle_cycle = 0
                    
        else:
            self.frame_count = 0
            self.walk_cycle = 0
            self.up_cycle = 0

        if self.is_hit:
            self.hit_timer +=1
            if self.hit_timer > 120:
                self.is_hit = False 
                self.hit_timer = 0

    def draw(self):
        # draw hero based on current pose
        self.idle1.pos = self.pos
        self.idle2.pos = self.pos
        self.walk1.pos = self.pos
        self.walk2.pos = self.pos
        self.up1.pos = self.pos
        self.up2.pos = self.pos
        self.hurt.pos = self.pos
        if self.is_hit:
            self.hurt.draw()
        elif self.current_pose == 'idle':
            if self.idle_cycle== 0:
                self.idle1.pos = self.pos
                self.idle1.draw()
            elif self.idle_cycle == 1:
                self.idle2.pos = self.pos
                self.idle2.draw()
          
        elif self.current_pose == 'walking':
            if self.walk_cycle == 0:
                self.walk1.pos = self.pos
                self.walk1.draw()
            elif self.walk_cycle == 1:
                self.walk2.pos = self.pos
                self.walk2.draw()
        elif self.current_pose == 'up':
            if self.up_cycle == 0:
                self.up1.draw()
            elif self.up_cycle == 1:
                self.up2.draw()

    def take_damage(self):
        self.is_hit = True
        self.current_pose = "idle"