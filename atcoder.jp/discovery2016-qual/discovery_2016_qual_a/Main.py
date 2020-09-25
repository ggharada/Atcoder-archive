w = int(input())
a = "DiscoPresentsDiscoveryChannelProgrammingContest2016"

for i in range(51):
    print(a[i],end="")
    if (i+1) % w == 0:
        print()
if 51 % w != 0:
    print()