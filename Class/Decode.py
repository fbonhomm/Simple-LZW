
from struct import *
import os

class Decode():

    def __init__(self, input, output, octet='12'):
        """
            __init__(input, output, octet=12)
            - input = file compressed
            - output = file decompressed
            - octet = numbers of bit for decoded, default decoding on 12 bit
            - dict_size = maximun bit encoded character or word
            - sizeFile = size file compressed
            - file = list who will contain all code of each character or word
        """
        self.fdin = open(input, 'rb')
        self.fdout = open(output, 'w+b')
        self.dict_size = 256
        self.sizeFile = os.path.getsize(input)
        self.octet = int(octet, 10)
        self.file = list()

    def _add(self, w):
        """
            _add(w)
            - w = word
            [EN] recover a numbers of bit in word and add in dictionary
        """
        tmp = w[:self.octet]
        ret = int(tmp, 2)
        if ret != 0:
            self.file.append(ret)
        w = w[self.octet:]
        return w

    def _getChar(self, nbr):
        """
            _getChar(nbr)
            - nbr = numbers of bytes
            [EN] reading on file compressed and unpack the bytes
        """
        txt = self.fdin.read(nbr)
        return unpack('B', txt)[0]

    def build(self):
        """
            build()
            [EN] recover all character following number of bit on which they are encoding
        """
        w = ''
        while self.sizeFile > 0:
            c = self._getChar(1)
            tmp = bin(c)[2:]
            while len(tmp) < 8:
                tmp = '0' + tmp
            w += tmp
            if len(w) > self.octet:
                w = self._add(w)
            self.sizeFile -= 1
        while w:
            w = self._add(w)

    def _write(self, char):
        """
            _write(char)
            - char = chararcter
            [EN] write character on decompressed file
        """
        self.fdout.write(pack('B', ord(char)))

    def decode(self, table):
        """
            decode(table)
            - table = contain all character following number of bit on which they are encoding
            [EN] Lzw decoding (for more explication going wikipedia LZW)
        """
        w = chr(self.file.pop(0))
        self._write(w)
        for c in self.file:
            if c > 255 and c in table:
                entry = table[c]
            elif c > 255 and c not in table:
                entry = w + w[0]
            else:
                entry = chr(c)

            for char in entry:
                self._write(char)

            table[self.dict_size] = w + entry[0]
            self.dict_size += 1
            w = entry
