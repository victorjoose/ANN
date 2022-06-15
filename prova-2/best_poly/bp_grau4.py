import best_poly as bp

if __name__ == '__main__':
    x = [-4.4406, -4.3701, -4.2524, -4.1563, -4.0562, -3.9837, -3.8296, -3.7868, -3.651, -3.6231, -3.4627, -3.3717, -3.2946, -3.2285, -3.0793, -3.0409, -2.8776, -2.7743, -2.7137, -2.6491, -2.5579, -2.3854, -2.3488, -2.1808, -2.1576, -2.0374, -1.9636, -1.7958, -1.7083, -1.6428, -1.5015, -1.3997, -1.3672, -1.2378, -1.1767, -1.0662, -0.9257, -0.8615, -0.7543, -0.6648, -0.5362, -0.4427, -0.3358, -0.2593, -0.2147, -0.1151, -0.0301, 0.14, 0.2168, 0.3194, 0.4086, 0.5289, 0.5677, 0.6439, 0.8123, 0.8868, 0.9628, 1.0753, 1.1598, 1.2845, 1.396, 1.4632, 1.5617, 1.6625, 1.7809, 1.8907, 1.939, 2.0369, 2.1118, 2.2071, 2.3474, 2.4463, 2.5246, 2.6407, 2.6884, 2.8457, 2.9421, 3.0064, 3.1041, 3.2069, 3.2859, 3.4195, 3.4648, 3.5462, 3.7027, 3.8107, 3.9325, 3.9432, 4.0352, 4.1298, 4.2306, 4.3852, 4.4282, 4.5461, 4.709, 4.7523, 4.8611, 4.9376]
    y = [1.1609, 2.1091, 3.252, 3.9, 4.6192, 5.1689, 6.1534, 5.922, 6.8921, 6.933, 7.3201, 7.5435, 8.417, 7.4055, 7.6767, 7.8025, 7.764, 7.7691, 8.0048, 7.3198, 9.3978, 7.487, 7.8079, 7.1462, 7.1304, 7.001, 6.7031, 6.5142, 6.4819, 6.6788, 6.0, 5.7826, 5.6667, 5.243, 5.2711, 5.3119, 4.5636, 4.8901, 4.4658, 4.672, 4.6531, 4.1435, 4.057, 4.3582, 3.9373, 4.2994, 3.8391, 4.2184, 4.0587, 5.0732, 4.2726, 4.5504, 3.4695, 4.2822, 4.5918, 5.6737, 4.0644, 4.7613, 5.116, 3.9918, 5.901, 5.9403, 6.4131, 6.3605, 6.703, 5.33, 7.1012, 7.7935, 7.6553, 7.9445, 8.4629, 8.8456, 8.4963, 9.2124, 9.6944, 9.9868, 9.9381, 8.6905, 10.6519, 10.7685, 10.8235, 9.8997, 10.8752, 11.1024, 11.0262, 9.9705, 10.6642, 9.8202, 10.597, 8.6708, 9.7544, 9.5164, 9.2453, 8.6588, 7.0644, 6.4423, 6.4528, 6.0989]

    a0, a1, a2, a3, a4 = bp.best_poly(x, y, 4)

    print(f'{a0 = } , {a1 = }, {a2 = }, {a3 = }, {a4 = }')