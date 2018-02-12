def SimpleArraySum(n,ar):
    Sum = 0
    for i in range(n):
        Sum = Sum + ar[i]
    return Sum
n = int(input().strip())
ar = list(map(int,input().strip().split(' ')))
result = SimpleArraySum(n,ar)
print(result)

