import sys


def cham_tower(poured, query_glass, query_row):
    g = [[0 for i in range(101)] for i in range(101)]
    g[0][0] = poured

    for i in range(0, query_row + 1):
        for j in range(0, i + 1):
            if g[i][j] > 1:
                g[i+1][j] += (g[i][j]-1) / 2.0
                g[i+1][j+1] += (g[i][j]-1) / 2.0
                g[i][j] = 1
            else:
                continue

    # for i in range(0, query_row + 1):
    #     for j in range(0, i + 1):
    #         print g[i][j],
    #     print

    return g[query_row][query_glass]


if __name__ == "__main__":
    poured = int(sys.argv[1])
    query_glass = int(sys.argv[2])
    query_row = int(sys.argv[3])
    print cham_tower(poured, query_glass, query_row)

