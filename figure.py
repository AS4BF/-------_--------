from point import Point

class Circle:
    def __init__(self, pc, radius, h):
        min_x = pc.x - radius 
        max_x = pc.x + radius
        min_y = pc.y - radius
        max_y = pc.y + radius
        self.net = []
        self.boarder = []
        x = min_x
        while x <= max_x:
            net_point = []
            y = min_y
            while y <= max_y:
                r2 = (x-pc.x)**2+(y-pc.y)**2
                if r2<(radius)**2:
                    net_point.append(Point(x, y))
                elif r2-radius**2 < h/2:
                    self.boarder.append(Point(x, y))
                y += h
            self.net.append(net_point)
            x += h
