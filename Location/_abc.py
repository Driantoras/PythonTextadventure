class Location:
    flavor_text = ''
    flavor_text_printed = False

    def __init__(self, player):
        self.visible = None
        self.items = [
            # [text, func reference, expression]
            # eg. ['Read', self.read, player.reading_skill > 3]
        ]

    def update_visible(self):
        self.visible = list(filter(lambda x: x[2], self.items))

    def show_options(self, player):
        self.__init__(player)
        self.update_visible()
        for i, item in enumerate(self.visible):
            print(f'{i + 1}| {item[0]}')

    def do(self, choice, player, questlog):
        self.__init__(player)
        self.update_visible()
        try:
            choice = int(choice) - 1
        except ValueError:
            return
        if 0 <= choice < len(self.visible):
            # return hings like 'beach', 'forest'
            return self.visible[choice][1](player, questlog)
