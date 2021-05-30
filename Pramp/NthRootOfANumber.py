def root(x, n: int):
    left = 0
    right = x
    return bisection(x, n, left, right)


# method that cal the root between the interval [left, right] by getting the middle item
def bisection(x, n, left, right):
    mid = (left + right) / 2
    print(mid)
    fmid = pow(mid, n)

    # if |mid^n - x| is close to zero then return 
    if abs(fmid - x) < 0.001:
        return mid
    
    if fmid > x:
        return bisection(x, n, left, mid)
    
    return bisection(x, n, mid, right)

print(root(7, 5))