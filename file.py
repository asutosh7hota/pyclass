from sys import argv

script, filename = argv

print "we gonna erase %r" % filename

print"if you dont want hit CRTL-C or return enter"

raw_input("? ")

print "Opening file"

target = open(filename, 'w')

print "truncating"

target.truncate()

print "insert  line"

line1 = raw_input("line 1 :")

print "I m gonna write the stuff"

target.write(line1)
print "finally we close the file"
target.close

print "file closed"


