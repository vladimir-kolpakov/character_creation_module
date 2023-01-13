class Character:
    ...


class Warrior(Character):
    ...


class Mage(Character):
    ...


class Healer(Character):
    ...


game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}


selected_class = None
char_name = None
selected_class = 'mage'
char_name = 'Игрок'

char_class = game_classes[selected_class](char_name)

print(char_class)
