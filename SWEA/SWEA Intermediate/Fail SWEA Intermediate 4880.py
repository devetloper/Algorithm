### grouping student ###
tor_list = []
def half(i,j):
    if i == j:
        tor_list.append(j)
    
    elif j -i ==1:
        tor_list.append([i,j])
    
    else:
        half(i,(i+j)//2)
        half((i+j)//2 + 1, j)

    return tor_list
    
def half_clear(i,j):
    tor_list.clear()
    return half(i,j)

### Do rcp function ###
def rcp(list):
    man1, man2 = list
    if card_dict[man1] == card_dict[man2]:
        return man1
    
    elif card_dict[man1] ==1 and card_dict[man2] ==3:
        return man1

    elif card_dict[man1] > card_dict[man2]:
        return man1
    
    else:
        return man2

### make mathcing function ###


def match(gr_list):
    if type(gr_list[0]) == int and type(gr_list[1]) == int:
        return rcp(gr_list)
    
    else:
        for group in gr_list:
            if type(group) == list:
                idx = gr_list.index(group)
                gr_list.remove(group)
                gr_list.insert(idx,rcp(group))
        if gr_list == [1,5]:
            return 3
        else:
            return match(regroup(gr_list))
            

### make regroup function ### ex) convert [1,3,5,6] to [[1,3],[5,6]]

def regroup(re_list):

    len_li =len(re_list)
    group_li = half_clear(1,len(re_list)) 
    for group in group_li:

        if type(group) == list:
            re_list.append([re_list[group[0]-1],re_list[group[1]-1]])
        
        else:
            re_list.append(re_list[group-1])


    re_list = re_list[len_li:]
    return re_list

### input ###
n = int(input()) #number of student

cards = input().split(" ")

card_dict = {}
card_dict = {i : int(cards[i-1]) for i in range(1,n+1)}

groups = half_clear(1,n)

print(match(groups))



