#!/usr/bin/python

import base64
import argparse
import random

def xor(encoded,key):
    return ''.join(chr(ord(a) ^ key) for a in encoded)

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="Path to powershell script",type=str,dest='path',required=True)
parser.add_argument("-o","--output", help="Output of powershell obfuscate script",type=str,dest='output',required=True)
args = parser.parse_args()

path = args.path
output = args.output

f = open(path,'r')
content = f.read()
f.close()

print ("[+]Generation of random encryption key")
key = random.randint(1,196)
print ("[+]Encode in UTF-16LE")
encoded = content.encode("utf-16-le")
print ("[+]Encrypt in XOR")
encoded = xor(encoded, key)
print ("[+]Encode in Base64")
encoded = base64.b64encode(encoded)
print ("[+]Your powershell is encoded : " + output)


with open("stub.txt") as f:
    templateObfuscate = f.read()
        
templateObfuscate = templateObfuscate.replace("$$DATA$$", encoded)
templateObfuscate = templateObfuscate.replace("$$KEY$$", str(key))

m = open(output,"w")
m.write(templateObfuscate)
m.close()