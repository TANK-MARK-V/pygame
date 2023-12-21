import pygame
import class_player
import class_frame
import class_introduce
import class_button
import class_pause
import const

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    FPS = const.FPS
    running = True
    screen = pygame.display.set_mode(const.size)

    pause = class_pause.Pause(screen, const.pause_size)
    frame = class_frame.Frames()
    inro = class_introduce.Introduce()
    buttons = class_button.Buttons(screen)
    player = class_player.Player(const.load_image("герой.png", -1), 1, 1, 0, const.barotraum)
    const.player_group.add(player)

    while running:
        frame.check(player)
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

                if event.key == pygame.K_y and inro.question:  # Проверка на ответ игрока
                    inro.ready = True
                    inro.question = False
                if event.key == pygame.K_n and inro.question:
                    running = False

        if buttons.start:  # Игрок нажал "Играть"
            buttons.pause = True
            if not inro.ready:  # Проигрывание вступительного ролика
                inro.show(screen, player)
            else:  # Основная часть игры
                pass
        if buttons.start:  # Игрок не в меню паузы
            pause.draw_pause()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
