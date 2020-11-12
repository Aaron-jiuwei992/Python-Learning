"""
@author = maoshaonan
@email = 1556902689@qq.com
@desc = caculate the extreme value of numbers! 
"""
import random


def calc_extreme_of_2_numbers(x, y):
    if x > y:
        max_ = x
        min_ = y
    else:
        max_ = y
        min_ = x
    return max_,min_


def calc_extreme_of_3_numbers(x, y, z):
    max_,min_ = calc_extreme_of_2_numbers(x, y)
    if z > max_:
        max_ = z
    if z < min_:
        min_ = z
    medium = x+y+z-max_-min_
    return max_,min_,medium 


def calc_extreme_of_4_numbers(w, x, y, z, ):
    max_,min_,medium = calc_extreme_of_3_numbers(x, y, z)
    if w > max_:
        max_second = max_
        max_ = w
    elif w > medium:
        max_second = w
    else:
        max_second = medium
    
    #求四个变量中的最小值
    if w < min_:
        min_ = w
        
    #求四个变量中的次小值
    min_second = w+x+y+z-max_-min_-max_second
    return max_,max_second,min_second,min_   

"""
if __name__=="__main__":
    w,x,y,z = random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000)
    max_,max_second,min_second,min_ = calc_extreme_of_4_numbers(w,x,y,z)
    print("{}\t{}\t{}\t{}".format(max_,max_second,min_second,min_))
"""


"""在循环中同时计算最大值，次大值，次最小值，最小值,和，平均值"""



def stastic_value_of_numbers_in_loop(numbers):
    max_ = min_ = max_second = min_second = numbers[0]
    sum_numbers = numbers[0]
    average = 0
    numbers_size = len(numbers)
    index = 1
    while index < numbers_size:
        
        # 如果number比上次循环的最大值要大，最大值就是number，那么次大值就是上次循环的最大值
        
        if numbers[index] > max_:
            max_second = max_
            max_ = numbers[index]
                              
        # 如果number比上一次循环的最大值要小，最大值就是上次循环的最大值，而其又大于次大值，那么次大值就是number
        elif numbers[index] > max_second:
             max_second = numbers[index]
        
        # 如果number小于max_，也小于max_second,而又假设max_和max_second相等，那么（只需要）更新次大值为number
        elif max_ == max_second:
           max_second = numbers[index]
           
        if numbers[index] < min_:
            min_second = min_
            min_ = numbers[index]
        
        elif numbers[index] < min_second:
            min_second = numbers[index]
            
        elif min_ == min_second:
            min_second = numbers[index]


        sum_numbers += numbers[index]
        average = sum_numbers / len(numbers)
        
        index += 1
        
        
        
    return max_,max_second,min_second,min_,sum_numbers,average
    

#求少数变量中的最大值，次大值，次小值，最小值


def stastic_value_of_numbers_in_loop(numbers):
    max_ = min_ = max_second = min_second = numbers[0] 
    if numbers[0] < numbers[1]:
        max_ = numbers[1]
        min_ = numbers[0]
    else:
        max_ = numbers[0]
        min_ = numbers[1]
        
    if numbers[2] > max_:
        max_ = numbers[2]
    if numbers[2] < min_:
        min_ = numbers[2]
        
    max_second = medium = numbers[0]+numbers[1]+numbers[2]-max_-min_
        
        
    
    for number in numbers[3:]:
        #如果number比上次最大值还要大，那么最大值就是number，次大值就是上次的最大值。
        if number > max_:
            max_second = max_ 
            max_ = number
        #如果number比上次的最大值小，又大于次大值，那么次大值肯定就是number。
        elif number > max_second:
            max_second = number        
       
        if number < min_:
            #如果number比上次最小值还要小，那么最小值就是number,次小值就是上次的最小值。
            min_second = min_ 
            min_ = number
        #如果number比上次的最小值大，又小于次小值，那么次小值肯定就是number。
        elif number < min_second:
            min_second = number
       
        
    return max_,max_second,min_second,min_



#随机数范围是【1，10000】，产生一百亿个随机数，求里面最大值，次大值，次小值，最小值。

import random


def stastic_value_of_numbers():
    max_ = max_second = min_second = min_ = random.randint(1,10000)

    
    for _ in range(10**10):
        
        
        number = random.randint(1,10000)    
        if number > max_:
            max_second = max_
            max_ = number

        elif number > max_second:
            max_second = number
                
            
        elif max_ == max_second:
            max_second = number
                
        if number < min_:
            min_second = min_
            min_ = number

        elif number < min_second:
            min_second = number
                
            
        elif min_ == min_second:
            min_second = number

        
        

    return max_,max_second,min_second,min_

"""
if __name__ == "__main__":
    print("{}".format(stastic_value_of_numbers()))
"""



