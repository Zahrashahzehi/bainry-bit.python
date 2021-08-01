n = int(input())
bainary = list(input())
f=bainary.count("1")
count = 0
while f > 1:
    count = count +1
    f=f-1
print(count)     