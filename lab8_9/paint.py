import pygame
import random

# Цвета
white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# --- Рисование линий между точками ---
def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# --- Все фигуры ---
def drawRectangle(screen, pos, w, h, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x, y, w, h), 3)

def drawCircle(screen, pos, color, radius):
    x, y = pos
    pygame.draw.circle(screen, color, (x, y), radius, 3)

def drawSquare(screen, pos, color, size):
    x, y = pos
    pygame.draw.rect(screen, color, (x, y, size, size), 3)

def drawRightTriangle(screen, pos, color, size):
    x, y = pos
    pygame.draw.polygon(screen, color, [(x, y), (x + size, y), (x, y + size)], 3)

def drawEquilateralTriangle(screen, pos, color, size):
    x, y = pos
    height = size * (3 ** 0.5) / 2
    pygame.draw.polygon(screen, color, [(x, y), (x + size, y), (x + size / 2, y - height)], 3)

def drawRhombus(screen, pos, color, size):
    x, y = pos
    w, h = size, size * 1.2
    points = [
        (x, y - h // 2),
        (x + w // 2, y),
        (x, y + h // 2),
        (x - w // 2, y)
    ]
    pygame.draw.polygon(screen, color, points, 3)

# --- Главная функция ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint Pro 🎨")
    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))
    radius = 10
    color = white
    figure_size = 100
    last_pos = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            # --- Изменение цвета ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = red
                elif event.key == pygame.K_g:
                    color = green
                elif event.key == pygame.K_b:
                    color = blue
                elif event.key == pygame.K_y:
                    color = yellow
                elif event.key == pygame.K_BACKSPACE:
                    color = eraser
                elif event.key == pygame.K_x:
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # --- Изменение размера ---
                elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                    figure_size = min(300, figure_size + 10)
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    figure_size = max(20, figure_size - 10)

                # --- Фигуры ---
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), figure_size * 2, figure_size, color)
                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), color, figure_size)
                elif event.key == pygame.K_q:
                    drawSquare(screen, pygame.mouse.get_pos(), color, figure_size)
                elif event.key == pygame.K_t:
                    drawRightTriangle(screen, pygame.mouse.get_pos(), color, figure_size)
                elif event.key == pygame.K_e:
                    drawEquilateralTriangle(screen, pygame.mouse.get_pos(), color, figure_size)
                elif event.key == pygame.K_d:
                    drawRhombus(screen, pygame.mouse.get_pos(), color, figure_size)

            # --- Свободное рисование мышью ---
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEMOTION and event.buttons[0] and last_pos:
                drawLineBetween(screen, last_pos, pygame.mouse.get_pos(), radius, color)
                last_pos = pygame.mouse.get_pos()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# --- Запуск ---
main()