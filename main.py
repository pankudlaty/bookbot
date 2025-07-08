from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



    

def main():
    book_text = get_book_text("/home/pawel/workspace/github.com/pankudlaty/bookbot/books/frankenstein.txt")
    count_words(book_text)

if __name__ == "__main__":
    main()
