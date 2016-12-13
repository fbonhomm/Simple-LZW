
class Dictionary():

    def __init__(self):
        """
            __init__()
            - self.dictSize = size of extended table ascii (256)
        """
        self.dictSize = 256

    def init(self):
        """
            init(self)
            [EN] loop who set dictionary until the size of extended table ascii
        """
        table = dict()
        for i in range(self.dictSize):
            table[chr(i)] = i
        return table

    def build(self, table, txt):
        """
            build(table, txt)
            - table = dictionary set until the size of extended table ascii
            - txt = texte
            [EN] Lzw encoding (for more explication going wikipedia LZW)
        """
        w = ''
        result = list()
        for c in txt:
            c = chr(c)
            wc = w + c
            if wc in table:
                w = wc
            else:
                result.append(table[w])
                table[wc] = self.dictSize
                self.dictSize += 1
                w = c
        if w:
            result.append(table[w])
        return result
