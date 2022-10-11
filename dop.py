import os, time

def esc(code):
    return f'\u001b[{code}m'

end = esc(0)
red = esc(41) + '  ' + end
blue = esc(44) + '  ' + end
white = esc(107) + '  ' + end
black = esc(45) + '  ' + end
pr = '  '

pic_1 = [pr * 9,
         pr * 2 + black * 5,
         pr * 4 + black * 4,
         pr * 3 + black + white * 3 + black,
         pr * 3 + black * 2 + white + black,
         pr * 4 + white * 3,
         pr * 2 + red * 2 + white + red * 2,
         pr * 3 + red + black + red,
         pr + red * 3 + black + red * 2,
         red + pr + red * 2 + black + red + white + red,
         black + pr + black * 4 + pr + black,
         pr + white + red * 4 + white,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + black + pr * 2 + black,
         pr * 2 + black + pr * 2 + black]

pic_2 = [pr * 9,
         pr * 9,
         pr * 3 + black * 2,
         pr * 4 + black * 3,
         pr * 3 + black * 4,
         pr * 3 + black + white * 3,
         pr * 2 + red * 2 + black + white + black,
         pr * 3 + red + white + red,
         pr + red * 3 + black + red * 2,
         red + pr + red * 2 + black + red + white + red,
         black + pr + black * 4 + pr + black,
         pr + white + red * 4 + white,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + black + pr * 2 + black,
         pr * 2 + black + pr * 2 + black]

pic_3 = [pr * 9,
         pr * 9,
         pr * 9,
         pr * 4 + black * 3,
         pr * 3 + black * 5,
         pr * 3 + black + white * 2 + black * 2,
         pr * 2 + red * 2 + black + white + black + pr + black,
         pr * 3 + red + white + red,
         pr + red * 3 + black + red * 2,
         red + pr + red * 2 + black + red + white + red,
         black + pr + black * 4 + pr + black,
         pr + white + red * 4 + white,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + red + pr * 2 + red,
         pr * 2 + black + pr * 2 + black,
         pr * 2 + black + pr * 2 + black]

while True:
    print(*pic_1, sep='\n')
    time.sleep(0.25)
    os.system("cls")

    print(*pic_2, sep='\n')
    time.sleep(0.25)
    os.system("cls")

    print(*pic_3, sep='\n')
    time.sleep(0.25)
    os.system("cls")

    print(*pic_2, sep='\n')
    time.sleep(0.25)
    os.system("cls")