test_list = [('we', 7), ('each', 5), ('or', 5), ('need', 5)]


# def formatted_results(list):
#     format = []
#     for spot in list:
#         stars = '*' * spot[1]
#         line_up = str(spot[0]) + " | " + str(spot[1]) + " " + stars
#         format.append(line_up)
#     # print(format)
#     for part in format:len(part)
#     return format

# formatted_results(test_list)


def formatted_results(list):
    formatted = []
    max_len = max(len(spot[0]) for spot in list)
    for spot in list:
        stars = '*' * spot[1]
        col1 = spot[0].rjust(max_len)
        col2 = str(spot[1]).rjust(2)
        line_up = f"{col1} | {col2} {stars}"
        formatted.append(line_up)
    return formatted


format = formatted_results(test_list)
for line in format:
    print(line)
