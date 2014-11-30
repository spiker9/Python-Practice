import os
print('ad')
def search(x):
	print('method start')
	x = os.listdir('.')
	for a in x:
		print(a)
search(1)