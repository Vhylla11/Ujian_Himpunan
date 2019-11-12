def triangle(num):
	pat = input("Enter a character : ")
	for i in range(1, num+1):
		for r in range(1, num+1):
			if r <= (num - i):
				print(end=' ')
			else:
				print(pat, end=' ')
		print()
triangle(int(input("Enter size : ")))


