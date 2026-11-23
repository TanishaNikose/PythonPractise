# Implement a function that calculates the sum of even numbers in a list using recursion

# # without recursion
# list1 = [1,2,3,4,5,6]
# sum = 0

# for i in list1:
#     if i % 2 == 0:
#         sum = sum + i

# print(sum)

# # With Recursion --> finding the sum of the list element

# def fun_sum(list1):
#     if list1 == []:
#         return 0
#     else:
#         return list1[0] + fun_sum(list1[1:]) 

# with recursion - finding the sum of the even Numbers in the list
def fun_sum(list1):
    if list1 == []:
        return 0
    else:
        if list1[0] % 2 == 0:
            return list1[0] + fun_sum(list1[1:]) 
        else:
            return fun_sum(list1[1:]) 

print(fun_sum([1,2,3,4]))
















