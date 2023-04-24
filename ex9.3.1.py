def my_mp3_playlist(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    # remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # calculate number of songs
    num_songs = len(lines)

    # get names of all songs
    song_names = [line.split(";")[0] for line in lines]

    # find longest song
    longest_song = max(lines, key=lambda x: int(x.split(";")[2].replace(":", "")))
    longest_song_name = longest_song.split(";")[0]

    # find most common performer
    performers = [line.split(";")[1] for line in lines]
    most_common_performer = max(set(performers), key=performers.count)

    return (longest_song_name, num_songs, most_common_performer)


print(my_mp3_playlist(r"c:\songs.txt"))