from flask import Flask, render_template, request
import lyricsgenius

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_lyrics():
    # get the input values from the HTML form
    artist = request.form['artist']
    word = request.form['word']
    access_token = request.form['access_token']
    
    # authenticate with the Genius API using the access token
    genius = lyricsgenius.Genius(access_token)
    
    # search for the artist
    search_result = genius.search_artist(artist, max_songs=50)
    
    # create an empty list to store the lyrics
    lyrics_list = []
    
    # loop through each song by the artist
    for song in search_result.songs:
        # check if the lyrics contain the specific word
        if word in song.lyrics:
            # add the lyrics to the list
            lyrics_list.append(song.lyrics)
    
    # join the lyrics in the list into a single string separated by two newlines
    lyrics = '\n\n'.join(lyrics_list)
    
    # render the lyrics in the HTML template
    return render_template('index.html', lyrics=lyrics)

if __name__ == '__main__':
    app.run(debug=True)
