# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 5
# Pacman Game objects and classes based on the original game PacMan by Toru Iwatani (Namco)


class Character:
    """Defined Character class"""
    def __init__(self, x, y, sp):
        self._x = x
        self._y = y
        self._movspeed = sp

    def movement(self, x_delta, y_delta):
        self._x = self._x + x_delta
        self._y = self._y + y_delta

class PacMan(Character):
    """Defines subclass Pacman(Character)"""
    _no_of_lives = 3

    @classmethod
    def check_lives(cls):
        return cls._no_of_lives != 0

    def __init__(self):
        PacMan._no_of_lives -= 1
        self.score = 0
        super().__init__(0, -50, 15)

    def chomp(self, food):
        if isinstance(food, Ghost):
            if food._status = 'blue':
                self._score += 500
                food.die()
            else:
                self.die(food)
        else:
            self.score += food._points
            food.remove()

    def die(self, Ghost):
        # Code here to show animation of PacMan death,
        # sound of death, etc.
        print('PacMan >>> Has been fragged by ' + ghost.name.title())
        self.score = 0

class Ghost(Character):
    """Defines the subclass Ghost(Character)"""
    def __init__(self, name):
        self._name = name
        self.status = 'fine'
        super().__init__(0, 0, 10)

    def sick(self):
        self._status = 'blue'
        self._movspeed = 5
    
    def graveReturn(self):
        self._status = 'death'
        self._movspeed = 25

    def die(self):
        print(self._name.title() + ' >>> has been chomped on by PacMan !!!')
        # Code here to animate ghost death, slight pause of death, play sound,
        # animate the eyes to return back to spawnpoint etc.

class Item:
    """Defines Item Class - eg pac-dots, fruit, PowerPills"""
    def __init__(self, xitem, yitem):
        self._xitem = xitem
        self._yitem = yitem
        # displays Item at position xitem, yitem

    def remove(self):
        pass
        # Code here to remove graphics of items when consumed.

class PacDot(Item):
    """Defines the objective item subclass PacDot(Item)"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self._points = 10

class PowerPill(Item):
    """Defines subclass PowerPill(Item) used to defeat Ghosts"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self._points = 50

def run():
    # inital set-up
    pac = PacMan()
    """Ghost objects named by its movement behaviour"""
    fickle = Ghost('inky')
    chaser = Ghost('blinky')
    ambusher = Ghost('pinky')
    stupid = Ghost('clyde')

    # Code here to privide top-level loop to control
    # execution of game...

if __name__ == "__main__": run()