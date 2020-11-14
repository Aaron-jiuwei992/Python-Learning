"""在循环中将十进制数123转换为二进制"""
number = 123
li = []
while number != 0:
    y = number % 2 
    li.append(y)
    number //= 2
    
str1 = ""
li_size = len(li)
for i in range(li_size-1,0,-1):
    str1 += str(li[i])
print(str1)