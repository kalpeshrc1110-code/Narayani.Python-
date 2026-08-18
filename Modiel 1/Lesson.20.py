# activity 1

empty_list = []
print (empty_list)

number = [1,2,3,4,5]
print (number)

mulit = [1*2, 5*9, 7*2,] * 2
print (mulit)

alist = [100,200,300,400,500]
alist = alist [ ::-1]
print (alist)

#activity 2

def match_words(words):
    cntr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word [0] == word [-1]:
            cntr += 1
            lst.append (word)

        print ("list of words with first and last letter same /n", lst)
        return cntr


count = match_words (['abc', 'aca', 'bnb', '1221', 'dgfd',])
print (count)