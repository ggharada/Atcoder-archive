n = int(input())

if n < 42:
    if len(str(n)) == 1:
        print("AGC00" + str(n))
    else:
        print("AGC0" + str(n))
else:
    print("AGC0" + str(n + 1))