from pytify import Spotify
import subprocess
import pylast
import Notification

#Go to http://www.last.fm/api/account and get the below mentioned fields to
#authenticate yourself.

API_KEY = 'ccd0f44abca06820ffd452952d488177'
API_SECRET = '8ea68dc5ec3585ea50565e53682a98e0'

#Last.fm username and md5 password hash.
username = 'ranveer5289'
password_hash = 'd8578edf8458ce06fbc5bb76a58c5ca4'

#A Last.fm network object
network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
                API_SECRET, username = username, password_hash = password_hash)

#Create Spotify object
spotify = Spotify()

# Get current playing track on spotify.
track_name = spotify.getCurrentTrack()
print track_name.lower()

# Get current playing artist on spotify.
artist_name = spotify.getCurrentArtist()

#Return a track object.
track_2_love = network.get_track(artist_name,track_name)

#Adds the track to the user's loved tracks
track_2_love.love()

#Return User Object
user_object = network.get_user(username)

#Return the last loved track
loved_track_list = user_object.get_loved_tracks(1)

#Return user's total playcount
playcount = user_object.get_playcount()
print playcount

#Get artist - track in unicode format
last_loved_track = str(loved_track_list[0][0])

#Get last loved artist,track name
artist,track = last_loved_track.split(' - ')
print track.lower()



# call Notificatin class from Notification.py to create notification object
notification = Notification.Notification()

#Check if track loved previously or not than
#send notification.

if track_name.lower() == track.lower():

        notification.send_Notification(track,artist,playcount,1)
else:

        notification.send_Notification(track,artist,playcount,0)
