
from Class.Dictionary import Dictionary as Dict
from Class.Decode import Decode as D

import sys

Dictionary = Dict()

if len(sys.argv) == 4:
    Decode = D(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    Decode = D(sys.argv[1], sys.argv[2])

"""
    sys.argv[1] = Compressed file
    sys.argv[2] = Decompressed file
    sys.argv[3] = Number of bit encoded provided per compress program
"""

if __name__ == '__main__':
    table = Dictionary.init()
    Decode.build()
    file = Decode.decode(table)
