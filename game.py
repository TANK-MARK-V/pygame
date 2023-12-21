import pygame
import class_player
import class_frame
import class_introduce
import class_button
import class_pause
import class_room
import const

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    FPS = const.FPS
    running = True
    screen = pygame.display.set_mode(const.size)

    room = class_room.Room(screen)
    pause = class_pause.Pause(screen, const.pause_size)
    frame = class_frame.Frames()
    inro = class_introduce.Introduce()
    buttons = class_button.Buttons(screen)
    player = class_player.Player(const.load_image("герой.png", -1), 1, 1, 0, const.barotraum)
    const.player_group.add(player)

    while running:
        player.frem = frame.count
        for event in pygame.event.get():
            if not buttons.start:
                running = buttons.menu(screen, event)  # Открытие меню
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:   # Нажата мышка
                if buttons.pause:
                    if pause.check_do(pygame.mouse.get_pos(), const.pause_size):  # Проверка на нажатие паузы c мышки
                        buttons = class_button.Buttons(screen, pause=True)

            if event.type == pygame.KEYDOWN:  # Нажата кнопка
                if event.key == pygame.K_ESCAPE and buttons.start:  # Проверка на нажатие паузы через "esc"
                    buttons = class_button.Buttons(screen, pause=True)

                if inro.question:  # Проверка на ответ игрока
                    if event.key == pygame.K_y:
                        inro.ready = True
                        inro.question = False
                        player.rect.x = const.width // 2 - const.sprites // 2
                        player.rect.y = const.floor[0][1] - const.sprites
                    if event.key == pygame.K_n:
                        running = False

                if inro.ready:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not player.can_fall:  # Игрок может прыгать только на земле
                        player.jump = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.right = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.left = True
            if event.type == pygame.KEYUP:  # Кнопку отпустили
                if inro.ready:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.right = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.left = False

        if buttons.start:  # Игрок нажал "Играть"
            buttons.pause = True
            if not inro.ready:  # Проигрывание вступительного ролика
                inro.show(screen, player)
            else:  # Основная часть игры
                frame.check(player, buttons)
                room.drawing()
        if buttons.start:  # Игрок не в меню паузы
            pause.draw_pause()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
