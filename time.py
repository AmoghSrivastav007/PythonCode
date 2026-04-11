"""What do we want
1. we want to evaluate the algorithms
2. we want to evaluate scalability
3. we want to evaluate in terms of input size"""



#1.Measuring time to execute
# import time

# start =  time.time()
# # for i in range(1,101):
# #      print(i)

# i = 1
# while(i<101):
#      print(i)
#      i+=1

# print("The time taken to execute the for loop is: ", time.time()-start)


"""Problem with this approach:-

# different time for different algorithms      Yes
# time varies if implementation changes        No
# different machines have different time       No
# does not work for extremely small inputs     No
# time varies for different inputs, but can't established a relationship     No"""




#2.Counting operations involved

# def c_to_f(c):
#     return c*9/5+32

# def mysum (x):
#     total = 0
#     for i in range(x+1):
#         total+=i
#     return total


# T=1+3x  (x=input)

"""Problem with this approach:-
# different time for different algorithms      Yes
# time varies if implementation changes        No
# different machines have different time       Yes
# no clear definition of which operation to count     No
# time varies for different inputs, but can't established a relationship     Yes
"""



# 3. order of growth


