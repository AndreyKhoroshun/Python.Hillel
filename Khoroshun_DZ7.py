from random import randint
my_list = [randint(1, 100) for i in range(20)]
print(my_list)
############################################################
import random
triangle = dict(A=(random.randrange(200), random.randrange(200)),
                B=(random.randrange(200), random.randrange(200)),
                C=(random.randrange(200), random.randrange(200)))
print(triangle)
#############################################################
my_str = "I'm the string"
def my_function(my_str):
    print("***" + my_str + "***")
my_function(my_str)
#############################################################
