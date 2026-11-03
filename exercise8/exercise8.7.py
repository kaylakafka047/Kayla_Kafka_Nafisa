def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun dictionary yang mendeskripsikan sebuah album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

album1 = make_album('sheila on 7', 'kisah klasik untuk masa depan')
album2 = make_album('taylor swift', 'fearless', 10)
album3 = make_album('dewa 19', 'laskar cinta')

print(album1)
print(album2)
print(album3)