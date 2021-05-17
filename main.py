import tekore as tk
import csv
import codecs

x = 0

def main():

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
    
    topTracks = []
    topTracksAllTime = getTopTracks(spotify, "long_term")
    topTracks6Months = getTopTracks(spotify, "medium_term")
    topTracks4Weeks = getTopTracks(spotify, "short_term")
    topTracks.append(topTracksAllTime)
    topTracks.append(topTracks6Months)
    topTracks.append(topTracks4Weeks)
    
    write(topTracks)


def write(topTracks):
    with codecs.open('topTracks.csv', mode='w', encoding='utf8') as trackFile:
        track_writer = csv.writer(trackFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        track_writer.writerow(["Song Name","Rank", "Group"])
        for i in range(len(topTracks)):
            for j in range(len(topTracks[i])-1):
                track_writer.writerow([topTracks[i][j],50-j, topTracks[i][-1]])
        
        

def getTopTracks(spotify, time_range):
    topTracks = []
    tracks = spotify.current_user_top_tracks(limit=50, time_range=time_range)
    for track in tracks.items:
        topTracks.append(track.name)
    topTracks.append(time_range)
    return topTracks

##artist = spotify.current_user_top_artists(limit=50, time_range="long_term")
##for artist in artist.items:
##    print(artist.name)








if __name__ == "__main__":
    main()

