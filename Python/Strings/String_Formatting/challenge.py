def print_formatted(number):
	buffer_width = len("{0:b}".format(number))
	for i in range(1, number+1):
		print str(i).rjust(buffer_width) + ' ' + "{0:o}".format(i).rjust(buffer_width) + ' ' + "{0:x}".format(i).upper().rjust(buffer_width) + ' ' + "{0:b}".format(i).rjust(buffer_width)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
