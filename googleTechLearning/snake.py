# Feel free to change anything in this code, e.g.
# add or remove variables and functions. If you don't
# like it, you can delete it and start from scratch.

import sys

n = int(sys.stdin.readline())
snake = []
for i in range(0, n):
    my_list = []
    for j in range(0, n):
        if i % 2 == 0:
            my_list.append(i * n + j + 1)
        else:
            my_list.append((i+1) * n - j)
        my_list
    snake.append(' '.join(map(str, my_list)))
print('\n'.join(map(str, snake)))  # ... Modify this.
# ... Add more code.