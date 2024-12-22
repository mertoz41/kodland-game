from hero import Hero
from enemy import Enemy
import random
import pgzrun

hero = Hero(100, 300)
enemies = [
    Enemy(random.randint(100, 500), random.randint(100, 300), x_boundary=(100, 500), y_boundary=(100, 500)),
    Enemy(random.randint(400, 600), random.randint(100, 300), x_boundary=(200, 600), y_boundary=(100, 400)),
    Enemy(random.randint(200, 300), random.randint(100, 300), x_boundary=(200, 600), y_boundary=(100, 400))

]

menu_active = True
background_music_playing = True
background_music_text = "Background music: ON"
sounds.background_music.play()
sounds.background_music.set_volume(0.1)

music_button_rect = Rect((100, 300), (300, 50)) 
start_button_rect = Rect((100, 400), (200, 50))

exit_button_pos = (800 - 150, 600 - 80)
exit_button_size = (120, 50)
exit_button_color = "red"
exit_button_text = "Exit"
def update():
    hero.move(keyboard.left, keyboard.right, keyboard.up, keyboard.down)
    hero.update()

    for enemy in enemies:
        enemy.move()
        enemy.update()
        if hero.idle1.colliderect(enemy.walk1) or hero.idle1.colliderect(enemy.walk2):
            hero.take_damage()

def draw():
    if menu_active:
        draw_menu()
    else:
        draw_game()

def draw_menu():
    screen.clear()
    screen.fill("black")
    screen.draw.text("Welcome to Run from Zombies!", (100, 100), fontsize=50, color="white")
    screen.draw.text("Contact with zombies will temporarily freeze you so stay away!", (100, 150), fontsize=30, color="white")
    screen.draw.filled_rect(music_button_rect, "blue")  
    screen.draw.text(background_music_text, center=music_button_rect.center, fontsize=30, color="white")
    screen.draw.text("Start game", center=start_button_rect.center, fontsize=30, color="white")
    screen.draw.filled_rect(Rect(exit_button_pos, exit_button_size), exit_button_color)
    screen.draw.text(
        exit_button_text, 
        center=(exit_button_pos[0] + exit_button_size[0] // 2, exit_button_pos[1] + exit_button_size[1] // 2),
        color="white", 
        fontsize=24
    )
def draw_game():
    screen.clear()
    hero.draw()
    for enemy in enemies:
        enemy.draw()
    
def on_mouse_down(pos):
    global menu_active, background_music_playing, background_music_text

    # handle background music
    if menu_active and music_button_rect.collidepoint(pos):
        background_music_playing = not background_music_playing
        if background_music_playing:
            sounds.background_music.play()  # Resume music
            background_music_text = "Background music: ON"
        else:
            sounds.background_music.stop()
            background_music_text = "Background music: OFF"

    # handle menu
    if menu_active and start_button_rect.collidepoint(pos):
        menu_active = False 


    exit_button_rect = Rect(exit_button_pos, exit_button_size)
    if exit_button_rect.collidepoint(pos):
        quit()


pgzrun.go()
