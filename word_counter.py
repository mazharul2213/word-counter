fname = input("Insert file name:")
fopen = open(fname)
my_list = []
for line in fopen :
    data = line.split()
    #print(data)
    for word in data:
        if word in my_list :
            continue

        else :
            my_list.append(word)
print(sorted(my_list))


