class Geezify:

    @staticmethod
    def geezify(number):
        return Geezify.__concat_geezified_pairs(Geezify.__geezify_pairs(Geezify.__pairup(number)))

    def __pairup(number):
        if (type(number) != int):
            raise TypeError("not a valid number")
        pairs = []

        while ((number // 100 != 0) or
               (number % 100 != 0)):
            pairs.append(number % 100)
            number = (number // 100)

        return pairs


    def __geezify_pairs(pairs):
        oneth = ['', '፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱']
        tenth = ['', '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺']

        geezified_pairs = list(map(lambda num: tenth[num // 10] +
                                   oneth[num % 10],
                                   pairs))

        return geezified_pairs


    def __concat_geezified_pairs(geezified_pairs):
        joined_str = ""

        for i in range(len(geezified_pairs)):
            if (i == 0):
                joined_str = geezified_pairs[i] + joined_str
            elif (i % 2 == 0 and geezified_pairs[i] == "፩"):
                joined_str = "፼" + joined_str
            elif (i % 2 == 0):
                joined_str = geezified_pairs[i] + "፼" + joined_str
            elif (geezified_pairs[i] == "፩"):
                joined_str = "፻" + joined_str
            elif (geezified_pairs[i] == ""):
                continue
            else :
                joined_str = geezified_pairs[i] + "፻" + joined_str

        return joined_str

print(Geezify.geezify(1))
print('፩')
print("-----------")
print(Geezify.geezify(10))
print('፲')
print("-----------")
print(Geezify.geezify(100))
print('፻')
print("-----------")
print(Geezify.geezify(1000))
print('፲፻')
print("-----------")
print(Geezify.geezify(10000))
print('፼')
print("-----------")
print(Geezify.geezify(100000))
print('፲፼')
print("-----------")
print(Geezify.geezify(1000000))
print('፻፼')
print("-----------")
print(Geezify.geezify(10000000))
print('፲፻፼')
print("-----------")
print(Geezify.geezify(100000000))
print('፼፼')
print("-----------")
print(Geezify.geezify(1000000000))
print('፲፼፼')
print("-----------")
print(Geezify.geezify(10000000000))
print('፻፼፼')
print("-----------")
print(Geezify.geezify(100000000000))
print('፲፻፼፼')
print("-----------")
print(Geezify.geezify(1000000000000))
print('፼፼፼')
print("-----------")

# a = Geezify(23423)
# print(a.geezify)
# print('፩')
