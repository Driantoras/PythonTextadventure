from re import match

# translate  ANSI character Escape Sequences to increase readability
BLACK = '\033[30m'
GREY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\33[93m'
BLUE = '\33[94m'
MAGENTA = '\33[95m'
CYAN = '\33[96m'
WHITE = '\33[97m'

BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINED = '\033[4m'
CROSSED_OUT = '\033[9m'

# disables all attributes e.g. BOLD, RED,...
NORMAL = '\033[0m'

ENTER_LINE = f'Ansonsten {ITALIC}{BOLD}Enter{NORMAL} drücken'

ADDED = f'{GREEN}+{NORMAL}'
REMOVED = f'{RED}-{NORMAL}'


# creates fancy input and clears terminal after input
def input_plus(output):
    input_value = input(f'\n{output}\n{YELLOW}{BOLD}=>{NORMAL} ')
    print('\033c', end='')
    return input_value


def input_valid_filename(input_question):
    pattern = '^[A-Za-z0-9_-]*$'

    while True:
        user_input = input_plus(input_question)
        result = match(pattern, user_input)
        if result:
            return user_input
        else:
            print(f'Es können nur _, -, Buchstaben und Zahlen verwendet werden.')
