import os

print "if you want to compress press 1 to decompress press 2",
filename = raw_input()


def text_compress():
    import compress.py
    os.system("python compress.py")
    
def image_compress():
    import decompressor.py
    os.system("python decompressor.py")

if(filename == 1):
  text_compress()
else:
   image_compress()
