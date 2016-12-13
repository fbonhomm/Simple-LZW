
from Class.Dictionary import Dictionary as Dict
from Class.Encode import Encode as E

import sys

Dictionary = Dict()
Encode = E(sys.argv[1], sys.argv[2])

"""
    sys.argv[1] = Original file
    sys.argv[2] = Compressed file
"""

if __name__ == '__main__':
    txt = Encode.fdin.read()
    table = Dictionary.init()
    result = Dictionary.build(table, txt)
    Encode.encode(result, Dictionary.dictSize)
