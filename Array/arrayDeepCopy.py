import array as arr
import copy
a = arr.array('i', [110, 220, 330, 440, 550])
b = copy.deepcopy(a)
print("Copied array:",b)