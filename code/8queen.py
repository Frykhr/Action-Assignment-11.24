def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result

def solve_queens(num, x, y):
    count = 0
    for solution in queens(num):
        if solution[y-1] == x-1:
            count += 1
    return count

x, y = map(int, input().split())
count = solve_queens(8, x, y)
print(count)
