def recite(start, take=1):
    song = []
    for counter in range(start, start - take, -1):
        if len(song) > 0:
            song.append("")

        if counter > 2:
            song.append(str(counter) + " bottles of beer on the wall, " + str(counter) + " bottles of beer.")
            song.append("Take one down and pass it around, " + str(counter - 1) + " bottles of beer on the wall.")
        elif counter == 2:
            song.append(str(counter) + " bottles of beer on the wall, " + str(counter) + " bottles of beer.")
            song.append("Take one down and pass it around, " + str(counter - 1) + " bottle of beer on the wall.")
        elif counter == 1:
            song.append("1 bottle of beer on the wall, 1 bottle of beer.")
            song.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif counter == 0:
            song.append("No more bottles of beer on the wall, no more bottles of beer.")
            song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
            break
    return song

print(recite(start=2, take=3))
