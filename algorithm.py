def fibMax(n):
     a, b = 1, 1
     while b < n:
         a, b = b, a+b
     return a

def fiboChicken(n):
    if fibMax(n+1) == n:
        return fibMax(n)
    else:
        sub = n - fibMax(n)
        chicken = fiboChicken(fibMax(n)) + fiboChicken(sub)
        return chicken
