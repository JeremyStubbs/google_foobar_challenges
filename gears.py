import math
import numpy as np
from decimal import *
from fractions import Fraction

def solution(pegs):
    #Make input, variable(radiuses) and answer arrays
    my_targets = []
    answer = [-1,-1]
    my_length = len(pegs)
    if pegs[1]-pegs[0]<3:
        return answer
    if my_length ==2:
        z = (Decimal(pegs[1])-Decimal(pegs[0]))/Decimal(1.5)
        final = Fraction(z)
        answer = [final.numerator, final.denominator]
        return answer
    for i in range(1,my_length):
        distance = pegs[i]-pegs[i-1]
        if distance<2:
            return answer
        my_targets.append(distance)
    my_targets.append(0)
    # print('targets', my_targets)

    #Make matrix of known relationships between gears
    my_matrix = np.zeros([my_length,my_length], dtype=int)
    for i in range(my_length):
        for j in range(my_length):
            if i==my_length-1:
                if j == 0:
                    my_matrix[i,j]=1
                elif j==my_length-1:
                    my_matrix[i,j]=-2
            else:
                if j==i or j==(i+1):
                    my_matrix[i,j] = 1
    # print('matrix',my_matrix)

    #Solve
    radiuses = np.linalg.solve(my_matrix,my_targets)
    # print('radiuses', radiuses)

    #Compose answer
    if all(x>=1 for x in radiuses):
        first_radius = radiuses[0]
        first_as_int = int(first_radius)
        next_var = math.floor((first_radius-first_as_int) * 10 ** 6) / 10 ** 6
        # print('haha', next_var)
        if next_var == 0.666666:
            subsequent_var = first_as_int*3+2
            answer = [subsequent_var, 3]
            return answer
        elif next_var == 0.333333:
            subsequent_var = first_as_int*3+1
            answer = [subsequent_var, 3]    
        else:
            answer = [first_as_int, 1]
    return(answer)

print('answer 1',solution([4,30,50]))
print('answer 2',solution([4,17,50]))
print('answer 3',solution([1,5]))
print(solution([1,5,8,11]))