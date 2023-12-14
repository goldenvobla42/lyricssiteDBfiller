#import parserEnLyrics
# This is a sample Python script.
import parserEnLyrics


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def main():
    songs = parserEnLyrics.collect_songs("salvador sobral", 2)
    parserEnLyrics.songs_lyrics(songs)

if __name__ == "__main__":
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
