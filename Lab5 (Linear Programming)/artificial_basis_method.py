import numpy as np


def artificial_basis(simplex_table, m, n):
    answer_vector = np.zeros([m * n])
    artificial_vector = np.zeros([n])
    dim_new = m * n + 1
    obj_func_num = m + n + 1

    while simplex_table[obj_func_num, 0] != 0:
        f_max = simplex_table[obj_func_num, 1]
        j_gen = 1
        for j in range(1, dim_new):
            if simplex_table[obj_func_num, j] >= f_max:
                f_max = simplex_table[obj_func_num, j]
                j_gen = j

        f_min = simplex_table[0, j_gen]
        i_gen = 0
        for i in range(m + n - 1):
            if f_min <= 0 or (simplex_table[i_gen, 0] > 0 and simplex_table[i + 1, 0] > 0 and simplex_table[i + 1, j_gen] > 0 and simplex_table[i + 1, 0]/simplex_table[i + 1, j_gen] <= simplex_table[i_gen, 0]/f_min):
                f_min = simplex_table[i + 1, j_gen]
                i_gen = i + 1

        general_element = simplex_table[i_gen, j_gen]
        simplex_table[i_gen, j_gen] = 1/general_element

        for i in range(m + n + 2):
            if i != i_gen:
                simplex_table[i, j_gen] *= -1 * simplex_table[i_gen, j_gen]

        for i in range(m + n + 2):
            for j in range(dim_new):
                if i != i_gen and j != j_gen:
                    simplex_table[i, j] += simplex_table[i, j_gen] * simplex_table[i_gen, j]

        for j in range(dim_new):
            if j != j_gen:
                simplex_table[i_gen, j] *= simplex_table[i_gen, j_gen]

        if i_gen >= m and i_gen <= m + n - 1 and artificial_vector[i_gen - m] == 0:
            artificial_vector[i_gen - m] = j_gen

        i_used = -1

        for i in range(m * n):
            if answer_vector[i] == i_gen + 1:
                i_used = i

        if answer_vector[j_gen - 1] == 0:
            answer_vector[j_gen - 1] = i_gen + 1
            if i_used != -1:
                answer_vector[i_used] = -j_gen
        elif answer_vector[j_gen - 1] > 0:
            for i in range(m * n):
                if answer_vector[i] == -j_gen:
                    answer_vector[i] = i_gen + 1
                    answer_vector[j_gen - 1] = -j_gen
                    break
                elif answer_vector[i] == j_gen:
                    answer_vector[i] = -j_gen
                    break
        elif answer_vector[j_gen - 1] < 0:
            for i in range(m * n):
                if answer_vector[i] == i_gen + 1:
                    answer_vector[i] = answer_vector[j_gen - 1]
                    break
            answer_vector[j_gen - 1] = i_gen + 1

        print(artificial_vector)
        print(answer_vector)
        print(simplex_table)
        print("\n")

    for j in range(n - 1, -1, -1):
        if artificial_vector[j] != 0:
            for i in range(m * n):
                if answer_vector[i] < 0 and abs(answer_vector[i]) > artificial_vector[j]:
                    answer_vector[i] += 1
            simplex_table = np.delete(simplex_table, (int(artificial_vector[j])), axis=1)

    simplex_table = np.delete(simplex_table, (m + n + 1), axis=0)

    print(answer_vector)
    print(simplex_table)
    print("\n")

    return simplex_table, answer_vector


def default_simplex(simplex_table, m, n, X):
    answer_vector = X
    obj_func_num = simplex_table.shape[0] - 1
    dim_new = simplex_table.shape[1]
    is_optimal = False

    while 1:
        for j in range(dim_new - 1):
            if simplex_table[obj_func_num, j + 1] <= 0:
                is_optimal = True
            else:
                is_optimal = False
                break

        if is_optimal:
            break

        f_max = simplex_table[obj_func_num, 1]
        j_gen = 1
        for j in range(dim_new - 1):
            if simplex_table[obj_func_num, j + 1] > f_max:
                f_max = simplex_table[obj_func_num, j + 1]
                j_gen = j + 1

        f_min = simplex_table[0, j_gen]
        i_gen = 0
        for i in range(obj_func_num - 1):
            if f_min <= 0 or (simplex_table[i_gen, 0] > 0 and simplex_table[i + 1, 0] > 0 and simplex_table[i + 1, j_gen] > 0 and simplex_table[i + 1, 0] / simplex_table[i + 1, j_gen] < simplex_table[i_gen, 0] / f_min):
                f_min = simplex_table[i + 1, j_gen]
                i_gen = i + 1

        general_element = simplex_table[i_gen, j_gen]
        simplex_table[i_gen, j_gen] = 1 / general_element

        for i in range(obj_func_num + 1):
            if i != i_gen:
                simplex_table[i, j_gen] *= -1 * simplex_table[i_gen, j_gen]

        for i in range(obj_func_num + 1):
            for j in range(dim_new):
                if i != i_gen and j != j_gen:
                    simplex_table[i, j] += simplex_table[i, j_gen] * simplex_table[i_gen, j]

        for j in range(dim_new):
            if j != j_gen:
                simplex_table[i_gen, j] *= simplex_table[i_gen, j_gen]

        i_used = -1

        for i in range(m * n):
            if answer_vector[i] == i_gen + 1:
                i_used = i

        if answer_vector[j_gen - 1] == 0:
            answer_vector[j_gen - 1] = i_gen + 1
            if i_used != -1:
                answer_vector[i_used] = -j_gen
        elif answer_vector[j_gen - 1] > 0:
            for i in range(m * n):
                if answer_vector[i] == -j_gen:
                    answer_vector[i] = i_gen + 1
                    answer_vector[j_gen - 1] = -j_gen
                    break
                elif answer_vector[i] == j_gen:
                    answer_vector[i] = -j_gen
                    break
        elif answer_vector[j_gen - 1] < 0:
            for i in range(m * n):
                if answer_vector[i] == i_gen + 1:
                    answer_vector[i] = answer_vector[j_gen - 1]
                    break
            answer_vector[j_gen - 1] = i_gen + 1

        print(answer_vector)
        print(simplex_table)
        print("\n")

    return simplex_table, answer_vector
