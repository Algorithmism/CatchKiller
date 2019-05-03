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


from collections import OrderedDict
from typing import Dict


class Parser:

    """
    Parses fasta data into dictionary.
    key = name
    value = sequence

    Source: Broseph's Post from https://stackoverflow.com/questions/22698807/parse-fasta-sequence-to-the-dictionary

    In class, it was mentioned that this is the only portion student's are allowed to look at the methods of others.

    """


    def parse_sequences(filename: str,
                        ordered: bool=False) -> Dict[str, str]:
        """
        Parses a text file of genome sequences into a dictionary.
        Arguments:
          filename: str - The name of the file containing the genome info.
          ordered: bool - Set this to True if you want the result to be ordered.
        """
        NAME_SYMBOL = '>'
        result = OrderedDict() if ordered else {}

        last_name = None
        with open(filename) as sequences:
            for line in sequences:
                if line.startswith(NAME_SYMBOL):
                    last_name = line[1:-1]
                    result[last_name] = []
                else:
                    result[last_name].append(line[:-1])

        for name in result:
            result[name] = ''.join(result[name])

        return result



class HamMatrix:

    """
    Calculates the hamming distance of two sequences.


    """

    # calculates the distance | returns an integer
    def distCalc( dataVals, susVals):
        mismatch_list = []

        # for every sequence
        for i in range(len(dataVals)):
            # sum mismatches variable
            mismatch = 0

            # for every char in the sequences
            for j in range(len(susVals[0])):
                # get sum of mismatch
                if( dataVals[i][j] != susVals[0][j] ):
                    mismatch = 1 + mismatch
            mismatch_list.append(mismatch)

        return mismatch_list







dataName = "/home/marokima/PycharmProjects/CatchKiller/data/test.fasta"
suspectName = "/home/marokima/PycharmProjects/CatchKiller/data/query-sequence.fasta"

#dictionaries
data = Parser.parse_sequences(dataName)
suspect = Parser.parse_sequences(suspectName)

#lists of values
dataValues = list(data.values())
suspectValue = list(suspect.values())


distance = HamMatrix.distCalc(dataValues, suspectValue)
