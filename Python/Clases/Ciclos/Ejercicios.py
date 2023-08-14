# # #1. excribir u programa que pida una palabra y la muestre diez veces

# # # word= input("Ingrese una palabra ")
# # # for i in range(10):
# # #     print(word)

# # #2

# # # age = int(input("Ingrese su edad "))
# # # for i in range(1,age+1):
# # #     print(i)

# # #3

# # num=int(input("Ingrese un numero entero positivo "))

# # for i in range(1,num+1):
# #     if i%2 !=0:
# #         if i == num or i == num-1:
# #             print(i)
# #         else:
# #             print(i, end=",")

# #4

# num=int(input("Ingrese un numero entero positivo "))

# for i in range(num,-1,-1):
#     if i== 0:
#         print(i)
#     else:
#         print(i, end=",")

#5

num=int(input("Ingrese un numero entero positivo "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end="")   
    print("")     