

#Write a program, wordcount.py, that opens a file and counts how many times each 
#space-separated word occurs in that file. Your program should then print those 
#counts to the screen.

#We’ve included a small file, test.txt, that you can use for testing out your 
#script. The file contains this poem:# 


def count_words(file):

    text_file = open(file)

    word_counts = {}

    for line in text_file:
        line = line.rstrip()
        words = line.split(' ')

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    word_counts.items()

    for word, number in word_counts.items():
        print (f"{word} {number}")

count_words('test.txt')