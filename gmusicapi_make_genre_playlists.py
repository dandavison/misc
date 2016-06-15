from gmusicapi import Mobileclient

client = Mobileclient()
assert client.login('dandavison7@gmail.com', PASSWORD, Mobileclient.FROM_MAC_ADDRESS)
tracks = client.get_all_songs()
genres_to_merge = {'Alternative Rock', 'Alt. Rock'}
playlist_track_ids = [t['id'] for t in tracks if t['genre'] in genres_to_merge]
print "Creating playlist with %d tracks" % len(playlist_track_ids)
playlist_id = client.create_playlist('Alt Rock')
client.add_songs_to_playlist(playlist_id, playlist_track_ids)
