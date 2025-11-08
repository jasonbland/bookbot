import sys
from stats import character_count_sorted, number_of_words, print_chars

def get_book_text(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return file.read()

def main():
  # file_path = './books/frankenstein.txt'

  # python3 main.py books/frankenstein.txt
  # python3 main.py books/mobydick.txt
  # python3 main.py books/prideandprejudice.txt


  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_text = get_book_text(sys.argv[1])
  word_count = number_of_words(book_text)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  chars = character_count_sorted(book_text)
  print_chars(chars)
  print("============= END ===============")

main()
