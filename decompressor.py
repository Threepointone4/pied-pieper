import zlib,sys,time,base64
text_filename = raw_input("enter file name")

text = open(text_filename,'r').read()


#decompressed = zlib.compress(base64.b64decode(text))
decompressed = zlib.decompress(text)
new_name = raw_input("enter new name")
savecomp = open(new_name,'a')
savecomp.write(decompressed)
savecomp.close()

