def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

print("Masukkan data album (ketik 'quit' kapan saja untuk berhenti).")

while True:
    artist = input("Nama Artis: ")
    if artist.lower() == 'quit':
        break
        
    title = input("Judul Album: ")
    if title.lower() == 'quit':
        break
        
    user_album = make_album(artist, title)
    print("\nAlbum yang dibuat:")
    print(user_album)
    print("-" * 30)