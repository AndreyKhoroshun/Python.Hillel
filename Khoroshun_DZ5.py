value = 564000000784000000007
symbol = 0
my_value = str(value)
my_symbol = str(symbol)
count = my_value.count(my_symbol)
print(count)
#######################################
value = 5640007840000000
symbol = 0
my_list = []
my_value = str(value)
my_str = my_value[::-1]
for symbol in my_str:
    if int(symbol) == 0:
        my_list.append(symbol)
    else:
        break
print(len(my_list))
########################################
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for value in my_list_1:
    if value % 2 == 0:
        my_result.append(value)
for value in my_list_2:
    if value % 2 != 0:
        my_result.append(value)
print(my_result)
########################################
my_list = [1, 2, 3, 4]
new_list = []
new_list.extend(my_list)
new_list.pop(0)
new_list.append(my_list[0])
print(new_list)
########################################
my_list = [1, 2, 3, 4]
my_list.append(my_list[0])
my_list.pop(0)
print(my_list)
########################################
my_str = "43 больше чем 34 но меньше чем 56"
new_list = my_str.split()
my_list = []
for symbol in new_list:
    if symbol.isnumeric():
        my_list.append(int(symbol))
print(sum(my_list))
#########################################
my_str = "abcde"
my_list = []
new_list = ["_"]
if len(my_str) % 2 != 0:
    my_str += "_"
print([my_str[i:i + 2] for i in range(0, len(my_str), 2)])
##########################################
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
l_limit = my_str.index(l_limit)
r_limit = my_str.index(r_limit)
sub_str = (my_str[l_limit+1:r_limit])
print(sub_str)
##########################################