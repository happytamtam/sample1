#1
max_number = 101
sum_number = 0
for i in range(1, max_number):
    sum_number += i
print("#1")
print(sum_number)

#1'
output = sum(range(1, 101))
print("#1'")
print(output)

#2
total = 0
max_number = 1001
for i in range(1, max_number):
    if i % 7 == 0 or i % 13 == 0:
        total += i
print("#2")
print(total)

#2'
output2 = sum(i for i in range(1, 1001) if i % 7 == 0 or i % 13 ==0)
print("#2'")
print(output2)




