import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def plot_using_matplotlib(title):
    xs = np.linspace(0, 2 * np.pi)
    ys1 = np.sin(xs)
    ys2 = np.cos(xs)
    ys3 = np.sin(xs)*np.exp(-xs)

    plt.plot(xs, ys1, label="sin")
    plt.plot(xs, ys2, label="cos")
    plt.plot(xs, ys3, label="sin*exp(-x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title(title)
    plt.show()


plot_using_matplotlib("タイトル : Before importing yagamee")
import yagamee
plot_using_matplotlib("タイトル : After importing yagamee")
yagamee.matplotlib_tools.restore_rcparams()
plot_using_matplotlib("タイトル : After restoring rcparams")