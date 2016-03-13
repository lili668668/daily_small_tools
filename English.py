'''
英文文意字彙測驗
'''
import fileinput
import random

# input
filename = input('input filename:')
c = input('choose motion[1 show words, 2 test, 3 exit]:')

# file process
words = []
tmp = ''
flag = True
for line in fileinput.input(filename + '.txt'):
    if flag:
        tmp = line.replace('\n', '')
        flag = False
    else:
        tmp2 = (tmp, line.replace('\n', ''))
        words.append(tmp2)
        flag = True
# user process
while c == '1' or c == '2':
    mis = []
    if c == '1':
         for (a,b) in words:
             print(a + " - " + b)
    elif c == '2':
        tmpWords = words
        while tmpWords:
            testWord = random.choice(tmpWords)
            (a,b) = testWord
            ans = input(a[0] + "______" + a[-1] + " - " + b + "\n:")
            if ans == a:
                print('Not bad')
            else:
                print('Stupid')
                print(testWord)
                mis.append(testWord)
            tmpWords.remove(testWord)
        filename = filename + 'n'
        f = open(filename + '.txt', 'x')
        for (a,b) in mis:
            f.write(a + '\n')
            f.write(b + '\n')
        c = input('use mistake?[Y]:')
        if c != 'N':
            words = mis
    c = input('choose motion[1 show words, 2 test, 3 exit]:')


