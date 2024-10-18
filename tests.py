def print_n(x, n):
    if x == n:
        print(x)
        return
    print(x)
    if x < n:
        print_n(x+1, n)
    else:
        print_n(x-1, n)
print_n(1, int(input()))

def print_n(a, b):
    if a == b:
        print(a)
        return
    print(a)
    if a < b:
        print_n(a+1, b)
    else:
        print_n(a-1, b)
print_n(int(input()), int(input()))
numb = int(input())
lst_numb = 1
result = ""

def count(numb, lst_numb):
    global result
    if lst_numb > numb:
        result = "NO"
    else:
        if lst_numb == numb:
            result = "YES"
        else:
            lst_numb *= 2
            count(numb, lst_numb)

count(numb, lst_numb)
print(result)
def rec(x):
    if x < 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
        print (x)
        rec (x+x)
rec(1)
