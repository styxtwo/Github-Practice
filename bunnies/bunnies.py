def print_bunny_pyramid():
    word = "BUNNY"
    for i in range(1, 6):
        spaces = "   " * (5 - i)
        layer_word = " ".join([word] * i)
        print(spaces + layer_word + spaces)

print_bunny_pyramid()