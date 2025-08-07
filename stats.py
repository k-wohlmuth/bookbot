def work_count(book):
    return len(book.split())


def char_count(book):
    book_lower = book.lower()
    ch_count = { }
    for i in book_lower:
        if i in ch_count:
            ch_count[i] += 1
        else:
            ch_count[i] = 1
    return ch_count

def sort_dict(dic):
    result = []
    for char, num in dic.items():
        entry = {"char": char, "num": num}
        result.append(entry)

    result.sort(reverse=True, key=lambda x: x["num"])
    return result

