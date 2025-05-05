import matplotlib.pyplot as plt
from point import Point
from figure import Circle
from figure import Rectangle
from grid import RectangleNet
from solvers import MKE


EPS = 10**-1
MIN_X = -4
MAX_X = 6
MIN_Y = -2.5    
MAX_Y = 2.5
LEFT_POTENTIAL = 200
RIGHT_POTENTIAL = -200
NUM_ITER = 1000


def plot_net(React):

    x_net = [p.x for row in React.net for p in row if p.active == True]
    y_net = [p.y for row in React.net for p in row if p.active == True]
    potential = [p.psi for row in React.net for p in row if p.active == True]

    plt.scatter(x_net, y_net, c=potential,  cmap="magma" , s=10)

    

    # x_left = [p.x for p in React.left_border]
    # y_left = [p.y for p in React.left_border]
    # plt.scatter(x_left, y_left, color = "red", s=10)

    # x_right = [p.x for p in React.right_border]
    # y_right = [p.y for p in React.right_border]
    # plt.scatter(x_right, y_right, color = "black", s=10)

    # x_top = [p.x for p in React.top_border]
    # y_top = [p.y for p in React.top_border]
    # plt.scatter(x_top, y_top, color = "green", s=10)

    # x_lower = [p.x for p in React.lower_border]
    # y_lower = [p.y for p in React.lower_border]
    # plt.scatter(x_lower, y_lower, color = "lightgray", s=10)
   
    plt.gca().set_aspect('equal', adjustable='box')
    plt.colorbar(label='Potential')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    my_net = RectangleNet(MIN_X, MAX_X, MIN_Y, MAX_Y, EPS, EPS)

    fig1 = Circle(Point(0, 0), 1, EPS, EPS)
    fig2 = Rectangle(3, 4, -0.7, 0.7, EPS, EPS)


    my_net.add_figure(fig1)
    my_net.add_figure(fig2)

    # def left(x, y):
    #     if y > 0:
    #         return LEFT_POTENTIAL*(MAX_Y-y)
    #     else:
    #         return  -LEFT_POTENTIAL*(MIN_Y-y)


    # def right(x, y):
    #     if y > 0:
    #         return RIGHT_POTENTIAL*(MAX_Y-y)
    #     else:
    #         return  -RIGHT_POTENTIAL*(MIN_Y-y)


    def top(x, y):
        return LEFT_POTENTIAL
    
    def lower(x, y):
        return RIGHT_POTENTIAL
    
    def nulldudn(pot):
        return pot
    
    

    def func(x, y):
        return 0
        

    sim = MKE(my_net, func, None, None, top, lower, nulldudn)
    sim.solver2D(NUM_ITER)


    # value = [A_matrix[i][j] for i in x for ]

   

    # bfig1 = fig1.border
    # bfig2 = fig2.border

    # x = [p.x for p in bfig1]
    # y = [p.y for p in bfig1]

    # x2 = [p.x for p in bfig2]
    # y2 = [p.y for p in bfig2]

    # plt.scatter(x, y)
    # plt.scatter(x2, y2)
    # plt.show()

    plot_net(sim.grid)

        

        
       