#实现动态哈希算法
"""
data_machines = ["192.168.1","192.168.2", "192.168.3"]

nodes = []
for machine in data_machines:
    nodes.append((hash(machine), {"ip_address": machine}))

print(nodes)

for i in (len(nodes)-1):
    exchange = False
    for j in (len(nodes)-1-i):
        if nodes[j][0] > nodes[j+1][0]:
            nodes[j][0],nodes[j+1][0] = nodes[j+1][0],nodes[j][0]
            exchange = True
    if not exchange:
        break
print(nodes)

for data_machine in data_machines:
    hash_value = hash(data_machine)
    if hash_value == nodes[][]

"""

















































#求100以内的所有素数


def is_prime_number():

    numbers = [x for x in range(2,101)]
    
    for number in numbers:
    
        is_prime = True
        
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:            
            print("{}".format(number),end = " ")

"""
if __name__=="__main__":
    is_prime_number()
     
"""

# 求一个列表里的中位数

def median(numbers):
    numbers.sort()
    numbers_size = len(numbers)
    if numbers_size % 2 == 0:
        median = (numbers[numbers_size//2]+numbers[numbers_size//2-1])/2
        print("{}".format(round(median,1)))
    else:
        median = numbers[(numbers_size-1)//2]
        print("{}".format(median))

"""
if __name__ == "__main__":
    numbers = []
    numbers.append(int(input("")))    # 怎么从键盘同时获取多个数值，然后填充到一个列表中？？？？
    
    median(numbers)
"""

















# 给你两个正整数a和b， 输出它们的最大公约数。
import random


def common_divisor(a,b):
    if a > b:
        a,b = b,a
    
    # 最大公约数肯定不会超过两个数中较小的数值
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            max_common_divisor = i
    return max_common_divisor

"""    
if __name__ == "__main__":
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("{}\t{}\n{}".format(a,b,common_divisor(a,b)))
"""

# 给你两个正整数a和b， 输出它们的最小公倍数。

import random


def common_multiple(a,b):
    if a < b:
        a,b = b,a
    
    # 最小公倍数肯定大于两个数中较大的数值，又小于等于二者之积。
    for i in range(a,a*b+1):
        if i % a == 0 and i % b == 0:
            min_common_multiple = i
            break
    return min_common_multiple

""" 
if __name__ == "__main__":
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("{}\t{}\n{}".format(a,b,common_multiple(a,b)))
"""

# 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
import random


def stastic_0(L):
    list1 = []
    for i in L:
        if i % 2 == 0 or i % 5 == 0:
            list1.append(i)
        
    product = 1
    for j in list1:
        product *= j

    count = 0
    while product % 10 == 0:
        
            count += 1
            product /= 10
    
    return count

"""
if __name__ == "__main__":
    L = [4, 2, 25, 7777777, 100, 3, 77777777, 77777777, 77777777, 77777777]
    print("{}".format(stastic_0(L)))
"""

# 给你一个整数a，数出a在二进制表示下1的个数，并输出，要求不能使用bin函数。

def counter(a):
    count = 0
    list1 = []
    while a != 0:
        list1.append(a % 2)
        a = a // 2
        
    for i in list1:
        count += i
    return count
  
"""  
if __name__ == "__main__":
    a = random.randint(1,100)
    print(a,bin(a))
    print(counter(a))
"""

# 给定一个字符串a, 将a中的大写字母转换成小写，其它字符不变，并输出。

def switch(a):
    a = list(a)
    b = ""
    for i in a:
        if i > "A" and i < "Z":
            i = chr(ord(i) + 32)
            b += i
        else:
            b += i
    return b

"""
if __name__ == "__main__":
    a = "KDJIskos234k,.;djfeiJ"
    print(switch(a))
"""

"""
给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。
若有多组解，输出它们之和最小的那组。注：所给数据都有解，不用考虑无解的情况。
"""






"""
计算所有自恋数的和
"""
def sum_of_shuixianhua():
    
    sum_of_numbers = 0
    
    for number in range(100,1000):

        if number == (number % 10)**3 + (((number // 10)) % 10)**3 + (number // 100)**3:
            print(number,end = " ")

            sum_of_numbers += number
    else:
        print(sum_of_numbers)

"""        
if __name__ == "__main__":
    sum_of_shuixianhua()
"""   


"""
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。

例如a="cagy", b=3, 

则输出 ：fdjb
"""

def slove_it(a,b):
    list1 = []
    for i in a:
        if ord(i)+b <=122:
            list1.append(chr(ord(i)+b))
        else:
            list1.append(chr(ord(i)+b-26))

if __name__ == "__main__":
    a = "cagy"
    b = 3
    slove_it(a,b)




























































