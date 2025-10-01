import random

# Snakes and Ladders positions
snakes = {99: 7, 70: 55, 52: 42, 25: 4, 95: 72}
ladders = {6: 25, 11: 40, 60: 85, 46: 90, 17: 69}

def roll_dice():
    return random.randint(1, 6)

def move_player(curr_position, player_name):
    dice = roll_dice()
    print(f"{player_name} rolled: {dice}")
    curr_position += dice

    if curr_position in snakes:
        print(f"🐍 Oops! Snake at {curr_position}")
        curr_position = snakes[curr_position]

    elif curr_position in ladders:
        print(f"🪜 Yay! Ladder at {curr_position}")
        curr_position = ladders[curr_position]

    if curr_position > 100:
        curr_position -= dice  # Stay in place if overshoot 100

    print(f"{player_name} is now at: {curr_position}\n")
    return curr_position

def print_board(players):
    size = 10
    print("\n" + "="*50)
    for row in range(size, 0, -1):  # from 10 to 1
        line = []
        for col in range(1, size+1):
            num = (row-1)*10 + col
            if row % 2 == 0:  # reverse zigzag row
                num = row*10 - (col-1)

            # Default cell number
            cell = str(num).rjust(3)

            # Show players if any in this cell
            markers = [p for p, pos in players.items() if pos == num]
            if markers:
                cell = "/".join(markers).rjust(3)

            line.append(cell)
        print(" | ".join(line))
    print("="*50 + "\n")

# Initial positions
pos1, pos2, pos3, pos4 = 0, 0, 0, 0

while True:
    input("Player 1, press Enter to roll...")
    pos1 = move_player(pos1, "P1")
    print_board({"P1": pos1, "P2": pos2, "P3": pos3, "P4": pos4})
    if pos1 == 100:
        print("🎉 Player 1 wins the game!")
        break

    input("Player 2, press Enter to roll...")
    pos2 = move_player(pos2, "P2")
    print_board({"P1": pos1, "P2": pos2, "P3": pos3, "P4": pos4})
    if pos2 == 100:
        print("🎉 Player 2 wins the game!")
        break

    input("Player 3, press Enter to roll...")
    pos3 = move_player(pos3, "P3")
    print_board({"P1": pos1, "P2": pos2, "P3": pos3, "P4": pos4})
    if pos3 == 100:
        print("🎉 Player 3 wins the game!")
        break

    input("Player 4, press Enter to roll...")
    pos4 = move_player(pos4, "P4")
    print_board({"P1": pos1, "P2": pos2, "P3": pos3, "P4": pos4})
    if pos4 == 100:
        print("🎉 Player 4 wins the game!")
        break
    