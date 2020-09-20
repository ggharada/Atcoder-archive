n = int(input())
sum_ = 0

def prime_check(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i  in range(1,n+1):
    sum_ += i

if prime_check(sum_):
    print("WANWAN")
else:
    print("BOWWOW")