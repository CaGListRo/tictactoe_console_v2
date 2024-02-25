import os
import sys


PLAYING_FIELD = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_winning(player, playing_field):
    for column in range(3):
        if playing_field[column] == playing_field[column + 3] and playing_field[column + 3] == playing_field[column + 6]:
            return True
        
    for line in range(0, 7, 3):
        print(line)
        if playing_field[line] == playing_field[line + 1] and playing_field[line + 1] == playing_field[line + 2]:
            return True
    if playing_field[0] == playing_field[4] and playing_field[4] == playing_field[8]:
        return True
    if playing_field[2] == playing_field[4] and playing_field[4] == playing_field[6]:
        return True


def player_swab(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


def mark_choice(player, playing_field, field_choice):
    field_choice -= 1
    if player == 1:
        playing_field[field_choice] = "X"
    else:
        playing_field[field_choice] = "O"


def get_input(player, playing_field):   
    while True:
        field_choice = input(f"\nSpieler {player}: ")
        if field_choice.isdigit():
            field_choice = int(field_choice)
            if 0 < field_choice <= 9:
                if field_choice == playing_field[field_choice - 1]:
                    break
                elif field_choice != playing_field[field_choice - 1]:
                    sys.stdout.write(f"Feld schon belegt, versuche es erneut Spieler {player}\n")
            else:
                sys.stdout.write("Nur Zahlen zwischen 1 und 9 sind erlaubt.\n")
        else:
            sys.stdout.write("Bitte eine Zahl eingeben...\n")
    return field_choice


def draw_playing_field(playing_field):
    numb_counter, line_counter = 0, 0
    for x in range(9):
        numb_counter += 1
        sys.stdout.write(str(playing_field[x]))
        if numb_counter == 3:
            sys.stdout.write("\n")
            line_counter += 1
            numb_counter = 0
            if line_counter < 3:
                sys.stdout.write("----------\n")
        else:
            sys.stdout.write(" | ")


def init_game(playing_field):
    del playing_field[:]
    for x in range(9):
        playing_field.append(PLAYING_FIELD[x])


def main():
    again_loop = True
    player = 1

    while again_loop:
        lap_counter = 0
        won = False
        playing_field = []
        init_game(playing_field)
            
        while not won:
            os.system("cls")
            draw_playing_field(playing_field)
            field_choice = get_input(player, playing_field)
            mark_choice(player, playing_field, field_choice)
            won = check_winning(player, playing_field)
            lap_counter += 1
            if won or lap_counter == 9:
                break
            player = player_swab(player)

        os.system("cls")
        draw_playing_field(playing_field)
        if won:            
            again = input(f"\nSpieler {player} hat gewonnen! Nochmal? (j/n) ")
        if lap_counter >= 9:
            again = input(f"\nUnentschieden! Nochmal? (j/n) ")
        if again.lower() == "n":
            sys.stdout.write("\nTschüss...")
            again_loop = False
        else:
            player = player_swab(player)       

if __name__ == "__main__":
    main()