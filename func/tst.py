def make_album(artist,title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict
art=input()
tit=input()
album = make_album(art, tit)
print(album)