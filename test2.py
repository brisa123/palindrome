
from collections import Counter

my_list=[1,2,3,5,3,2,3,4,1,3,5,3]

my_str="i am a girl, very common girl, looking like a girl.".split()

list_counter=Counter(my_list)
str_counter=Counter(my_str)
print(type(list_counter),type(str_counter))
print((list_counter),(str_counter))
print(list_counter.most_common(2))
print(str_counter.most_common(2))