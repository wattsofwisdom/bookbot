def count_words(content):
    """Count the words in content"""
    words = content.split()
    word_count = len(words)
    print(word_count)

def count_chars(content):
    """Count the number of characters"""
    cnt = {}
    for c in content:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return cnt

# Open the file in read mode
book = open("books/frankenstein.txt","r")

# read the entire content of the file and print
content = book.read()
# print(content)
count_words(content)
print(count_chars(content.lower()))

# close the file
book.close()

