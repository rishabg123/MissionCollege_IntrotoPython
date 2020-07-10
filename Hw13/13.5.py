import os.path

def main():
    fileName = input("Enter a filename to replace text with: ").strip()
    #print(fileName)

    while True:
        if not os.path.isfile(fileName):
            print("File:", fileName, "does not exist")
            fileName = str(input("Enter the correct filename: ").strip())
        else:
            break


    oldStr = str(input("Enter the old string to be replaced: "))
    newStr = str(input("Enter the new string to replace the old string: "))

    if (oldStr == newStr):
        print("The old string and the new string are the same!")
        exit(0)

    fp = open(fileName, "r")
    readlines = fp.readlines()
    fp.close()
    matching = False
    #print(lines)
    fpw = open(fileName, "w")
    for line in readlines:
        #print("Linei:", line)
        if oldStr in line:
            matching = True
        newline = line.replace(oldStr, newStr)
        #print("Lineo:", lineo)
        fpw.write(newline)

    fpw.close()

    if  matching == False:
        print('No match word "%s" found in the file: "%s"' % (oldStr, fileName))

    print("Done")
main()