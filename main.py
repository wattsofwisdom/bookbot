def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")

    # Open the file in read mode
    book = open(book_path,"r")

    # read the entire content of the file and print
    content = book.read()

    # close the file
    book.close()

    # get total word count
    tot_num_words = count_words(content)

    # get character count
    chars_dict = count_chars(content.lower())

    print(f"{tot_num_words} words found in the document\n")

    for key, value in chars_dict.items():
        if not key.isalpha():
            continue
        print(f"The '{key}' character was found {value} times")
    print("--- End of Report ---")

def count_words(content):
    """Count the words in content"""
    words = content.split()
    word_count = len(words)
    return word_count

def count_chars(content):
    """Count the number of characters"""
    cnt = {}
    for c in content:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return cnt

main()
