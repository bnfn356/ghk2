def is_even(n):
    if n%2==0:
        return True
    else:
        return False
first=1
second=2
sum=0
while (first<40):
    if is_even(first):
        sum+=first
    new=first+second
    first=second
    second=new
print(f'first is {first} and sum of them is {sum}')
