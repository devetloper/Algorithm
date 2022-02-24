# Run without error but wrong answer. Have to fix make pizza fuction

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
    if len(oven) >= n:
        print("Oven full")
    elif len(pizza_list) != 0:
        pizza = pizza_list.pop(0)
        oven.insert(0,pizza)
    else:
        print("No pizza")

def take_out__oven():
    pizza = oven.pop(0)
    pizza_dict[pizza] -= 1
    
    if pizza_dict[pizza] == 0:
        if len(pizza_list) != 0:
            put_in_oven()
    
    else:
        oven.insert(0,pizza)

def turn_oven():
    pizza = oven.pop(0)
    oven.append(pizza)

### input ###
n, m = map(int,input().rstrip(" ").split(" "))
pizza_ci_str = input().split(" ")
pizza_ci = [convert_count(int(pizza_ci)) for pizza_ci in pizza_ci_str if pizza_ci != ""]

pizza_dict = {i+1 : pizza_ci[i] for i in range(m)} #pizza number: cheese

oven = []
pizza_list = [key for key in pizza_dict] # pizza to put in

def make_pizza():
    while len(oven) < n:
        put_in_oven()
    while len(oven) != 1:
        take_out__oven()
        turn_oven()
    return oven[0]

print(make_pizza())

