
# from getopt import getopt
import sys
# import keyword
from itertools import permutations

def load_word_file(fileName: str) -> str:
    wordList: list = []
    my_file = open(fileName, "r")
    for line in my_file:
        wordList.append(line.strip())
    my_file.close()
    return wordList

def list_intersection(list1: list, list2: list) -> list:
    return (list(set(list1) & set(list2)))

def word_permutations(word: str) -> list:
    permutationList: list = []
    for i in range (1,len(word) + 1):
        setPermutations = permutations(word,i)
        # Join tuples into a single string 
        for j in list(setPermutations): 
            str_join: str = "".join(j) # This is slow for long words
            permutationList.append(str_join)
    return permutationList

def word_jumble_algorithm(wordFile: str, word: str) -> list:
    # Load the word file
    wordList: list = load_word_file(wordFile)

    # Get all sets, sub sets and permutations
    permutationList: list = word_permutations(word)

    # Find the list of permutations that intersect with the word list
    validWordList: list = list_intersection(wordList, permutationList)

    return validWordList

def main():
    try:
        wordFile = str(sys.argv[1])
        word = str(sys.argv[2])
        #print ('File: ', wordFile)
        #print ('Word: ', word)

        validWordList = word_jumble_algorithm(wordFile, word)

        # Print the words
        print(validWordList)
    except:
        print ('#########  Incorrect Usage  #########')
        print ('python3 jumble_solver.py <word_file.txt> <word>')
        sys.exit(2)


if __name__ == "__main__":
    main()


    # try:
    #     opts, args = getopt.getopt(sys.argv, "hi:o:", ["ifile=","ofile="])
    # except getopt.GetoptError:
    #     print ('python3 jumble_solver.py -i <corncob_lowercase.txt> -w <word>')
    #     sys.exit(2)