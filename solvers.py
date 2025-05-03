from point import Point
from grid import RectangleNet

class MKE:
    def __init__(self, grid):
        self.grid = grid

    # def solver2D(Net, hx, hy):
        
    #     matrix = [0 for i in range]

    #     for i in range(len(Net)):
    #         for j in range(len(Net[i])):
                
     #function of x, y



    def set_border_condition_potential(self, left=None, right=None, top=None, lower=None, border=None):
        if left != None:
            for pl in self.grid.left_border:
                pl.set_potential(left(pl.x, pl.y))
        
        if right != None:
            for pr in self.grid.right_border:
                pr.set_potential(right(pr.x, pr.y))

        if top != None:
            for pt in self.grid.top_border:
                pt.set_potential(top(pt.x, pt.y))

        if lower != None:
            for plow in self.grid.lower_border:
                plow.set_potential(lower(plow.x, plow.y)) 
        
        if border != None:
            figure_border = {(round(point.x, 5), round(point.y, 5)) for figur in self.grid.figurs for point in figur.border}
            for nx in self.grid.net:
                for p in nx:
                    if (round(p.x, 5), round(p.y, 5)) in figure_border:
                        p.set_potential(border(p.x, p.y))
        
