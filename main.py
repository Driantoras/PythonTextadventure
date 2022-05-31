import os
import pickle  # for saving and loading game states
import sys

import Location
from utilities import *
from player import Player
from quests import Questlog

SAVE_PATH = 'saved/'


def game_loop():
    global position

    current_location = location[position]

    while player.alive:

        # print stuff
        if not current_location.flavor_text_printed:
            print(current_location.flavor_text)
            current_location.flavor_text_printed = True

        print(
            f'{26 * "⎯"}\n'
            f'i| Inventar\n'
            f'c| Charakterstatus\n'
            f'h| Herstellung\n'
            f'q| Questlog\n')

        current_location.show_options(player)
        choice = input_plus('Was willst du tun?')

        # handle choice
        if choice == 'i':
            player.print_gold()
            item = player.inventory.open()
            if item is not None:
                player.use_item(item)

        elif choice == 'c':
            player.print_stats()
            player.print_gear()

        elif choice == 'h':
            player.open_crafting()

        elif choice == 'q':
            questlog.list_quests()

        elif choice == 'save':
            save_game()

        elif choice == 'load':
            if load_game():
                location.play()

        elif choice == 'menu':
            if input_plus(f'ja| Sicher?') == 'ja':
                main_menu()

        temp = current_location.do(choice, player, questlog)
        if temp:
            position = temp
            current_location = location[position]


def save_game():
    # prevent variable being permanent false
    location['forest'].plants = True

    save_name = input_valid_filename('Gib den Namen des Spielstands ein:')
    print(f'"{save_name}" wird angelegt...')

    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    if not os.path.exists(f'{SAVE_PATH}{save_name}'):
        os.mkdir(f'{SAVE_PATH}{save_name}')

    f = open(f'{SAVE_PATH}{save_name}/player.sav', 'wb+')
    pickle.dump(player, f)
    f = open(f'{SAVE_PATH}{save_name}/questlog.sav', 'wb+')
    pickle.dump(questlog, f)
    f = open(f'{SAVE_PATH}{save_name}/location.sav', 'wb+')
    pickle.dump(location, f)
    f = open(f'{SAVE_PATH}{save_name}/position.sav', 'wb+')
    pickle.dump(position, f)
    f.close()
    print('Spielstand erfolgreich gespeichert.')


def load_game():
    global player, questlog, location, position

    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    saves = os.listdir(SAVE_PATH)

    if not saves:
        print(f'Kein Spielstand vorhanden')
        return

    print(f'{len(saves)} {"Spielstand" if len(saves) == 1 else "Spielstände"} verfügbar\n')

    for i, save in enumerate(saves):
        print(f'{i + 1}| {save}')

    choice = input_plus(f'Entsprechende Zahl eingeben um den Spielstand zu laden.\n{ENTER_LINE}')

    if not choice.isnumeric():
        return

    choice_num = int(choice) - 1
    if not 0 <= choice_num < len(saves):
        return

    save_name = saves[choice_num]
    try:
        f = open(f'{SAVE_PATH}{save_name}/player.sav', 'rb')
        player_temp = pickle.load(f)
        f = open(f'{SAVE_PATH}{save_name}/questlog.sav', 'rb')
        questlog_temp = pickle.load(f)
        f = open(f'{SAVE_PATH}{save_name}/location.sav', 'rb')
        location_temp = pickle.load(f)
        f = open(f'{SAVE_PATH}{save_name}/position.sav', 'rb')
        position_temp = pickle.load(f)
        f.close()
    except pickle.UnpicklingError:
        print(f'"{save_name}" ist beschädigt')

    else:
        player = player_temp
        questlog = questlog_temp
        location = location_temp
        position = position_temp
        print('Spielstand erfolgreich geladen.')
        return True


def new_game():
    global player, questlog, location, position

    player = Player()
    questlog = Questlog()
    location = Location.create(player)
    position = 'beach'


def main_menu():
    while True:
        choice = input_plus(
            f'1| Neues Spiel\n'
            f'2| Spielstand laden\n'
            f'3| Verlassen\n')

        if choice == '1':
            new_game()
            game_loop()

        elif choice == '2':
            if load_game():
                game_loop()

        elif choice == '3':
            sys.exit()


if __name__ == '__main__':
    player: Player
    questlog: Questlog
    location: Location.create
    position: str

    main_menu()
