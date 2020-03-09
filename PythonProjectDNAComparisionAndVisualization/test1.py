# window_size = 3
# threshold = 1
#
# dot_plot = [[0, 1, 1, 1, 0] , [ 1, 0, 0, 0, 1], [ 1, 0, 0, 0, 1], [ 1, 1, 1, 0, 1], [ 0, 0, 0, 0, 0]]
# filtered_dot_plot = [[0 for x in range(len(dot_plot[0]))] for y in range(len(dot_plot))]
#
# print(dot_plot)
# print(filtered_dot_plot)
#
# window_x_range = window_size
# window_y_range = window_size
#
# for i in range(len(dot_plot) - window_size):
#
#     window_x = 0
#     window_x_range = window_size
#
#     for j in range(len(dot_plot[i]) - window_size):
#         window_y = 0
#         window_y_range = window_size
#
#         counter = 0
#
#         for window_x in range(window_x_range + window_x):
#             for window_y in range(window_y_range + window_y):
#
#
#                 if window_x == window_y:
#
#                     if dot_plot[window_x][window_y] == 1:
#                         counter += 1
#                         # print("counter " + str(counter))
#
#         # print("counter " + str(counter))
#         # print("window_size - threshold " + str(window_size - threshold))
#         # print(counter >= (window_size - threshold))
#
#         if counter >= (window_size - threshold):
#             # print("counter>")
#             for window_x in range(window_x_range):
#                 for window_y in range(window_y_range):
#                     if window_x == window_y:
#                         if dot_plot[window_x][window_y] == 1:
#                             filtered_dot_plot[window_x][window_y] = 1
#                         else:
#                             filtered_dot_plot[window_x][window_y] = 0
#
#         else:
#             # print("counter<")
#             for window_x in range(window_x_range):
#                 for window_y in range(window_y_range):
#                     if window_x == window_y:
#                         filtered_dot_plot[window_x][window_y] = 0
#     window_y += 1
#     window_y_range += 1
# window_x += 1
# window_x_range += 1
#
from mpmath import diag













#
# dot_plot = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 0]]
# filtered_dot_plot = [[0 for x in range(len(dot_plot))] for y in range(len(dot_plot[0]))]
# first_matrix = dot_plot
# second_matrix = dot_plot[0]
# threshold = 1
# window_size = 3
#
#
# def sum_diag(matrix):
#     counter = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i == j:
#                 if matrix[i][j] == 1:
#                     counter += 1
#     return counter
#
#
# def create_matrix_window(dot_plot, window_size, i, j):
#     matrix = [[0 for x1 in range(window_size)] for y1 in range(window_size)]
#     a = 0
#     for x in range(i, i + window_size):
#         b = 0
#         for y in range(j, j + window_size):
#             print("X, Y: " + str(x) + " " + str(y))
#             print("A, B: " + str(a) + " " + str(b))
#             print("matrix: " + str(matrix[a][b]))
#             print("dot_plot: " + str(dot_plot[x][y]))
#             matrix[a][b] = dot_plot[x][y]
#             b += 1
#         a += 1
#     return matrix
#
#
# for i in range(len(dot_plot) - window_size):
#     for j in range(len(dot_plot[0]) - window_size):
#         # window matrix
#         print("i, j : " + str(i) + " " + str(j))
#         window_matrix = create_matrix_window(dot_plot, window_size, i, j)
#         # [i:i + window_size, j:j + window_size]
#         print(" window matrix " + str(window_matrix))
#         if sum_diag(window_matrix) >= window_size - threshold:
#             print("============")
#             for k in range(len(window_matrix)):
#                 print("len : " + str(len(window_matrix)))
#                 filtered_dot_plot[i + k][j + k] = window_matrix[k][k]
#                 print(filtered_dot_plot[i + k][j + k])
#             print("============")
#
# for a1 in range(len(dot_plot)):
#     for a2 in range(len(dot_plot[0])):
#         print(dot_plot[a1][a2], end=' ')
#     print()
#
# print()
# for a1 in range(len(dot_plot)):
#     for a2 in range(len(dot_plot[0])):
#       print(filtered_dot_plot[a1][a2], end=' ')
#     print()