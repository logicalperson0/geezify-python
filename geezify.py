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
        len_gp = len(geezified_pairs)

        for i in range(len_gp):
            if (i == 0):
                joined_str = geezified_pairs[i] + joined_str
            elif (i % 2 == 0 and geezified_pairs[i] == "፩" and i == len_gp - 1):
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