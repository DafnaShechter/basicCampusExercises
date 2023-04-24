def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r+') as f:
        lines = f.readlines()
        if len(lines) < 3:
            lines.extend(['\n'] * (3 - len(lines)))
        lines[2] = new_song + ';' + 'Unknown;' + '0:00;\n'
        f.seek(0)
        f.writelines(lines)
    with open(file_path, 'r') as f:
        print(f.read())


my_mp4_playlist(r"c:\songs.txt", "Python Love Story")