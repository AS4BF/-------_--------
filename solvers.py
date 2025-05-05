from point import Point
from grid import RectangleNet

class MKE:
    def __init__(self, grid, func, left=None, right=None, top=None, lower=None, border=None):
             #function of x, y
        self.grid = grid
        self.left = left
        self.right = right 
        self.top = top
        self.lower = lower
        self.border = border
        self.func = func


    def solver2D(self, num_iteration):


        if self.left != None:
            for pl in self.grid.left_border:
                pl.set_potential(self.left(pl.x, pl.y))
                 
        
        if self.right != None:
            for pr in self.grid.right_border:
                pr.set_potential(self.right(pr.x, pr.y))


        if self.top != None:
            for pt in self.grid.top_border:
                pt.set_potential(self.top(pt.x, pt.y))

        if self.lower != None:
            for plow in self.grid.lower_border:
                plow.set_potential(self.lower(plow.x, plow.y)) 


        
        for it in range(num_iteration):
            print(it)
            border_not_set = True
            for i in range(1, len(self.grid.net)-1):
                for j in range(1, len(self.grid.net[i])-1):
                    p = self.grid.net[i][j]
                    hx = self.grid.hx
                    hy = self.grid.hy
            
                    if not p.active:
                        continue

                    pxm = self.grid.net[i-1][j]
                    pxp = self.grid.net[i+1][j]
                    pym = self.grid.net[i][j-1]
                    pyp = self.grid.net[i][j+1]

                    if not (pxm.active and pxp.active and pym.active and pyp.active):
                        top = {(round(pb.x, 5), round(pb.y, 5)) for pb in self.grid.top_border}
                        lower = {(round(pb.x, 5), round(pb.y, 5)) for pb in self.grid.right_border}
                        
                            
                             
                        if (round(p.x, 5), round(p.y, 5)) in top:
                            p.psi = pxm.psi
                        elif (round(p.x, 5), round(p.y, 5)) in lower:
                            p.psi = pxm.psi
                        elif border_not_set:
                            border_not_set = False
                            p.psi = pxm.psi

                            for pb in self.grid.border_figure:
                                pb.psi = self.border(p.psi)


                        continue
                    
                    p.psi = ((pxp.psi+pxm.psi)*hy**2+(pyp.psi+pym.psi)*hx**2-self.func(p.x, p.y)*(hx*hy)**2)/(2*(hx**2+hy**2))




        

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
        
