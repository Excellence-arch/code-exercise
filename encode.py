def encode(string_to_be_encoded, is_case_sensitive):
	answer = []
	c = []
	alpha = 'qwertyuiopasdfghjklzxcvbnm'
	count = 0
	if is_case_sensitive:
		for i in alpha:
			for j in string_to_be_encoded:
				if i == j:
					count += 1
					b = [i,  count]
					answer.append(b)
			count = 0
		return answer
	else:
		for i in alpha:
			for j in string_to_be_encoded:
				if i == j.lower():
					count += 1
					b = [i,  count]
					answer.append(b)
			count = 0
		return answer


print(encode('wwwaaad', True))


import random
def generateNumber():
	return random.randrange(1,24)

def init():
	num = []
	for i in range(5):
		a = generateNumber()
		num.append(a)
	if sum(num) <= 25:
		for i in num:
			print(i, end=' ')
	else:
		init()

init()


import math
def perfectSquare(num):
	if (math.sqrt(num)) % 1 == 0:
		print(str(num) + ' is a perfect square')
	else:
		print(str(num) + ' is not a perfect square')
perfectSquare(10)


def main(string):
    ind = []
    upper = string.upper()
    for i in range(len(string)):
        if string[i] == upper[i]:
            ind.append(i)
    return ind
print(main('HeLlO'))


def double_letters(string):
	check = False
    for i in range(len(string)):
        if string[i] == string[i+1]:
        	check = True
            return check
        if string[i] != string[i+1]:
        	return check


def main(dad, son):
	if dad > 1 and son > 0 and dad >son:
		rDad = int(dad)
		while int(dad)/int(son) != 2:
			dad += 1
			son += 1
		return dad-rDad
	else:
		return 'Dad must be greater than son'

print(main(-50, -10))


def recursionSolver(values):
	val = 0
	diff = values[2] - values[1]
	for i in values:
		val = i
	return val+diff
print(recursionSolver([2,4,6]))


total = 0
number = int(input('enter a anumber: '))
while number > 0:
	total += number
	number = int(input('Enter a number: '))
print('The sum is {}'.format(total))


def reverse_str_word(string):
	return string[::-1]

print(reverse_str_word("My Name is Jessa"))