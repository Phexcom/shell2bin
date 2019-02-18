#!/usr/bin/python
#Referenced "Malware Analyst’s "Cookbook

import re
import sys
try:
    from distorm3 import Decode, Decode16Bits, Decode32Bits, Decode64Bits
except ImportError:
    print 'distorm3 is not installed, install "python -m pip install distorm3"'
    sys.exit(1)


# the first argument is Unicode-encoded shellcode 

sc = sys.argv[1]

# translate to binary
bin_sc = re.sub('%u(..)(..)', 
	lambda x: chr(int(x.group(2),16))+chr(int(x.group(1),16)), sc)

# save to disk (optional)
FILE = open("shellcode.bin", "wb") 
FILE.write(bin_sc)
FILE.close()

# disassemble the binary data
l = Decode(0, bin_sc, Decode32Bits) 
for i in l:
	print "0x%08x (%02x) %-20s %s" % (i[0], i[1], i[3], i[2])
