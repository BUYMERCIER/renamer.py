import os
import glob

files = glob.glob('*.jpg')

i = 1

for file in files:
    os.rename(file, "{}.jpg".format(i))
    i += 1

last = open('last.txt', "w")
last.write(str(i - 1))
last.close
