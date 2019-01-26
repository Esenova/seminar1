from myclass import SumTwoNumbers

num_1 = int(input("Please, enter the first num: "))
num_2 = int(input("Please, enter the second num: "))

cl_sum = SumTwoNumbers(num_1, num_2)
print('Sum of two numbers is: {}'.format(cl_sum.get_sum()))
