# -*- coding: utf-8 -*-
"class practice work 4"

def iter_lines(fd):
    "somthing to do"
    
    res = ""
    for l in fd:
        if l == '\n':
            yield res
            res = ""
        else:
            res += l
    yield res

def strip_spaces(iter):
	"strip spaces"

	for str1 in iter:
		yield str1.strip()

def drop_empty(iter):
	"drop empty"

	for str1 in iter:
		if str1 != "":
			yield str1
		else:
			continue 

def split_items(iter):
    "split every line on int/float/string sequince"
    #"10 12.5 sdfsdgsgs 12.8       78" => [10, 12.5, "sdfsdgsgs". 12.8]
    
    for srt1 in iter:
        temp = srt1.split(' ')
        for substr in temp:
            if substr.isdigit():
                yield int(substr)
                continue
            isstring = False
            twopoints = False
            for ch in substr:
                if ch == '.':
                    if twopoints == False:
                        twopoints = True
                        break
                    else:
                        isstring = True
                        break
                if not ch.isdigit():
                    isstring = True
                    break
            if isstring:
                yield substr
            else:
                yield float(substr)


def get_ints(iter):
	"yield only ints"

	for srt8 in iter:
		if type(srt8) == int:
			yield srt8

def my_sum(iter):
	"calculate sum of all elements in iter"

	sum = 0

	for srt10 in iter:
		sum += int(srt10)

	return sum

def main():
    "main"
    #fs = open("text.txt")
    #fd = fs.read()
    fd = "1 2 3 3.45 abra_cadabra   \n\n12"
    assert list(iter_lines(fd)) == ["1 2 3 3.45 abra_cadabra   ", "", "12"]
    assert list(strip_spaces(["1 2 3 3.45 abra_cadabra   ", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "", "12"]
    assert list(drop_empty(["1 2 3 3.45 abra_cadabra", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "12"]
    assert list(split_items(["1 2 3 3.45 abra_cadabra", "12"])) == [1, 2, 3, 3.45, "abra_cadabra", 12]
    assert list(get_ints([1, 2, 3, 3.45, "abra_cadabra", 12])) == [1, 2, 3, 12]
    assert my_sum([1, 2, 3, 12]) == 18
    assert my_sum(get_ints(split_items(drop_empty(strip_spaces(iter_lines(fd)))))) == 18
    print "TEST OK!"
    raw_input()
    return 0

if __name__ == "__main__":    
	exit(main())
