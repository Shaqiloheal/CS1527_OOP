class Rectangle:
    __doc__ = 'Rectangle GUI Component'

    def __init__(self, xc, yc, siz, **kwargs):
        super().__init__(**kwargs)
        self._xcoord = xc
        self._ycoord = yc
        self._size = siz


class Clickable:
    __doc__ = 'Simple GUI Clickable Object'

    def __init__(self, stat, **kwargs):
        super().__init__(**kwargs)
        self._status = stat

    def press(self):
        if self._status == 'ON':
            self._status = 'OFF'
        else:
            self._status = 'ON'

class Button(Clickable):

    def __init__(self, lbl, **kwargs):
        super().__init__(**kwargs)
        self._label = lbl

myButton = Button(xc = 0, yc = 0, siz = 50, stat = 'OFF', lbl = 'Press Me')