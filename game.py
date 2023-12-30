import pygame
import class_player
import class_frame
import class_introduce
import class_button
import class_pause
import class_room
import class_borders
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
    player = class_player.Player(const.load_image("герой.png", -1), 2, 1, 0, const.barotraum)
    const.player_group.add(player)

    for blok in const.bloks:  # Границы блоков
        x1, y1, x2, y2 = blok
        const.up.add(class_borders.Border(x1 + 1, y1, x2 - 1, y1 + 1))
        const.down.add(class_borders.Border(x1 + 1, y2 - 1, x2 - 1, y2))
        const.left.add(class_borders.Border(x1, y1 + 1, x1 + 1, y2 - 1))
        const.right.add(class_borders.Border(x2 - 1, y1 + 1, x2, y2 - 1))
    x1, y1, x2, y2 = const.floor[0][0], const.floor[0][1], const.floor[0][0] + const.floor[1][0], const.floor[0][1] + \
                                                           const.floor[1][1]
    const.up.add(class_borders.Border(x1, y1, x2, y1 + 1))  # Границы пола
    const.down.add(class_borders.Border(x1, y2 - 1, x2, y2))
    const.left.add(class_borders.Border(x1, y1, x1 + 1, y2))
    const.right.add(class_borders.Border(x2 - 1, y1, x2, y2))

    # Запрет игроку на выход из локации
    const.right.add(
        class_borders.Border(const.bloks[0][2] - 1, const.bloks[0][3], const.bloks[0][2], const.floor[0][1]))
    const.left.add(class_borders.Border(const.bloks[1][0] + 1, const.bloks[0][3], const.bloks[1][0], const.floor[0][1]))

    const.left.add(class_borders.Border(const.width - 1, 0, const.width, const.height))
    const.right.add(class_borders.Border(1, 0, 0, const.height))
    const.down.add(class_borders.Border(0, 0, const.width, 1))
    const.up.add(class_borders.Border(0, const.height - const.floor[1][1], const.width, const.height))

    # Дополнительная коллизия, если босс не готов получать урон
    const.dop_left.add(
        class_borders.Border(const.bloks[1][0] - 1, const.bloks[2][3], const.bloks[1][0], const.bloks[1][1]))
    const.dop_right.add(
        class_borders.Border(const.bloks[0][2] + 1, const.bloks[2][3], const.bloks[0][2], const.bloks[0][1]))

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
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not player.can_move[1]:
                        # Игрок может прыгать только на земле
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
                frame.check(player, buttons, room)
                room.drawing()
        if buttons.start:  # Игрок не в меню паузы
            pause.draw_pause()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()