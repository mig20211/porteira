class Cube:
    def __init__(self):
        self.is_held = False
        self.name = "a cube"

    def use(self):
        self.is_held = True

    def show(self):
        print("you hold "+self.name)


class Door:
    def __init__(self):
        self.is_held = False
        self.name = "the door"

    def use(self):
        self.is_held = True

    def show(self):
        print("you hold "+self.name)
        print("but its locked")
        print("nothing happen")


class Button:
    def __init__(self):
        self.is_held = False
        self.name = "the button"

    def use(self):
        self.is_held = True

    def show(self):
        print("you press "+self.name)
        print("you tried to press the button but you're not strong enough ")
        print("nothing happen")

class Wall:
    def __init__(self):
        self.is_held = False
        self.name = "the wall"

    def use(self):
        self.is_held = True

    def show(self):
        print("you hold "+self.name)
        print("you try to pick up the wall but it is too heavy")
        print('you let go of the wall')

class Joao:
    def __init__(self):
        self.is_held = False

    def use(self, thing):
        self.is_held = thing
        thing.show()


class Scenario:
    def __init__(self):
        self.hero = Joao()
        self.view = Wall()
        self.exit = Door()
        self.thing = Cube()
        self.action = Button()

    def use(self):
        thing = input("Use: 1-door, 2-button, 3-cube, 4-wall")
        thing = int(thing) - 1
        whatever = [self.exit, self.action, self.thing, self.view]
        self.hero.use(whatever[thing])


def main():
    print("Welcome to Porteira!")
    print("you can see a white wall, a button, a cube and a door")
    scenario = Scenario()
    scenario.use()


if __name__ == '__main__':
    main()
