from point import Point


class RectangleNet:
    def __init__(self, min_x, max_x, min_y, max_y, hx, hy):
        num_px = int((max_x-min_x)/hx)+1
        num_py = int((max_y-min_y)/hy)+1
        self.net = [[Point(min_x+i*hx, min_y+j*hy, i, j) for j in range (num_py)] for i in range(num_px)]

        self.left_border = self.net[0]
        self.right_border = self.net[-1]
        self.lower_border = [self.net[i][0] for i in range(num_px)]
        self.top_border = [self.net[i][-1] for i in range(num_px)]
        self.figurs = []
        self.border_figure = []
        self.hx = hx
        self.hy = hy

    
    def add_figure(self, figure):
        figure_coords = {(round(fp.x, 5), round(fp.y, 5)) for fx in figure.net for fp in fx}
        border_cords = {(round(bp.x, 5), round(bp.y, 5)) for bp in figure.border}
        
        for nx in self.net:
            for np in nx: 
                if (round(np.x, 5), round(np.y, 5)) in figure_coords:
                    np.active = False
                if (round(np.x, 5), round(np.y, 5)) in border_cords:
                    self.border_figure.append(np)
        self.figurs.append(figure)

    #function of x, y

    # def set_border_condition_potential(self, left=None, right=None, top=None, lower=None, border=None):
    #     if left != None:
    #         for pl in self.left_border:
    #             pl.set_potential(left(pl.x, pl.y))
        
    #     if right != None:
    #         for pr in self.right_border:
    #             pr.set_potential(right(pr.x, pr.y))

    #     if top != None:
    #         for pt in self.top_border:
    #             pt.set_potential(top(pt.x, pt.y))

    #     if lower != None:
    #         for plow in self.lower_border:
    #             plow.set_potential(lower(plow.x, plow.y)) 
        
    #     if border != None:
    #         figure_border = {(round(point.x, 5), round(point.y, 5)) for figur in self.figurs for point in figur}
    #         for nx in self.net:
    #             for p in nx:
    #                 if (round(p.x, 5), round(p.y, 5)) in figure_border:
    #                     p.set_potential(border(p.x, p.y))

                
                        


    