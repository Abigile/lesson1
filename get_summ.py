
def get_summ(one,two,delimiter='&'):
	return str(one) + delimiter + str(two)

one = 'learn'
two = 'python'

sum_string = get_summ(one,two).upper()

print(sum_string)