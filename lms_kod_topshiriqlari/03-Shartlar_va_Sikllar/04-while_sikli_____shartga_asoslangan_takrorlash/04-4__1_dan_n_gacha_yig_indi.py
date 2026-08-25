# n beriladi.
# while yordamida 1+2+...+n yig‘indisini topib chiqar.

n = int(input())
yigindi = 0
i = 1
while i <= n:
    yigindi += i
    i += 1
print(yigindi)