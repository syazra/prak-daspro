def div(x, y):
    if abs(x) < abs(y):
        return 0
    elif x == 0 or y == 0:
        return 0
    elif (x < 0 and y > 0) or (x > 0 and y < 0):
        return div(x + y, y) - 1
    else:
        return div(x - y, y) + 1

print(div(12, 6))   # -> 2
print(div(-12, 6))  # -> -2
print(div(12, -6))  # -> -2
print(div(-12, -6)) # -> 2

def exp(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / x * exp(x, y + 1)
    else:
        return x * exp(x, y - 1)
    
print(exp(3, 6))   # -> 729
print(exp(3, -1))  # -> 0.33333333333
print(exp(-3, 3))  # -> -27
print(exp(6, 0))   # -> 1
