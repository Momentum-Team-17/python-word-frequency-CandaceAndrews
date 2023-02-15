def test_bank():
    filtered_list = []
    with open("simple-test-file.txt") as word_txt:
        for spot in word_txt:
            word = spot.split(" ")
            filtered_list.append(word)
        print(filtered_list)


test_bank()
