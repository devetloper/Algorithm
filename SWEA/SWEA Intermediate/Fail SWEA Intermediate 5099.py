### Insert fake pizza to keep list size same, But still ot wrong answer in last case.
### Have to fix make pizza function or take_out_oven function. Not sure which one.
 
### function that convert ci to count(how many cycle pizza can run)
def convert_count(ci):
    
    n = 0
    while True:
        if 2**n <= ci < 2**(n+1):
            return (n+1)
        
        else:
            n += 1
### make pizza functions ###
def put_in_oven():
    if len(pizza_list) != 0 and 0<= len(oven) < n:
        pizza = pizza_list.pop(0)
        oven.insert(0,pizza)


def take_out__oven():
    pizza = oven.pop(0)
    pizza_dict[pizza] -= 1
    
    
    if pizza_dict[pizza] == 0:
        out_pizza.append(pizza)
        put_in_oven()
    
    else:
        oven.insert(0,pizza)

def turn_oven():
    pizza = oven.pop(0)
    oven.append(pizza)

def make_pizza():
    for _ in range(n):
        put_in_oven()
    while len(oven) == n:
        take_out__oven()
        turn_oven()
    
    return out_pizza[-1]

### input ###
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().rstrip(" ").split(" "))
    pizza_ci_str = input().split(" ")
    pizza_ci = [convert_count(int(pizza_ci)) for pizza_ci in pizza_ci_str if pizza_ci != ""]

    pizza_dict = {i+1 : pizza_ci[i] for i in range(m)} #pizza number: cheese

    for i in range(n-1):                 #fake pizza which doesn't melt in case for put in empty pizza
        pizza_dict[101+i] = 11111+i
    
    oven = []
    pizza_list = [key for key in pizza_dict] # pizza to put in
    out_pizza=[]

    print(make_pizza())
    




 
