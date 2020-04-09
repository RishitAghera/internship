def find_anagrams(word, candidates):
    list_word = sorted(list(word.lower()))
    return list(filter(lambda option: sorted(list(option.lower())) == list_word and word.lower() != option.lower(), candidates))


# print(find_anagrams("LISTEN", ["Listen", "Silent", "LISTEN"]))
