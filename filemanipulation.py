import os
filename = input('enter file name (.txt): ')
if os.path.exists(filename):
    openfile = open(filename, 'r') #Precise accessibility, edit open(filename, 'path', 'r') 
    for count, ofl in enumerate(openfile):
        print(f"\nentry({count}): {ofl}")
    count += 1 #due to "forloop" started on index "0". 
    print(f"\nnumber of entry: {count}")
else:
    print("file not found, please check and try again.")
