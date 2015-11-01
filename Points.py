x = 0
y = 0
k = 1

while True:
    user_input = input("Please enter direction ('<', '>', '^', 'v') or '~' for warp and '#' for end\n 'c' for clearing the position\n\n")
    if user_input == '<':
        x -= k
        pass
    if user_input == '>':
        x += k
        pass
    if user_input == '^':
        y -= k
        pass
    if user_input == 'v':
        y += k
        pass
    if user_input == '~':
        k = -k
        pass
    if user_input == 'c':
        x = 0
        y = 0
        pass
    if user_input == '#':
        break
    else: print("Please enter one of the valid symbols ( '<', '>', '^', 'v', '~', '#')")

print(x, y)
