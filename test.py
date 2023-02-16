test_list = [('we', 7), ('each', 5), ('or', 5), ('need', 5)]


def formatted_results(list):
    format = []
    for spot in list:
        stars = '*' * spot[1]
        line_up = str(spot[0]) + " | " + str(spot[1]) + " " + stars
        format.append(line_up)
    print(format)
    return format


formatted_results(test_list)
