def count_letters(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def format_report(letter_dict):
    count_list = []
    for k, v in letter_dict.items():
        if k.isalpha() and len(k) == 1:
            # count_list.append({f"{k}": v})
            count_list.append({"name": k, "num": v})
    # print(count_list)
    count_list.sort(key=sort_on, reverse=True)
    return count_list




def main():
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
        words = text.split()
        print(len(words)) # prints the whole text

        total_letter_count = count_letters(text)
        # print(total_letter_count)
        dict_list = format_report(total_letter_count)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document.")
        for i in dict_list:
            print(f"The letter '{i['name']}' appears {i['num']} times")
        print("--- End report ---")


if __name__ == "__main__":
    main()
