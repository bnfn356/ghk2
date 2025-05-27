def factor_3or5(n):
    if n%3==0 or n%5==0:
        return True
    else:
        return False
sum=0
for i in range(1, 10):
    if (factor_3or5(i)):
        print(f'checking {i}')
        sum+=i
        print(sum)
print(sum)
