import urllib.request

fullcnt, associatecnt, assistantcnt = 0, 0, 0
fullsalary, associatesalary, assistantsalary = 0, 0, 0


#url1 = input("Enter URL for a file: ").strip()
#url = url1.strip('"')
#print(url)
infile = urllib.request.urlopen("http://liveexample.pearsoncmg.com/data/Salary.txt")
#fp = open("Salary.txt", "r")

#infile = fp.readlines()
for line in infile:
    decoded_line = line.decode("utf-8")
    #decoded_line = line

    record = decoded_line.split()
    #print("Record: ", record)

    salary = (record[3])
    if 'full' in decoded_line:
        role = 'full'
        fullcnt += 1
        fullsalary += float(record[3])
    elif 'assistant' in decoded_line:
        role = 'assistant'
        assistantcnt += 1
        assistantsalary += float(record[3])
    else:
        role = 'associate'
        associatecnt += 1
        associatesalary += float(record[3])


    #print(role)

avgfullsalary = "{:.2f}".format(fullsalary / fullcnt)
avgassociatesalary = "{:.2f}".format(associatesalary / associatecnt)
avgassistantsalary = "{:.2f}".format(assistantsalary / assistantcnt)
facultysalary = fullsalary + associatesalary + assistantsalary
facultycnt = fullcnt + associatecnt + assistantcnt
avgfacultysalary = "{:.2f}".format(facultysalary / facultycnt)
print()
print("Full professor count:", str(fullcnt))
print("Total full professor salary:", "{:.2f}".format(fullsalary))
print("Average full professor salary:", avgfullsalary)
print()
print("Associate professor count:", str(associatecnt))
print("Total associate professor salary:", "{:.2f}".format(associatesalary))
print("Average associate professor salary:", avgassociatesalary)
print()
print("Assistant professor count:", str(assistantcnt))
print("Total assistant professor salary:", "{:.2f}".format(assistantsalary))
print("Average assistant professor salary:", avgassistantsalary)
print()
print("Faculty count:", str(facultycnt))
print("Total faculty salary:", "{:.2f}".format(facultysalary))
print("Average faculty salary:", avgfacultysalary)

#fp.close()
