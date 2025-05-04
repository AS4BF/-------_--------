from point import Point

class Circle:
    def __init__(self, pc, radius, hx, hy):
        min_x = pc.x - radius 
        max_x = pc.x + radius
        min_y = pc.y - radius
        max_y = pc.y + radius
        self.net = []
        self.border = []
        x = min_x
        
        while x <= max_x:
            net_point = []
            y = min_y
            while y <= max_y:
                r2 = (x-pc.x)**2+(y-pc.y)**2
                if r2<(radius)**2:
                    net_point.append(Point(x, y))
                y += hy
            self.net.append(net_point)
            x += hx
        ps = {(round(p.x, 5), round(p.y, 5)) for row in self.net for p in row}

        for row in self.net:
            for p in row:
                px = round(p.x, 5)
                py = round(p.y, 5)
                neighbors = [(round(px + hx, 5), py),
            (round(px - hx, 5), py),
            (px, round(py + hy, 5)),
            (px, round(py - hy, 5))]
                for nx, ny in neighbors:
                    if (nx, ny) not in ps:
                        self.border.append(Point(nx, ny))
                        
                        


