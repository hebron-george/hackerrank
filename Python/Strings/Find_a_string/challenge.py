def count_substring(string, sub_string):
    sub_len = len(sub_string)
    count = 0
    for i in range(0, (len(string) - sub_len)+1):
    	if string[i:i+sub_len] == sub_string:
    		count += 1

    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count