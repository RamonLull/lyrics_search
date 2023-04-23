from flask import Flask, render_template, request, redirect
import lyricsgenius

app = Flask(__name__)
word, artist, search_result = None, None, None



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inquiry', methods=['POST','GET'])
def check_artist_name():
    if request.form['submit_button'] == 'Evet':
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
    else:
        return "lol"


@app.route('/get_lyrics', methods=['POST'])
def get_lyrics():
    global search_result, artist, word
    # get the input values from the HTML form
    artist = request.form['artist']
    word = request.form['word']
    access_token = "vBzal6SKsuLALoUsRkUZDqXxwD7ooJtUi4RgMcfoAOImsYlGA_emercol_H_F__N"

    # authenticate with the Genius API using the access token
    genius = lyricsgenius.Genius(access_token)

    # search for the artist
    search_result = genius.search_artist(artist, max_songs=1)
    search_result.save_lyrics()
    return render_template('inquiry.html', artist_name=search_result.name)


if __name__ == '__main__':
    app.run(debug=True)
