class Arabify:
    """Converts geez numbers to arab numbers
    """
    arabNums = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 20, 30, 40, 50, 60, 70, 80, 90,
                100, 10000]
        
    geezNums = ['፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱',
                '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺',
                '፻', '፼']
    
    @staticmethod
    def arabify_num(self, geezNum):
        return self.concat_arabify_pairs(self.arabify_pairs(self, (self.arabify(self, geezNum))))


    def arabify(self, geezNum):
        """This takes in a geez number and seperates it
        into its individual values
        """
        sep_geezNum = []

        if type(geezNum) != str:
            raise ValueError("Not a valid string")
        
        for i in list(geezNum):
            for j in self.geezNums:
                if i == j:
                    sep_geezNum += i

        if sep_geezNum == []:
            return("Not a valid geez number!")
        else:
            return (sep_geezNum)

    def arabify_pairs(self, sep_geezNum):
        """pairs the geeznums to their arabnums counter parts
        """
        
        arabify_pairs = []

        for i in range(len(sep_geezNum)):
            for j in range(len(self.geezNums)):
                if sep_geezNum[i] == self.geezNums[j]:
                   arabify_pairs.append(self.arabNums[j])
        
        return (arabify_pairs)
    
    def concat_arabify_pairs(arabify_pairs):
        """This concats the list of nums to give
        its equivalent value for the geez num
        """
        arabnum = 0

        for i in range(len(arabify_pairs)):
            arabnum += arabify_pairs[i]
        
        return arabnum
             




h = Arabify

e = h.arabify_num(h, '፻፳፫')
d = h.arabify_num(h, '፼፲፼')
xx = h.arabify_num(h, '፼፩፼')
ww = h.arabify(h, "What is goin on?")

print(e)
print(d)
print(xx)
print(ww)
