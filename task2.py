import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


matplotlib.use('TkAgg')


def plot_accordance(x, y, f, title='', n_figure=0, projection=1):
    list_x = sorted(x)
    list_y = sorted(y)

    ampl_x = len(list_x)
    ampl_y = len(list_y)
    center = max(ampl_x, ampl_y) / 2
    ellipse_x = Ellipse(xy=(1, center - 0.5), width=0.9, height=ampl_x * 1.1, edgecolor='k', fc='None', lw=2)
    ellipse_y = Ellipse(xy=(3, center - 0.5), width=0.9, height=ampl_y * 1.1, edgecolor='k', fc='None', lw=2)

    fig = plt.figure(n_figure)
    ax = fig.add_subplot(projection)
    ax.add_artist(ellipse_x)
    ax.add_artist(ellipse_y)
    ax.set_xlim(0, 4)
    ax.set_ylim(center * -0.3, center * 2.2)

    ellipse_x.set_clip_box(ax.bbox)
    ellipse_y.set_clip_box(ax.bbox)

    delta_h_x = center - len(list_x) / 2
    ax.scatter([1] * len(list_x), [i + delta_h_x for i in range(len(list_x))])
    for i in range(len(list_x)):
        ax.annotate(list_x[i], (0.87, i + delta_h_x - 0.13))

    delta_h_y = center - len(list_y) / 2
    ax.scatter([3] * len(list_y), [j + delta_h_y for j in range(len(list_y))])
    for j in y:
        ax.annotate(list_y[j], (3.06, j + delta_h_y - 0.13))

    for (k, v) in f:
        ax.annotate("", xytext=(1, list_x.index(k) + delta_h_x), xy=(3, list_y.index(v) + delta_h_y),
                    arrowprops=dict(arrowstyle="->"))

    ax.set_title(title)

    props = [False] * 4
    if x == {i for i, j in f}:
        props[0] = True
    if y == {j for i, j in f}:
        props[1] = True
    if len([j for i, j in f]) == len({j for i, j in f}):
        props[2] = True
    if len([i for i, j in f]) == len({i for i, j in f}):
        props[3] = True
    columns = ('всюду определённость', 'сурьективность', 'инъективность', 'функциональность')
    table = ax.table(
        rowLabels=[''],
        colLabels=columns,
        cellText=[['Да' if is_prop else 'Нет' for is_prop in props]],
        loc='bottom',
        cellLoc='center'
    )

    plt.axis('off')


def run():
    x = y = u = set(range(10))
    f = {(2, 4), (3, 3), (5, 9), (8, 7), (9, 9)}
    g = {(3, 5), (4, 3), (5, 3), (7, 3), (9, 5)}

    plot_accordance(x, y, f, 'f', 0, 111)
    plot_accordance({i for i in x if i != 0}, y, g, 'g', 1, 111)
    plt.show()