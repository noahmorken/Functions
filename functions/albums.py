def make_album(artist_name, album_name, num_songs=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name, 'album': album_name}
    if num_songs:
        album['number of songs'] = num_songs
    return album

album = make_album('The Beatles', 'Abbey Road', '16')
print(album)
album = make_album('Nirvana', 'Nevermind', '40')
print(album)
album = make_album('The Beach Boys', 'Pet Sounds', '13')
print(album)

while True:
    print("\nPlease input your album:")
    print("(enter 'q' at any time to quit)")
    
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    num_songs = input("Number of songs: ")
    if num_songs == 'q':
        break

    complete_album = make_album(artist, album, num_songs)
    print(f"\nYour album's complete dictionary is {complete_album}.")