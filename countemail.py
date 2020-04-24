#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
handle = open(name)
counts = dict()
list = []
for line in handle:
    if not line.startswith("From:") : continue
    words = line.split()

    for word in words[1:]:
        counts[word] = counts.get(word,0) + 1

bcount = None
bword = None
for word,count in counts.items():
    if bcount is None or count > bcount:
        bword = word
        bcount = count

print(bword,bcount)
