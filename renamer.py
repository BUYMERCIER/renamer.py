import os
import glob

files = glob.glob('*.jpg')

i = 1

for file in files:
    os.rename(file, "{}.jpg".format(i))
    i += 1

with open('last.txt', "w") as f:
    f.write(str(i - 1))
    f.close
