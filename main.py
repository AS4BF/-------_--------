import matplotlib.pyplot as plt
from point import Point
from figure import Circle
from grid import RectangleNet

EPS = 10**-1
MIN_X = -20
MAX_X = 20
MIN_Y = -10
MAX_Y = 10


def plot_net(React):

    x_net = [p.x for row in React.net for p in row]
    y_net = [p.y for row in React.net for p in row]

    plt.scatter(x_net, y_net, color = "blue", s=1)

    x_left = [p.x for p in React.left_border]
    y_left = [p.y for p in React.left_border]
    plt.scatter(x_left, y_left, color = "red", s=10)

    x_right = [p.x for p in React.right_border]
    y_right = [p.y for p in React.right_border]
    plt.scatter(x_right, y_right, color = "black", s=10)

    x_top = [p.x for p in React.top_border]
    y_top = [p.y for p in React.top_border]
    plt.scatter(x_top, y_top, color = "green", s=10)

    x_lower = [p.x for p in React.lower_border]
    y_lower = [p.y for p in React.lower_border]
    plt.scatter(x_lower, y_lower, color = "lightgray", s=10)
   
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    my_net = RectangleNet(MIN_X, MAX_X, MIN_Y, MAX_Y, EPS)

    fig1    = Circle(Point(0, 0), 4, EPS)
    fig2 = Circle(Point(2, 0), 2, EPS)


    my_net.add_figure(fig1)


    plot_net(my_net)

        

        
       


