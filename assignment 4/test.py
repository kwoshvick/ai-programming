a1 = {'a':150, 'b':13, 'd':45, 'c':200, 'e':30}
from collections import OrderedDict

sorted_dictionary = OrderedDict(sorted(a1.items(), key=lambda v: v[1], reverse=True))

print(sorted_dictionary)

n=3
firstNpairs = {k: sorted_dictionary[k] for k in list(sorted_dictionary.keys())[:n]}
print(firstNpairs.values())