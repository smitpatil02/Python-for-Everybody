#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
handle = open(name)
list1 = []
list2 = []
list3 = []
lst = []
counts = dict()

for line in handle:
    if not line.startswith("From ") : continue
    list1 = line.split()
    list2 = list1[5].split(":")
    list3.append(list2[0])

for list in list3:
    counts[list] = counts.get(list,0)+1


for k,v in counts.items():
    newtup = (k,v)
    lst.append(newtup)

#print(lst)
lst = sorted(lst)
#print(lst)
for k,v in lst:
    print(k,v)
