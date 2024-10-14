def count_words(content):
    """Count the words in content"""
    words = content.split()
    word_count = len(words)
    print(word_count)

# Open the file in read mode
book = open("books/frankenstein.txt","r")

# read the entire content of the file and print
content = book.read()
# print(content)
count_words(content)

# close the file
book.close()

