# Recursive Approach
def func(n):
    if n == 1 or n == 2:
        return n+1
    return func(n-1)+func(n-2)


# Dynamic Programming Approach
def func(n):
    mp = [0]*(n+1)
    mp[1] = 2
    mp[2] = 3
    for i in range(3, n+1):
        mp[i] = mp[i-1]+mp[i-2]
    return mp[n]


n = int(input("Enter the Number : "))
r = func(n)
print(r)