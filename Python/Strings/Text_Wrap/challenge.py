import textwrap

def wrap(string, max_width):
	r = textwrap.fill(string, max_width)
	return r


if __name__ == "__main__":
	s = raw_input()
	w = int(raw_input())
	r = wrap_text(s, w)
	print r
