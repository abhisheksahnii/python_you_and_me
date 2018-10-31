import autotest2

dictlist = []

for key in autotest2.locales:
    dictlist.append(key)

gnome_component = ['gedit', 'yelp', 'evolution']

temp = []

for x in gnome_component:
    for y in dictlist:
        temp1 = [x, y]
        temp.append(tuple(temp1))

for i in temp:
    print i
