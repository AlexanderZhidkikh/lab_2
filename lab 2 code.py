import csv

def esc(code):
    return f'\u001b[{code}m'

def fill_array(array, step, result):
    for Y in range(10):
        for X in range(10):
            if X == 0:
                array[Y][X] = round(step * (8 - Y) + step, 1)
            if Y == 9:
                array[Y][X] = X
    for Y in range(9):
        for X in range(1, 10):
            if round(array[Y][0], 1) >= result[X] > round(array[Y+1][0], 1):
                array[Y][X] = 1
    return array

end = esc(0)
red = esc(41) + '  ' + end
blue = esc(44) + '  ' + end
white = esc(107) + '  ' + end
black = esc(45) + '  ' + end
pr = '  '
RED = esc(41)
WHITE = esc(47)

for i in range(2):
    print(red * 14 + end)
for i in range(2):
    print(white * 14 + end)
for i in range(2):
    print(blue * 14 + end)
print()

sq = RED + '   ' + end
sqp = '   '

size = int(input('Введите размер паттерна: '))
print()

s1 = ((sq + sqp * 3) * size) + sq
s2 = (sqp + sq + sqp + sq) * size
s3 = (sqp * 2 + sq + sqp) * size
s4 = (sqp + sq + sqp + sq) * size
print((s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n') * size + s1)
print()

result = [i * 2 for i in range(10)]

step = round(abs((result[9] - result[0])) / 9, 1)

array_graph = [[0 for _ in range(10)] for _ in range(10)]
array_graph = fill_array(array_graph, step, result)

for Y in range(10):
    if Y == 9: print(WHITE + '  ' + end, end='')
    for X in range(10):
        if X == 0 or Y == 9: print(WHITE + str(array_graph[Y][X]) + ' ' + end, end='')
        elif array_graph[Y][X] == 1: print(RED + '  ' + end, end='')
        else: print(WHITE + '  ' + end, end='')
    print()
print()

km = 0
kb = 0

with open('books.csv') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))
    for row in table[1:]:
        if int(row[6][:4]) > 2016:
            kb += 1
        elif int(row[6][:4]) < 2016:
            km += 1

sum = km + kb
kmp = round(km / sum * 100)
kbp = round(kb / sum * 100)

print('Книги до 2016 года обозначены синим цветом: ' + blue + '   ' + end)
print('Книги после 2016 года обозначены красным цветом: ' + red + '   ' + end + '\n')
print(kmp, '% ' + blue * (int(kmp) // 2) + red * ((100 - kmp) // 2) + end, kbp, '%')