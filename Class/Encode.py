
from struct import *

class Encode():

    def __init__(self, input, output, octet=0):
        """
            __init__(input, output, octet=0)
            - input = file descriptor original file
            - output = file descriptor compressed file
            - octet = numbers of bit for encoded, default variable encoding
        """
        self.fdin = open(input, 'rb')
        self.fdout = open(output, 'w+b')
        self.byte = octet

    def setSizeByte(self, sizeDict):
        """
            setSizeByte(sizeDict)
            - sizeDict = maximun bit encoded character or word
            [EN] Initialize self.byte for encoding, if byte is not provided the encoding on maximun character
        """
        if self.byte != 0:
            return
        self.byte = sizeDict.bit_length()

    def encode(self, result, sizeDict):
        """
            encode(result, sizeDict)
            - result = contain dictionnary encoded per LZW algorithm
            - sizeDict = maximun bit encoded character or word
            [EN] Encoding all index of result on the bit provided per self.byte and write on file output
        """
        self.setSizeByte(sizeDict)
        print("Encoded on %d bit" % (self.byte))
        buffer = ''
        for c in result:
            byte = bin(c)[2:]
            while len(byte) < self.byte:
                byte = '0' + byte
            buffer += byte

        while len(buffer) > 8:
            octet = buffer[:8]
            self.fdout.write(pack('B', *bytearray([int(octet, 2)])))
            if len(buffer) > 8:
                buffer = buffer[8:]
        while len(buffer) < 8:
            buffer = buffer + '0'

        self.fdout.write(pack('B', *bytearray([int(buffer, 2)])))
        self.fdout.close()
