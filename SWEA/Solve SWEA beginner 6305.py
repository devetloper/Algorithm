given_list = [12,24,35,24,88,120,155,88,120,155]

def remove_overlap(x):
    no_overlap_list = []
    for i in x:
        if i not in no_overlap_list:
            no_overlap_list.append(i)
    return no_overlap_list

print(remove_overlap(given_list))
