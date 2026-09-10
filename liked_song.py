liked_songs = {
    'title': 'Shape of You',
    'artist': 'Ed Sheeran'
}

def write_liked_song_to_file(liked_songs, filename):
    with open(filename, 'w') as file:
        file.write(f"""
        Liked Songs:
        {liked_songs['title']} by {liked_songs['artist']}
        """)

write_liked_song_to_file(liked_songs, 'playlist.txt')