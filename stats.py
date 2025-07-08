def count_words(file_contents):
    words = file_contents.split()
    words_count = len(words)
    print(f"{words_count} words found in the document")
