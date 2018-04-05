def factorial(fact):
    total=1
    while(fact>1):
        total*=fact
        fact=fact-1
    return total
n = int(input())
lis = []
sum=1
for i in range(n):
    lis.append(input())
lis.sort()
test = input()
for i in range(0,n):
    variab=lis.index(test[i])
    sum+=factorial(n-1-i)*variab
    lis.pop(variab)
print(sum)