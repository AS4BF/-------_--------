from point import Point


class RectangleNet:
    def __init__(self, min_x, max_x, min_y, max_y, h):
        num_px = int((max_x-min_x)/h)+1
        num_py = int((max_y-min_y)/h)+1
        self.net = [[Point(min_x+i*h, min_y+j*h) for j in range (num_py)] for i in range(num_px)]

        self.left_border = self.net[0]
        self.right_border = self.net[-1]
        self.lower_border = [self.net[i][0] for i in range(num_px)]
        self.top_border = [self.net[i][-1] for i in range(num_px)]
        self.figurs = []

       

    
    def add_figure(self, figure):
        figure_coords = {(round(fp.x, 5), round(fp.y, 5)) for fx in figure.net for fp in fx}
        net = []
        for nx in self.net:
            xnet = []
            for np in nx: 
                if (round(np.x, 5), round(np.y, 5)) not in figure_coords:
                    xnet.append(np)
            net.append(xnet)
        self.net = net

        self.figurs.append(figure)
