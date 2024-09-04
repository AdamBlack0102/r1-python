def logo_play():
    turtle_map = [[' ' for _ in range(10)] for _ in range(10)]

    current_turtle_x = 0
    current_turtle_y = 0

    last_char = ' '

    command_number = int(input())

    for _ in range(command_number):
        command = input().split()

        if len(command) < 3:
            command.append(last_char)
        else:
            last_char = command[2]

        direction, steps, char = command

        try:
            steps = int(steps)
        except ValueError:
            print("Error!")
            continue

        if direction == 'U':
            if current_turtle_y - steps < 0:
                print("Error!")
                continue
            for _ in range(steps):
                current_turtle_y -= 1
                turtle_map[current_turtle_y][current_turtle_x] = char
        elif direction == 'D':
            if current_turtle_y + steps > 9:
                print("Error!")
                continue
            for _ in range(steps):
                current_turtle_y += 1
                turtle_map[current_turtle_y][current_turtle_x] = char
        elif direction == 'L':
            if current_turtle_x - steps < 0:
                print("Error!")
                continue
            for _ in range(steps):
                current_turtle_x -= 1
                turtle_map[current_turtle_y][current_turtle_x] = char
        elif direction == 'R':
            if current_turtle_x + steps > 9:
                print("Error!")
                continue
            for _ in range(steps):
                current_turtle_x += 1
                turtle_map[current_turtle_y][current_turtle_x] = char

    for row in turtle_map:
        print(''.join(row))



