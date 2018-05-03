#!/usr/bin/python3
def func_y(x):
    return x**2.0

class DiffShow:
    def numerical_diff(self, f, x):
        h = 1e-4
        d =  (f(x+h) - f(x-h))/(2.0*h)
        return d


    def show_overlap(self, f, x):

        y = f(x)
        dy = [ self.numerical_diff(func_y,i) for i in x ]

        fig, ax1 = plt.subplots()
        ax1.plot(x, y, color='red')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.tick_params('y', colors='red')

        ax2 = ax1.twinx()
        ax2.plot(x, dy, color='blue')
        ax2.set_ylabel('dy')
        ax2.tick_params('y', colors='blue')

        fig.tight_layout()
        plt.show()

    def show_updown(self, f, x):

        y = f(x)
        dy = [ self.numerical_diff(func_y,i) for i in x ]

        plt.subplot(2, 1, 1)
        plt.plot(x, y, '-', lw=2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(x, dy, '-', lw=2)
        plt.xlabel('x')
        plt.ylabel('dy')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    def line_y_from_x(self, f, xy, a):
        a_slope = self.numerical_diff(f, xy[0])
        return xy[1] + (a - xy[0]) * a_slope


    def draw_slope_at(self, f, x, a):

        y =  f(x)

        fig, ax1 = plt.subplots()
        ax1.plot(x, y, color='red')
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.tick_params('y', colors='red')


        
        xmin, xmax = ax1.get_xlim()

        ymin = self.line_y_from_x(f, [a, f(a)], xmin)
        ymax = self.line_y_from_x(f, [a, f(a)], xmax)

        ax1.plot([xmin, xmax ], [ymin, ymax], color='blue')
        ax1.set_ylabel('dy')
        ax1.tick_params('y', colors='blue')

        fig.tight_layout()
        plt.show()


import numpy as np
import matplotlib.pylab as plt

x = np.arange(-2.0, 2.0, 0.1)
#DiffShow().show_overlap(func_y, x)
#DiffShow().show_updown(func_y, x)
DiffShow().draw_slope_at(func_y, x, 0.5)
