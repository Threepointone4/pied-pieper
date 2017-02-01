import zlib,sys,time,base64

text_filename = raw_input("enter file name")
                          
text = open(text_filename,'r').read()
print 'Raw size:',sys.getsizeof(text)

compressed = zlib.compress(text,9)
#print '9 compressed size:',sys.getsizeof(compressed)

new_name = raw_input("enter new name")
savecomp = open(new_name,'a')
savecomp.write(compressed)
savecomp.close()

compfile = open(new_name,'r').read()
compressed = zlib.compress(text,9)
print '9 compressed size:',sys.getsizeof(compressed)



