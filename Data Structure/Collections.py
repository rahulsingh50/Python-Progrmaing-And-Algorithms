'''
The collections module provides more specialized, high, performance alternatives for
the built-in data types as well as a utility function to create named tuples.

'''

from collections import deque
dq =deque('abc')
dq.append('d')
dq.appendleft('z')
dq.extend('efg')
dq.extendleft('yxw')
print(dq)

# loop
for i in dq:
    print(i)