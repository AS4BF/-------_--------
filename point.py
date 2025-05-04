class Point:
    def __init__(self, x, y, i = None, j = None):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.vx = 0
        self.vy = 0
        self.psi = 0
        self.active = True
      

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def set_potential(self, psi):
        self.psi = psi

        