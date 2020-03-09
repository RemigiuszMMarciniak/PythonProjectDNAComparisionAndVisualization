dot_plot = [[1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 0]]
window_size = 3
threshold = 1
x = 0
y = 0
window_size_i = window_size
for i in range(len(dot_plot)):
    x += i
    window_size_i += i
    for j in range(len(dot_plot[i])):
        y += j
        window_size_i += j
        for xi in range(x, window_size_i):
            for yi in range(y, window_size_i):
                print("Vector: i: " + str(i) + " j: " + str(j) + " , xi: " + str(xi) + " , yi: " + str(yi))

        y = 0
        window_size_i = window_size
    x = 0
    window_size_i = window_size