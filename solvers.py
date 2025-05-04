from point import Point
from grid import RectangleNet

class MKE:
    def __init__(self, grid, left=None, right=None, top=None, lower=None, border=None):
             #function of x, y
        self.grid = grid
        self.left = left
        self.right = right 
        self.top = top
        self.lower = lower
        self.border = border


    def solver2D(self):
        A_matrix = [[0 for i in range(len(nx))] for nx in self.grid.net]


        if self.left != None:
            for pl in self.grid.left_border:
                pl.set_potential(self.left(pl.x, pl.y))
                A_matrix[pl.i].append(1)
                 
            
        
        if self.right != None:
            for pr in self.grid.right_border:
                pr.set_potential(self.right(pr.x, pr.y))
                A_matrix[pr.i].append(1)

        if self.top != None:
            for pt in self.grid.top_border:
                pt.set_potential(self.top(pt.x, pt.y))
                A_matrix[pt.i][pt.j] = 1

        if self.lower != None:
            for plow in self.grid.lower_border:
                plow.set_potential(self.lower(plow.x, plow.y)) 
                A_matrix[plow.i][plow.j] = 1
        
        return A_matrix
        

        # if self.left != None:
             





    # def set_border_condition_potential(self, left=None, right=None, top=None, lower=None, border=None):
    #     if left != None:
    #         for pl in self.grid.left_border:
    #             pl.set_potential(left(pl.x, pl.y))
        
    #     if right != None:
    #         for pr in self.grid.right_border:
    #             pr.set_potential(right(pr.x, pr.y))

    #     if top != None:
    #         for pt in self.grid.top_border:
    #             pt.set_potential(top(pt.x, pt.y))

    #     if lower != None:
    #         for plow in self.grid.lower_border:
    #             plow.set_potential(lower(plow.x, plow.y)) 
        
    #     if border != None:
    #         figure_border = {(round(point.x, 5), round(point.y, 5)) for figur in self.grid.figurs for point in figur.border}
    #         for nx in self.grid.net:
    #             for p in nx:
    #                 if (round(p.x, 5), round(p.y, 5)) in figure_border:
    #                     p.set_potential(border(p.x, p.y))
        
