from task1 import set_to_str


def run():
    u = list(range(1, 5))
    md = [[1, 0, 0, 1],
          [1, 0, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 0, 1]]
    d = {(x, y) for x in range(1, 5) for y in range(1, 5) if md[x - 1][y - 1] == 1}
    t = {(1, 2), (1, 3), (1, 4), (4, 2)}
    p = {(2, 2), (1, 4), (3, 4), (4, 1)}

    b1 = d & t
    b2 = d - t
    b3 = (d & t) ^ p
    b4 = {(y, x) for x, y in t}
    b5 = {(x, z) for x, yt in t for yp, z in p if yt == yp}

    b = [b1, b2, b3, b4, b5]
    for i in range(len(b)):
        print(f'b{i + 1}:')
        print(set_to_str(b[i]), end='\r\n\r\n')