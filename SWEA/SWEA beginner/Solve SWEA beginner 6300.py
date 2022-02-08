given_list = [12, 24, 35, 70, 88, 120, 155]

even_idx_list = [given_list[i] for i in range(len(given_list)) if i % 2 == 1]

print(even_idx_list)