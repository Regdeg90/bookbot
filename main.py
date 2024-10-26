
def get_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def count_words(text):
    word_count = 0
    for line in text.split("\n"):
        word_count += len(line.split())
    return word_count

def count_chars(text):
    chars = {}
    for line in text.split("\n"):
        for ch in line.lower():
            chars[ch] = chars.get(ch, 0) + 1
    return chars

def book_report(filepath):
    text = get_text(filepath)
    word_count = count_words(text)
    char_count = count_chars(text)
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    for ch, count in sorted(char_count.items(), key=lambda x: x[-1], reverse=True):
        print(f"The '{ch}' character was found {count} times")
    
def main():
    filepath = "books/frankenstein.txt"
    book_report(filepath=filepath)


main()
