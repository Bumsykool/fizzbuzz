
def fizzbuzz(arg):

	if arg % 3 == 0 and arg % 5 ==0:
		print("fizzbuzz")
	elif arg % 5 ==0:
		print ("buzz")
	elif arg % 3 == 0:
		print ("fizz")
	else:
		print (arg)

print (fizzbuzz(15))