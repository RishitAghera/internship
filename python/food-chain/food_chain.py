def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse+1):
        verses.extend(recite_one_verse(i-1))

    return verses[:-1:]


def recite_one_verse(i):
    comment = ["",
               "It wriggled and jiggled and tickled inside her.",
               "How absurd to swallow a bird!",
               "Imagine that, to swallow a cat!",
               "What a hog, to swallow a dog!",
               "Just opened her throat and swallowed a goat!",
               "I don't know how she swallowed a cow!",
               "She's dead, of course!"
               ]
    animal = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

    verse = []
    start = f"I know an old lady who swallowed a {animal[i]}."
    verse.append(start)
    # Not a fly
    if i != 0:
        verse.append(comment[i])
    # She is dead by horse, verse ends here
    if i == 7:
        verse.append("")
        return verse

    for j in range(i, 0, -1):
        reason = f"She swallowed the {animal[j]} to catch the {animal[j-1]}"
        if j == 2:
            reason += " that wriggled and jiggled and tickled inside her"
        verse.append(reason+".")

    end = "I don't know why she swallowed the fly. Perhaps she'll die."
    verse.append(end)
    verse.append("")
    return verse