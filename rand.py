'''
幫你解決生活中各種需要random的小問題
'''
import fileinput
import random

filename = input('input file name:')

lines = []

for line in fileinput.input(filename):
    lines.append(line)

choice = random.choice(lines)

print(choice)

continus = input('continus?:')
while continus == 'Y' :
    choice = random.choice(lines)

    print(choice)

    continus = input('continus?:')
