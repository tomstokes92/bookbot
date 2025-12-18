#check argument input
import sys
if len(sys.argv) < 2 or sys.argv[1] == "":
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#set filepath to be input 
filepath = sys.argv[1]

#read input txt
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

#convert text to string
def main():
    book = get_book_text(filepath)
    return book

book_text = main()
from stats import word_count
num_words = word_count(book_text)
from stats import character_count
character_counts = character_count(book_text)
from stats import sorted_characters
sorted_chars = sorted_characters(character_counts)

#define report format
def report():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

report()