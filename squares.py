import math
from itertools import repeat

def solution(area):
    # Your code here
    answer = []
    while True:
        x = int(math.sqrt(area))
        if x <= 1:
            break
        answer.append(x*x)
        area = area-x*x
        if area ==0:
            break
        
    answer.extend(repeat(1,area))
    return answer
        

print(solution(12))