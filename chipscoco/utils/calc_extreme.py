"""
@author = maoshaonan
@email = 1556902689@qq.com
@desc = caculate the max value and the extreme value of four numbers! 
@filename = calc_extreme.py
"""
import random
import algorithm


def max_medium(w,x,y,z,t):
    max_,max_second,min_second,min_ = algorithm.calc_extreme_of_4_numbers(w, x, y, z, )
    if t > max_:
        max_medium = max_second
    elif t > max_second:
        max_medium = max_second
    elif t > min_second:
        max_medium = t
    else:
        max_medium = min_second
    return max_medium
    
    
if __name__=="__main__":
    w,x,y,z,t = random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000),random.randint(1,1000)
    print("{} {} {} {} {}\n the max_med5 value is {}!".format(w,x,y,z,t,max_medium(w,x,y,z,t)))