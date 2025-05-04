import matplotlib.pyplot as plt
from point import Point
from figure import Circle
from grid import RectangleNet
from solvers import MKE


EPS = 5*10**-2
MIN_X = -20
MAX_X = 20
MIN_Y = -10
MAX_Y = 10
LEFT_POTENTIAL = 200
RIGHT_POTENTIAL = -200


def plot_net(React):

    x_net = [p.x for row in React.net for p in row if p.active == True]
    y_net = [p.y for row in React.net for p in row if p.active == True]
    potential = [p.psi for row in React.net for p in row if p.active == True]

    plt.scatter(x_net, y_net, c=potential,  cmap="coolwarm" , s=1)

    

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
    fig2 = Circle(Point(2, 0), 2, EPS, EPS)


    my_net.add_figure(fig1)
    my_net.add_figure(fig2)

    def left(x, y):
        return LEFT_POTENTIAL

    def right(x, y):
        return RIGHT_POTENTIAL
    
    def nulldudn(pot):
        return pot
        

    sim = MKE(my_net, left, right, None, None, nulldudn)
    A_matrix = sim.solver2D()

    # x = [i for i in range(len(A_matrix)) for j in range(len(A_matrix[i]))]
    # y = [j for row in A_matrix for j in range(len(row))]

    # plt.scatter(x, y)
    # plt.show()

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

        

        
       


