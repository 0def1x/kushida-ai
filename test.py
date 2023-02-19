import search_words

while True:
    word = str(input(""))
    if word.lower() in search_words.words_talk:
        print("Hello!")
    else:
        print("Bye!")