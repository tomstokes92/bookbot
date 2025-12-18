def word_count(text):
    word_count = len(text.split())
    return word_count

def character_count(text):
    characters = {}
    for i in text:
        standard = i.lower()
        if standard not in characters:
            characters[standard] = 1
        else:
            characters[standard] += 1
    return characters

def sorted_characters(character_counts):
    char_list = []
    for char, count in character_counts.items():
        char_list.append({
            "char": char, 
            "num": count
        })
    def sort_on(item):
        return item["num"]
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list