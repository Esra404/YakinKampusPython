# def greet():
#     print("hello esra!")
# print(greet())
# def add_numbers(num1,num2):
#     sum=num1+num2
#     print('sum: ',sum)

# print(add_numbers(4,5))

# def find_square(num):
#     result=num*num
#     return result
# square=find_square(3)
# print("square",square)
# def add_numbers(num1,num2):
#     sum=num1+num2
#     return sum
# result=add_numbers(5,4)
# print('sum',result)
# ------------------------------------------
# HAZIR BAZI FONKSİYONARk
# import math
# square_root=math.sqrt(4)
# print("square root of 4 is",square_root)
# power=pow(4,2)
# print("power")
def get_square(num):
    return num*num
for i in [1,2,3]:
    result=get_square(i)
    print('square of ',i,'=',result)