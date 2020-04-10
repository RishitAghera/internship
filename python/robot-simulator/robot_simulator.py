NORTH=0
EAST=90
SOUTH=180
WEST=270

class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self.direction = direction

    @property
    def coordinates(self):
        return (self._x, self._y)

    def turn_left(self):
        self.direction = (self.direction - 90) % 360

    def turn_right(self):
        self.direction = (self.direction + 90) % 360

    def advance(self):
        if self.direction == NORTH:
            self._y += 1
        elif self.direction == EAST:
            self._x += 1
        elif self.direction == SOUTH:
            self._y -= 1
        else:
            self._x -= 1

    def move(self, program):
        for instr in program:
            if instr == 'L':
                self.turn_left()
            elif instr == 'R':
                self.turn_right()
            else:
                self.advance()