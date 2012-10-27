# -*- coding: utf-8 -*-
"class practice work 4"

def map_yield(func, iterator):
    "map generator"

    for i in iterator:
        yield func(i)

def my_filter(func, iterator):
    "filter generator"

    for i in iterator:
        if func(i):
            yield i

def gh(param):
	"If more than 3"

	return param > 3

def my_reduce(func, iterator):
    "reduce generator"

    while True:
        if len(iterator) == 1:
            yield iterator
            return
        if len(iterator) == 2:
            yield func(iterator)
            return
        if len(iterator) > 2:
            res = func(iterator[:2])
            yield res
            iterator = [res] + iterator[2:]

def iter_lines(fd):
    "somthing to do"
    
    fs = open(fd)
    res = ""

    while True:
        l = fs.read(1)
        if l == '':
            yield res
            return
        if l == '\n':
            yield res
            res = ""
        else:
            res += l

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

    gen = map_yield(lambda x : x ** 2, [1, 2, 3])
    assert next(gen) == 1
    assert next(gen) == 4
    assert next(gen) == 9
    gen = my_filter(gh, [1,2,3,4,5,6,7])
    assert next(gen) == 4
    assert next(gen) == 5
    assert next(gen) == 6
    gen = my_reduce(sum, [1,1,1,1,1,1])
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 4
    assert next(gen) == 5
    assert next(gen) == 6
    #assert list(iter_lines("text.txt")) == ["1 2 3 3.45 abra_cadabra   ", "", "12"]
    #assert list(strip_spaces(["1 2 3 3.45 abra_cadabra   ", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "", "12"]
    #assert list(drop_empty(["1 2 3 3.45 abra_cadabra", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "12"]
    #assert list(split_items(["1 2 3 3.45 abra_cadabra", "12"])) == [1, 2, 3, 3.45, "abra_cadabra", 12]
    #assert list(get_ints([1, 2, 3, 3.45, "abra_cadabra", 12])) == [1, 2, 3, 12]
    #assert my_sum([1, 2, 3, 12]) == 18
    assert my_sum(get_ints(split_items(drop_empty(strip_spaces(iter_lines("text.txt")))))) == 18
    print "TEST OK!"
    raw_input()
    return 0

if __name__ == "__main__":    
	exit(main())
