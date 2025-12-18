#imports
import sys
from character_utils import word_count
from character_utils import character_count
from character_utils import sorted_characters



#check argument input
if len(sys.argv) < 2 or sys.argv[1] == "":
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#read input txt
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

#convert text to string


#define report format
def report(filepath, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def main():
    #globals
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)    
    num_words = word_count(book_text)
    character_counts = character_count(book_text)
    sorted_chars = sorted_characters(character_counts)
    report(filepath, num_words, sorted_chars)

if __name__ == "__main__":
     main()