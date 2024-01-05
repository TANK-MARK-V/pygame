import pygame
import class_player
import class_boss
import const

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    FPS = const.FPS
    running = True
    screen = pygame.display.set_mode(const.size)

    player = class_player.Player(const.load_image("герой.png", -1), 2, 1, 0, const.barotraum)  # Создание игрока
    const.player_group.add(player)

    boss = class_boss.Boss()
    const.boss_group.add(boss)

    buttons, inro, pause, frame, room, attack = const.make_prep(screen)  # Создание классов
    const.boss_group.add(boss)

    const.make_bloks()

    while running:
        for event in pygame.event.get():
            if not buttons.start:
                running = buttons.menu(screen, event)  # Открытие меню

            if event.type == pygame.QUIT:  # Выход
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Нажата кнопка мышки
                if buttons.start:  # Если идёт игра
                    if pause.check_do(pygame.mouse.get_pos(), const.pause_size):  # Проверка на нажатие паузы c мышки
                        buttons = const.make_prep(screen, True)  # Открытие меню

            if event.type == pygame.KEYDOWN:  # Нажата кнопка
                if event.key == pygame.K_ESCAPE and buttons.start:  # Проверка на нажатие паузы через "esc"
                    buttons = const.make_prep(screen, True)  # Открытие меню

                if inro.question:  # Проверка на ответ игрока на вопрос незнакомца
                    if event.key == pygame.K_y:  # Ответил правильно (Сюда добавить главный экран)
                        running = False
                    if event.key == pygame.K_n:  # Ответил неправильно
                        inro.ready = True
                        inro.question = False
                        player.rect.x = const.width // 2 - const.sprites // 2
                        player.rect.y = const.floor[0][1] - const.sprites
                        player.hp = 3
                        player.count = 0
                        player.killed = 0

                if inro.ready:  # Игра началась
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not player.can_move[1]:
                        # Игрок может прыгать только на земле
                        player.jump = True

                    # Начало движения
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.right = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.left = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        attack.pressed = True
                        attack.started = frame.count

            if event.type == pygame.KEYUP:  # Кнопку отпустили
                if inro.ready:  # Игра началась
                    # Конец движения
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.right = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.left = False

        if buttons.start:  # Игрок нажал "Играть"
            if not inro.ready:  # Проигрывание вступительного ролика
                inro.show(screen, player)
            else:  # Основная часть игры
                frame.check(player, buttons, room, boss)  # Счёт фреймов
                room.drawing(screen, boss.damage * 100)  # Отрисовка блоков
                running = frame.draw_hp(screen, player)  # Отрисовка здоровья игрока
                const.boss_group.draw(screen)
                attack.draw(screen, player, boss, frame.count)  # Отрисовка удара ложкой
            pause.draw_pause()  # Отрисовка кнопки паузы
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
