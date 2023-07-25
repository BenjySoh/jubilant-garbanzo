import os
filename = input('enter file name (.txt): ')
if os.path.exists(filename):
    openfile = open(filename, 'r')
    for count, ofl in enumerate(openfile):
        print(f"\nentry({count}): {ofl}")
    print(f"\nnumber of entry: {count}")
else:
    print("file not found, please check and try again.")