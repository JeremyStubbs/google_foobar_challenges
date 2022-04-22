from collections import deque

def solution(src, dest):
    #Make board
    xaxis = [x for x in range(8)]
    yaxis = [x for x in range(8)]
    board = []
    for i in xaxis:
        for j in yaxis:
            board.append([i, j])
    my_dict ={}
    for i in range(len(board)):
        my_dict[i]= board[i]

    # Initializing a queue
    q = deque()
    visited = deque()
    q.append(src)
    visited.append(src)

    #Initialize Counter
    Count = 0
    last_value =src
    
    while q:
        val = q.popleft()

        if val == dest:
            return Count

        new_x_positions = [my_dict[val][0]+2, my_dict[val][0]-2, my_dict[val][0]+1, my_dict[val][0]-1]
        new_y_positions = [my_dict[val][1]+2, my_dict[val][1]-2, my_dict[val][1]+1, my_dict[val][1]-1]

        if new_x_positions[0] <=7 and new_x_positions[0] >=0:
            if new_y_positions[2] >=0 and new_y_positions[2] <=7:
                a = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[0],new_y_positions[2]])]
                if a not in visited:
                    q.append(a)
                    visited.append(a)
            if new_y_positions[3] >=0 and new_y_positions[3] <=7:
                b = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[0],new_y_positions[3]])]
                if b not in visited:
                    q.append(b)
                    visited.append(b)

        if new_x_positions[1] <=7 and new_x_positions[1] >=0:
            if new_y_positions[2] >=0 and new_y_positions[2] <=7:
                a = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[1],new_y_positions[2]])]
                if a not in visited:
                    q.append(a)
                    visited.append(a)
            if new_y_positions[3] >=0 and new_y_positions[3] <=7:
                b = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[1],new_y_positions[3]])]
                if b not in visited:
                    q.append(b)
                    visited.append(b)

        if new_y_positions[0] <=7 and new_y_positions[0] >=0:
            if new_x_positions[2] >=0 and new_x_positions[2] <=7:
                a = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[2],new_y_positions[0]])]
                if a not in visited:
                    q.append(a)
                    visited.append(a)
            if new_x_positions[3] >=0 and new_x_positions[3] <=7:
                b = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[3],new_y_positions[0]])]
                if b not in visited:
                    q.append(b)
                    visited.append(b)
        if new_y_positions[1] <=7 and new_y_positions[1] >=0:
            if new_x_positions[2] >=0 and new_x_positions[2] <=7:
                a = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[2],new_y_positions[1]])]
                if a not in visited:
                    q.append(a)
                    visited.append(a)
            if new_x_positions[3] >=0 and new_x_positions[3] <=7:
                b = list(my_dict.keys())[list(my_dict.values()).index([new_x_positions[3],new_y_positions[1]])]
                if b not in visited:
                    q.append(b)
                    visited.append(b)
        if val == last_value:
            Count= Count + 1
            last_value = q[-1]

            
