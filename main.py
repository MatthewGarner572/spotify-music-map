import tekore as tk



client_id = "8e8994a3baf14c97885d5cf7c8f5b709"
client_secret = "b38a1f1e8cdc406581326aff849b0c59"
redirect_uri = "http://localhost:8888/callback"


user_token = tk.prompt_for_user_token(
    client_id,
    client_secret,
    redirect_uri,
    scope=tk.scope.every
)


spotify = tk.Spotify(user_token)

tracks = spotify.current_user_top_tracks(limit=50, time_range="long_term")
for track in tracks.items:
    print(track.name)
print()
print("/////////////////////")
print()
artist = spotify.current_user_top_artists(limit=50, time_range="long_term")
for artist in artist.items:
    print(artist.name)

