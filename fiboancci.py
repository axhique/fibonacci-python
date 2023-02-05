first_num = 0
second_num = 1
print (first_num ,second_num,end=' ')

for i in range(10):
    sum = first_num + second_num
    first_num = second_num
    second_num = sum
    print (sum ,end=' ')