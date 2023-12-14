import lyricsgenius
import json
import os
import credentials

from translateEnLyricstoUa import translate_lyrics
client_access_token = credentials.genius_api_key
print(client_access_token)
genius = lyricsgenius.Genius(client_access_token, remove_section_headers=True, skip_non_songs=True)

def collect_songs(artist, nb_songs):
    artist_genius = genius.search_artist(artist, max_songs = nb_songs, sort='popularity')
    songs = artist_genius.songs
    return songs


def songs_lyrics(songs):
    song_number = 0
    # json_object = {}
    for song in songs:
        if song is not None:
            song_number += 1
            genre =
            translation = translate_lyrics(song.lyrics)
            dictionary = {"title": song.title,
                          "lyrics": song.lyrics,
                          "translation": translation}
            json_object = json.dumps(dictionary, indent=4)
        # write_json(y)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return


