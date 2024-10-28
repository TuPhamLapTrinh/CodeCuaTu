# bai 9
import math
def SCP(x):
	tmp=int(math.sqrt(x))
	if tmp * tmp == x : return True
	return False
a=int(input())
if SCP(a):
	print('True')
else:
	print('False')