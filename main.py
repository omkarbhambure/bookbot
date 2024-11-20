def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)
    
    def count_words(text):
        word_list = text.split()
        return len(word_list)
    
    def character_count(text):
        lowered_text = text.lower()
        d = {}
        for c in lowered_text:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d
    
    #print(count_words(file_contents))
    #print(character_count(file_contents))

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    dicto = character_count(file_contents)
    for k in dicto:
        if not k.isalpha():
            continue
        print(f"The '{k}' character was found {dicto[k]} times")
    print("--- End report ---")

main()