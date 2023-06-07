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
        tenthousand = 1
        arabnum = 0

        for i in range(len(arabify_pairs)):
            if arabify_pairs[0] == 100:
                arabnum += arabify_pairs[i]
            elif arabify_pairs[0] == 10000:
                arabnums = arabify_pairs[0] + arabify_pairs[1]
                if i > 1:
                    tenthousand *= arabify_pairs[i]
                arabnum = tenthousand * arabnums
            elif arabify_pairs[i] == 100 & i > 0:
                tenthousand *= arabify_pairs[i]
                arabnum = tenthousand
                
        return arabnum
             



# rough test case:

h = Arabify

e = h.arabify_num(h, '፻፳፫') #123
d = h.arabify_num(h, '፼፲፼') #100100000
xx = h.arabify_num(h, '፼፩፼') #100010000
zz = h.arabify_num(h, '፴፻፴፫') #3033
ff = h.arabify_num(h, '፼፻፩') #10101
ww = h.arabify_num(h, "What is goin on?")

print(e)
print(d)
print(xx)
print(ww)
print(zz)
print(ff)
