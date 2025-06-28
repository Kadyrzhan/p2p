import pygame
import os
from mutagen.mp3 import MP3

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Музыкальный плеер 🎵")

ASSET_FOLDER = "C:\\Users\\Asus\\job\\lab7"
songs = [f for f in os.listdir(ASSET_FOLDER) if f.endswith(".mp3")]

if not songs:
    raise FileNotFoundError("Нет музыкальных файлов в папке.")

current_song = 0
is_playing = True

pygame.mixer.init()

def play_song(start_time=0):
    pygame.mixer.music.load(ASSET_FOLDER + "\\" + songs[current_song])
    pygame.mixer.music.play(start=start_time)
    global track_length
    track_length = MP3(ASSET_FOLDER + "\\" + songs[current_song]).info.length

play_song()

# Загрузка фона
IMAGE_PATH = "C:\\Users\\Asus\\job\\lab7\\rose.jpg"
if os.path.exists(IMAGE_PATH):
    background = pygame.image.load(IMAGE_PATH)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    print(f"Файл {IMAGE_PATH} не найден!")
    background = None

# Загрузка кнопок
button_images = {
    "play": pygame.image.load("C:\\Users\\Asus\\job\\lab7\\play.png"),
    "pause": pygame.image.load("C:\\Users\\Asus\\job\\lab7\\pause.png"),
    "next": pygame.image.load("C:\\Users\\Asus\\job\\lab7\\next.png"),
    "prev": pygame.image.load("C:\\Users\\Asus\\job\\lab7\\back.png"),
}

for key in button_images:
    button_images[key] = pygame.transform.scale(button_images[key], (80, 80))

button_positions = {
    "prev": (100, 350),
    "play_pause": (210, 350),
    "next": (320, 350),
}

progress_bar_x = 50
progress_bar_y = 300
progress_bar_width = 400
progress_bar_height = 10
progress_circle_radius = 8
is_dragging = False

font = pygame.font.Font(None, 26)

running = True
while running:
    screen.fill((30, 30, 30))

    if background:
        screen.blit(background, (0, 0))

    screen.blit(button_images["prev"], button_positions["prev"])
    screen.blit(button_images["next"], button_positions["next"])
    screen.blit(button_images["pause"] if is_playing else button_images["play"], button_positions["play_pause"])

    current_time = pygame.mixer.music.get_pos() / 1000

    if not is_dragging:
        progress = min(current_time / track_length, 1.0)
    else:
        progress = (drag_x - progress_bar_x) / progress_bar_width

    pygame.draw.rect(screen, (180, 180, 180), (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height))
    circle_x = progress_bar_x + int(progress * progress_bar_width)
    pygame.draw.circle(screen, (255, 255, 255), (circle_x, progress_bar_y + progress_bar_height // 2), progress_circle_radius)

    time_text = f"{int(current_time // 60)}:{int(current_time % 60):02d} / {int(track_length // 60)}:{int(track_length % 60):02d}"
    text_surface = font.render(time_text, True, (255, 255, 255))
    screen.blit(text_surface, (WIDTH // 2 - 40, progress_bar_y - 25))

    song_name = songs[current_song].replace(".mp3", "")
    song_text_surface = font.render(song_name, True, (255, 255, 255))
    screen.blit(song_text_surface, (WIDTH // 2 - song_text_surface.get_width() // 2, 450))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                play_song()
                is_playing = True
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                play_song()
                is_playing = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for key, pos in button_positions.items():
                btn_x, btn_y = pos
                if btn_x <= x <= btn_x + 80 and btn_y <= y <= btn_y + 80:
                    if key == "play_pause":
                        if is_playing:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        is_playing = not is_playing
                    elif key == "next":
                        current_song = (current_song + 1) % len(songs)
                        play_song()
                        is_playing = True
                    elif key == "prev":
                        current_song = (current_song - 1) % len(songs)
                        play_song()
                        is_playing = True

            if progress_bar_x <= x <= progress_bar_x + progress_bar_width and progress_bar_y - 10 <= y <= progress_bar_y + progress_bar_height + 10:
                is_dragging = True
                drag_x = x

        elif event.type == pygame.MOUSEBUTTONUP:
            if is_dragging:
                new_time = ((drag_x - progress_bar_x) / progress_bar_width) * track_length
                pygame.mixer.music.play(start=new_time)
            is_dragging = False

    pygame.display.flip()

pygame.quit()
