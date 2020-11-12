"""冒泡排序"""


numbers = [9,5,11,7]
number_size = len(numbers)
index = 0
while index < number_size-1:
    index_ = 0
    is_sorted = False
    while index_ < number_size-1-index:
        if numbers[index_] > numbers[index_+1]:
            numbers[index_],numbers[index_+1] = numbers[index_+1],numbers[index_]        
            tmp = True    
        index_ +=1
    if not is_sorted:
        break
    print(numbers)
    index += 1
    