from collections import deque
import math
import copy

def solution(input):
    q = deque()
    visited = []
    answers=[]
    numba = int(input)
    y = int(math.log2(numba))
    # print("Line 11: ", "number =", numba, ", y =", y, ", 2**y =",2**y)
    if 2**y == numba:
        return y
    a = {"number": numba, "num_of_moves": 0}
    q.append(a)
    while q:
        x = q.pop()
        d = copy.deepcopy(x)
        # print("line18: ", "value =", x)
        # print("line19: ", "queue =", q)
        # print("line20: ", "visited = ", visited)
        # print("line 21:",d in visited)
        if d["number"] == 1:
            answers.append(d["num_of_moves"])
        elif d["number"]%2 == 0:
            # print("Line 22: even")
            while d["number"]%2 == 0:
                d["number"]=int(d["number"]/2)
                d["num_of_moves"] +=1
                # print("line 26: d =", d)
            
            if d not in visited:
                q.append(d)
                visited.append(d)
        else:
            # print('Line 39: odd')
            b={}
            c={}
            b["number"]=x["number"]+1
            b["num_of_moves"]=x["num_of_moves"]+1
            c["number"]=x["number"]-1
            c["num_of_moves"]=x["num_of_moves"]+1
            # print("line 42: b and c in visited", b in visited, c in visited)
            if b not in visited:
                q.append(b)
                visited.append(b)
            if c not in visited:
                q.append(c)
                visited.append(c)
        # print("line 51:", "answers = ", answers)
    
    return min(answers)

print(solution("98798671555555555555555555555555529666666666666666666666666666666666666666666666666666667777777777777777777777777777777777777777777777777777777888888888888888844444444444444444444422222222222222222222222222222222222222222222222222222222222222224444444444444444444444411111111111111115555555555555555555555555"))


my_arr = []
for i in range(1,513):
    my_arr.append(solution(i))

my_arr1=my_arr[0:2]
print(my_arr1)
my_arr2=my_arr[1:4]
print(my_arr2)
my_arr3=my_arr[3:8]
print(my_arr3)
my_arr4=my_arr[7:16]
print(my_arr4)
my_arr5=my_arr[15:32]
print(my_arr5)
my_arr6=my_arr[31:64]
print(my_arr6)
my_arr7=my_arr[63:128]
print(my_arr7)
my_arr8=my_arr[127:256]
print(my_arr8)
my_arr9 = my_arr[255:512]
print(my_arr9)

# print(solution(100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000100000000000000000000))