"""选择排序"""

# 使用for循环写选择排序
numbers = [5,3,7,1,4]
print(numbers)
numbers_size = len(numbers)
for i in range(numbers_size-1):
    min_index = i
    for j in range(i+1,numbers_size):
        if numbers[j] < numbers[min_index]:   # 这里min_index会重新更新的，所以numbers[min_index]并不是始终是5，它的变化过程是：3,1。
            min_index = j
    if min_index != i:
        numbers[i],numbers[min_index] = numbers[min_index],numbers[i]
    print(numbers)
        
        

# 使用while循环写选择排序

numbers = [5,3,7,1,4]
print(numbers)
numbers_size = len(numbers)
index = 0
while index < numbers_size-1:
    index_min = index
    index_ = index
    
    while index_ < numbers_size:
        if numbers[index_] < numbers[index_min]:
            index_min = index_
        index_ += 1
        
    if index_min != index:
        numbers[index],numbers[index_min] = numbers[index_min],numbers[index]
        print(numbers)    
        
    
    index += 1

    



















