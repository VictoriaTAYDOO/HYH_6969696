import os
import sys

import pygame
import requests

a = input().split()
x, y = float(a[0]), float(a[1])
m = float(input())
running = True

while running:
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={m},20&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    # Переключаем экран и ждем закрытия окна.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if m - 5 >= 50:
                    m -= 5
            elif event.key == pygame.K_UP:
                if m + 5 <= 100:
                    m += 5
    pygame.display.flip()
pygame.quit()
os.remove(map_file)
# Удаляем за собой файл с изображением.