########################################################################################################################
#   Catch a Killer CSE 491 Homework 6 Final Project
#
#
#   This program will utilize Bioinformatics to simulate the process of catching a given suspect via a DNA string.
#   Another database of DNA strings is provided.
#
#
#
########################################################################################################################

#parsing FASTA formatted data

import re

dna = []
sequences = []

#read fasta file
def read_fasta(filename):

    # seq, header, dna, sequences
    global seq, header, dna, sequences

    # open the file
    with open(filename) as file:
        seq = ''
        # for loop through the lines
        for line in file:
            header = re.search(r'^>\w+', line)
            # if line contains the header '>' then append it to the dna list
            if header:
                line = line.rstrip("\n")
                dna.append(line)
            # in the else statement is where I have problems, what I would like is
            # else:
                # the proceeding lines before the next '>' is the sequence for each header,
                # concatenate these lines into one string and append to the sequences list
            else:
                seq = line.replace('\n', '')
                sequences.append(seq)





# f.i.l.e
filename = ''
# r.e.a.d_f.a.s.t.a
read_fasta(filename)
