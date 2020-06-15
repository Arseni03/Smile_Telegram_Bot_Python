a,b,c,d = map(int, input().split())
def minimum(a,b,c,d):
    min=a
    if min>b:
        min=b
    if min>c:
        min=c
    if min>d:
        min=d
    return min
print(minimum(a,b,c,d))