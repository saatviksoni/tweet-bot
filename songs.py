def lyrics():
    import lyricsgenius 
    from dotenv import load_dotenv
    import os 
    from random import randint
   
    load_dotenv()
    genius = lyricsgenius.Genius(os.environ.get('genius_access_token'))  # import class and initate class
    genius.remove_section_headers = True
    genius.excluded_terms = ["(Remix)", "(Live)"]

    lst_songs = []
    with open('songs.txt') as file:    
        for i in range(68):    
            song = file.readline()
            lst_songs.append(song.rstrip('\n'))

    songs = {key:value for key,value in zip(range(68), lst_songs)}
    songs_done = []

    temp = randint(0,56)
    artist_song = songs[temp]
    artist_name = 'Lana Del Rey'

    with open('lyrics.txt', 'w') as file:
        file.write(genius.search_song(artist_song, artist_name).lyrics)