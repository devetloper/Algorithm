#/// have to convert [1,2,3,5,6] to [[1,2],3,[5,6]]
### grouping student ###
tor_list = []
def half(i,j):
    if i == j:
        tor_list.append(j)
        return tor_list
    
    elif j -i ==1:
        tor_list.append([i,j])
        return tor_list
    
    else:
        half(i,(i+j)//2)
        half((i+j)//2 + 1, j)

    return tor_list

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

### input ###
n = int(input()) #number of student

cards = input().split(" ")

card_dict = {}
card_dict = {i : int(cards[i-1]) for i in range(1,n+1)}

###


def match(gr_list):
    for group in gr_list:
        if type(group) == list:
            idx = gr_list.index(group)
            gr_list.remove(group)
            gr_list.insert(idx,rcp(group))
    return gr_list

groups = half(1,n)

print(match(groups))



