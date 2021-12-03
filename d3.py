from aoc import get_input
list = get_input(3).splitlines()

def p1():
    gamma = ""
    for i in range(len(list[0])):
        count = 0
        for j in list:
            if j[i] == "1":
                count +=1

        if count * 2 > (len(list)):
            gamma += "1"
        else:
            gamma += "0"

    epsilon = int("".join(['1' if num == '0' else '0' for num in gamma]),2)
    gamma = int(gamma, 2)

    return epsilon * gamma

def p2(l, first, second):
    tmp = ["" for i in range(len(l[0]))]
    rate = []
    
    for i in range(len(l[0])):
        for j in l:
            tmp[i] += j[i]

    for i in tmp:
            count = i.count("1") 
            print(count)

            if count*2 < len(i):
                rate += first
            else:
                rate += second

    return int("".join(rate), 2)
                
print(p2(list, "1", "0") * p2(list, "0", "1"))
