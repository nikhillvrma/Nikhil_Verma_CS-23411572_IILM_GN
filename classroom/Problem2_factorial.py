# Recursive Approach
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)



# Dynamic Programming
def factorial(n):
    mp = [0]*(n+1)
    mp[0] = 1
    mp[1] = 1
    for i in range(2, n+1):
        mp[i] = i*mp[i-1]
    return mp[n]

n = int(input("Enter the Number : "))
r = factorial(n)
print(r)