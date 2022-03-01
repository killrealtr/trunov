def dot_product(a,b):
    s=0
    for i in range(3):
        s+=a[i]*b[i]
    return s
a=list(map(int, input().split()))
b=list(map(int, input().split()))
print('(a,b)=',dot_product(a, b))