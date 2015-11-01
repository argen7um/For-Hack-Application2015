
puzzle = '''ivan
evnh
inav
mvvn
qrit
navi
'''
clue = 'ivan'

puzzle = puzzle.replace(' ', '')
length = puzzle.index('\n')+1
letters = [(letter, divmod(index, length))
            for index, letter in enumerate(puzzle)]

lines = {}
offsets = {'down': 0, 'left down': -1, 'right down': 1}
for direction, offset in offsets.items():
    lines[direction] = []
    for i in range(length):
        for j in range(i, len(letters), length + offset):
            lines[direction].append(letters[j])
        lines[direction].append('\n')
lines['right'] = letters
lines['left'] = [i for i in reversed(letters)]
lines['up'] = [i for i in reversed(lines['down'])]
lines['right up'] = [i for i in reversed(lines['left down'])]
lines['left up'] = [i for i in reversed(lines['right down'])]
for direction, tup in lines.items():
    string = ''.join([i[0] for i in tup])
    if clue in string:
        location = tup[string.index(clue)][1]
        print (clue, 'row', location[0]+1, 'column', location[1]+1, direction)
