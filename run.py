from helpers.graph import convert_into_word, find_paths, is_word

adj_matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1, 0, 0],
              [1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 0],
              [0, 4, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1, 1, 0, 1],
              [0, 0, 0, 0, 0, 1, 1, 0]]

vertex_dict = {
    0: "p",
    1: "p",
    2: "o",
    3: "n",
    4: "r",
    5: "c",
    6: "o",
    7: "k",
}


path_list = list(find_paths(adj_matrix))
english_words = []

for path in path_list:
    word = convert_into_word(path, vertex_dict)
    if is_word(word):
        if word not in english_words:  # avoiding duplicate words
            english_words.append(word)

print(english_words)
