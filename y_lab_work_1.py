point_1 = (0, 2)  # координаты первой точки
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

d = [point_2, point_3, point_4, point_5]
big = []
for i in range(0, 4):
    for j in range(0, 4):
        if j != i:
            for k in range(0, 4):
                if k != j and k != i:
                    for m in range(0, 4):
                        if m != k and m != j and m != i:                            
                            big.append([point_1] + [d[i], d[j], d[k], d[m]] + [point_1])
length_list = []
for i in range(len(big)):
    way = 0
    for j in range(len(big[i])):
        if j + 1 != len(big[i]):
            distance = ((big[i][j + 1][0] - big[i][j][0]) ** 2 + (big[i][j + 1][1] - big[i][j][1]) ** 2) ** 0.5
            way += distance

    length_list += [way]
    if i == 0:
        way_min = way
    else:
        if way < way_min:
            way_min = way
shortest = []
for i in range(len(length_list)):
    if way_min == length_list[i]:
        shortest += [i]

arrow = '->'
for num in shortest:
    big[num]
    distance_1 = ((big[num][1][0] - big[num][0][0]) ** 2 + (big[num][1][1] - big[num][0][1]) ** 2) ** 0.5
    distance_2 = ((big[num][2][0] - big[num][1][0]) ** 2 + (big[num][2][1] - big[num][1][1]) ** 2) ** 0.5 + distance_1
    distance_3 = ((big[num][3][0] - big[num][2][0]) ** 2 + (big[num][3][1] - big[num][2][1]) ** 2) ** 0.5 + distance_2
    distance_4 = ((big[num][4][0] - big[num][3][0]) ** 2 + (big[num][4][1] - big[num][3][1]) ** 2) ** 0.5 + distance_3
    distance_5 = ((big[num][5][0] - big[num][4][0]) ** 2 + (big[num][5][1] - big[num][4][1]) ** 2) ** 0.5 + distance_4

    print([big[3][0], arrow, big[3][1], [distance_1], arrow, big[3][2], [distance_2], arrow, big[3][3], [distance_3],
          arrow, big[3][4], [distance_4], arrow, big[3][5], [distance_5]], '=', [distance_5])





  




