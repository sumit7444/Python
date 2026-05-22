print("Ashutosh Kumar")
for num in range(1,1001):
    temp=num
    reverse_num=0
    while temp>0:
        digit=temp%10
        reverse_num=reverse_num*10+digit
        temp=temp//10
    if num==reverse_num,
        print(num)
