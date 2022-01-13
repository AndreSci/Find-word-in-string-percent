""" search for a word with a selected percentage """


def find_word_per(line_1, line_2, percent=100):
    max_found = 0

    for item_1 in range(len(line_1)):

        for item_2 in range(len(line_2)):
            index_found = 0

            if line_1[item_1] == line_2[item_2]:

                for index in range(len(line_2) - item_2):
                    if item_1 + index >= len(line_1):
                        break
                    elif line_1[item_1 + index] == line_2[item_2 + index]:
                        index_found += 1
            if max_found < index_found:
                max_found = index_found

    result_per = (100 / len(line_1)) * max_found

    return result_per >= percent


def test_find(w1, w2, percent):
    result = find_word_per(w1, w2, percent)
    print(f"Test: {percent}% {result}")


def test_01():
    test_find("words_list", "words_list", 100)  # True
    test_find("words_list", "12312312words_list", 100)  # True
    test_find("words_list", "12312312words_li", 80)  # True
    test_find("words_list", "12312312words", 50)  # True
    test_find("words_list", "words", 50)  # True


if __name__ == "__main__":
    test_01()

