def make_line(n):
    if n == 1:
        return ['*']

    stars = make_line(n//3)

    line = []
    for star in stars:
        line.append(star * 3)
    for star in stars:
        line.append(star + " "*(n//3) + star)
    for star in stars:
        line.append(star*3)

    return line


n = int(input())

print('\n'.join(make_line(n)))