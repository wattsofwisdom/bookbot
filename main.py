# Open the file in read mode
book = open("books/frankenstein.txt","r")

# read the entire content of the file and print
content = book.read()
print(content)

# close the file
book.close()