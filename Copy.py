from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coppying from %s to %s" %(from_file , to_file)

in_file= open(from_file)
indata=open(from_file).read()

print "The iinput file is %d bytes long" % len(indata)

print "Does o/p file esists? % r" %exists(to_file)

print "Ready, hit enter to continue"

raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "saaraye!"

out_file.close()
in_file.close()

