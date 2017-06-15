

# def hanoi(height, left='left', right='right', middle='middle'):
# 	if height:
# 		hanoi(height - 1, left, middle, right)
# 		print(left, '=>', right)
# 		hanoi(height - 1, middle, right, left)


# Trying to make this less confusing
def hanoi(height, src='left', dest='right', through='middle'):
	if height:
		# print("1", height-1, src, through, dest)
		hanoi(height - 1, src, through, dest)
		print(src, '=>', dest)
		# print("2", height-1, src, dest, through)
		hanoi(height - 1, through, dest, src)


hanoi(3)