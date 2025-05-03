class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.psi = 0
      

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def set_potential(self, psi):
        self.psi = psi

        