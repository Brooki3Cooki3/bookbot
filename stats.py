def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def character(text_string):
    counter = {} 
    for letter in text_string:
        lower = letter.lower()
        if lower in counter:
            counter[lower] += 1
        else:
            counter[lower] = 1
    return counter

def sort_on(items):
    return items["num"]

def sorted_hat(characters):
    diclist = []
    for key,value in characters.items():
        newdic = {}
        newdic["char"] = key
        newdic["num"] = value
        diclist.append(newdic)
    diclist.sort(reverse=True, key=sort_on)
    return diclist
        