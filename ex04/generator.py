import time
text = "Le Lorem Ipsum est simplement du faux texte."


def randomer(len):
    ts = time.time()
    ran = ts % len
    ran *= 1000
    ran = int(ran % len)
    return ran


def shuffle(list):
    le = len(list)
    list2 = []
    for x in range(len(list)):
        mot = list[randomer(le)]
        list2.append(mot)
        list.remove(mot)
        le -= 1
    list = list2
    return list


def generator(text, sep=" ", option=None):
    op = option
    if op == "unique" or op == "shuffle" or op == "ordered" or not op:
        if isinstance(text, str):
            list = text.split(sep)
            if option == "unique":
                list = set(list)
            elif option == "shuffle":
                list = shuffle(list)
            elif option == "ordered":
                list = sorted(list)
            for x in list:
                yield x
        else:
            print("ERROR")
    else:
        print("ERROR")


# for x in generator(text, sep=" "):
#     print(x)
