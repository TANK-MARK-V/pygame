import pygame
import class_player
import const

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    FPS = const.FPS
    running = True
    screen = pygame.display.set_mode(const.size)

    player = class_player.Player(const.load_image("герой.png", -1), 2, 1, 0, const.barotraum)
    const.player_group.add(player)

    buttons, inro, pause, frame, room, attack = const.make_prep(screen)

    const.make_bloks()

    while running:
        player.frem = frame.count
        for event in pygame.event.get():
            if not buttons.start:
                running = buttons.menu(screen, event)  # Открытие меню
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Нажата мышка
                if buttons.pause:
                    if pause.check_do(pygame.mouse.get_pos(), const.pause_size):  # Проверка на нажатие паузы c мышки
                        buttons = const.make_prep(screen, True)

            if event.type == pygame.KEYDOWN:  # Нажата кнопка
                if event.key == pygame.K_ESCAPE and buttons.start:  # Проверка на нажатие паузы через "esc
                    buttons = const.make_prep(screen, True)

                if inro.question:  # Проверка на ответ игрока
                    if event.key == pygame.K_y:
                        running = False
                    if event.key == pygame.K_n:
                        inro.ready = True
                        inro.question = False
                        player.rect.x = const.width // 2 - const.sprites // 2
                        player.rect.y = const.floor[0][1] - const.sprites
                        player.hp = 3
                        player.count = 0
                        player.killed = 0

                if inro.ready:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not player.can_move[1]:
                        # Игрок может прыгать только на земле
                        player.jump = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.right = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.left = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        attack.pressed = True
                        attack.started = frame.count
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
                frame.check(player, buttons, room)
                room.drawing()
                running = frame.draw_hp(screen, player)  # Отрисовка здоровья игрока
                attack.draw(screen, player, frame.count)
        if buttons.start:  # Игрок не в меню паузы
            pause.draw_pause()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
