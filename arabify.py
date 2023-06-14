from re import sub

class Arabify:
    """Converts geez numbers to arab numbers
    """
    numbers_dict = {'፩': 1, '፪': 2, '፫': 3, '፬': 4,
                    '፭': 5, '፮': 6, '፯': 7, '፰': 8,
                    '፱': 9, '፲': 10, '፳': 20, '፴': 30,
                    '፵': 40, '፶': 50, '፷': 60, '፸': 70,
                    '፹': 80, '፺': 90, ' ': 0}

    @staticmethod
    def arabify(geezNum):
        # validate_number
       quartets = list(reversed(Arabify.__rollback(geezNum).split('፼')))
       num = sum(map
                 (lambda ntup:
                  Arabify.__arabify_quartets(ntup[1]) * (10000 ** ntup[0]),
                  enumerate(quartets)))

       return(num)

    def __rollback(strgeez):
        return(sub(r'^፼', '፩፼', (sub(r'^፻', '፩፻', sub('፼፻', '፼፩፻', strgeez)))))

    def __arabify_pairs(geezNum):
        """pairs the geeznums to their arabnums counter parts
        """
        # validate_pairs
        return(sum([Arabify.numbers_dict[char] for char in geezNum]))

    def __arabify_quartets(geezNum):
        """pairs the geeznums to their arabnums counter parts
        """
        # validate_quartets
        paired = geezNum.split('፻')

        if len(paired) == 0:
            paired = ['', '']
        elif len(paired) == 1:
            paired = ['', paired[0]]

        return((Arabify.__arabify_pairs(paired[0]) * 100) + Arabify.__arabify_pairs(paired[1]))
