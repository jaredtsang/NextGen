# titles = ('a tale of two cities', 'about A boy', 'wind in the willows')
# for x in titles:
#     lowerx = x.lower()
#     titlex = x.title()
#     print(titlex)


def fix_title(title):
    title = title.lower()
    title = title.split()
    title = list(title)
    for x in range(len(title)):
        if title[x] not in ('a', 'the', 'an', 'in', 'of'):
            title[x] = title[x].capitalize()
    fixed_title = ' '.join(title)
    return fixed_title

print(fix_title('GONE WITH THE WIND'))