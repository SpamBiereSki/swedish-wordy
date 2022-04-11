from json import load, dump


if __name__ == '__main__':
    with open("./data/svenska-ord.json", encoding="utf-8") as ioin:
        all_words = load(ioin)

    words_selected = []
    for word in all_words:
        if len(word) == 5:
            words_selected.append(word)

    with open("./data/selected-words.json", "w+", encoding="utf-8") as ioout:
        dump(words_selected, ioout)
