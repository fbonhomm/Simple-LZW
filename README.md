
# Simple LZW

implementing the algorithm Lempel–Ziv–Welch in Python3

## Usage:

### compress.py
- python3 compress.py original compressed

### decompress.py
- python3 decompress.py compressed decompressed numbers_of_bit

## Benchmark:
File      | Original Size   | Compressed Size  | Ratio
--------- | --------------- | -----------------| ------
Test1     |      84 bytes   |      79 bytes    |   -5.952%
Test2     |     598 bytes   |      428 bytes   |  -28.428%
Test3     |   22301 bytes   |    8761 bytes    |  -60.714%
Test4     |  285376 bytes   |   103938 bytes   |  -63.578%
