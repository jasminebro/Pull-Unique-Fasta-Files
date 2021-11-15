import Bio

from Bio.SeqRecord import SeqRecord

from Bio import SeqIO

from Bio.Alphabet import SingleLetterAlphabet

'''This script pulls unique fasta sequences from a file and writes them to another file'''

# place location of file here
handle = open("C:File Path.fasta","r") # place location of file here

# #this is the file where the new fasta file is placed
OutPut=open("C:\\Users\\Jasmine\\Dropbox\\FinishYourProject\\sf86SMseq.fasta", "w")

Sequence_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta")) #create a dictionary

handle.close()


#pull keys from text file/GI#s of files you want
keys=[keys.strip()for keys in open("Path of List of keys to pull.txt")] 

#this gets rid of repetitive keys in the output fasta file
UniqueKeys=list(set(keys)) 
#print(UniqueKeys)

n=0

for item in UniqueKeys:

    record=(Sequence_dict[item])

    SeqIO.write(record,OutPut,"fasta")

    n=n+1

    #Count.write(str(n))

    print(n)

print("Done!")

OutPut.close()
