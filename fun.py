def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))



def palimdrom(n):
    s=str(n)
    m=int(s[::-1])
    if n==m:
        return True
    else:
        return False
print(palimdrom(234))