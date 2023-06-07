class Arabify:

    def arabify(geezNum):
        """This takes in a geez number and seperates it
        into its individual values
        """
        geezNums = ['፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱',
                    '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺',
                    '፻', '፼']
        sep_geezNum = []

        if type(geezNum) != str:
            raise ValueError("Not a valid string")
        
        for i in list(geezNum):
            for j in geezNums:
                if i == j:
                    sep_geezNum += i

        if sep_geezNum == []:
            return("Not a valid geez number!")
        else:
            return (sep_geezNum)

    def arabify_pairs(sep_geezNum):
        """pairs the geeznums to their arabnums counter parts
        """
        arabNums = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    10, 20, 30, 40, 50, 60, 70, 80, 90,
                    100, 10000]
        
        geezNums = ['፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱',
                    '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺',
                    '፻', '፼']
        
        arabify_pairs = []

        for i in range(len(sep_geezNum)):
            for j in range(len(geezNums)):
                if sep_geezNum[i] == geezNums[j]:
                   arabify_pairs.append(arabNums[j])
        
        return (arabify_pairs)
    
    def concat_arabify_pairs(arabify_pairs):
        """This concats the list of nums to give
        its equivalent value for the geez num
        """
        arabnum = 0

        for i in range(len(arabify_pairs)):
            if arabify_pairs[0] == 10000:
                arabnum = arabify_pairs[0] + arabify_pairs[1]
            arabnum += arabify_pairs[i]
        
        return arabnum
             



obj = Arabify

e = obj.arabify('፻፳፫')
c = obj.arabify("W፻፳፫hat is goin on?")
d = obj.arabify('፼፲፼')
ww = obj.arabify("What is goin on?")

s = obj.arabify_pairs(e)
i = obj.arabify_pairs(c)
j = obj.arabify_pairs(d)

ss = obj.concat_arabify_pairs(s)
ii = obj.concat_arabify_pairs(i)
jj = obj.concat_arabify_pairs(j)

print(e)
print(c)
print(d)

print(s)
print(i)
print(j)

print(ss)
print(ii)
print(jj)