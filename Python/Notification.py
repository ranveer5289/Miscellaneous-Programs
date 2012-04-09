import gntp.notifier

#Class to send notification to growl.

class Notification():

        def __init__(self):

                #create growl object with application name "Loved Track"
                self.growl = gntp.notifier.GrowlNotifier(
                                applicationName = "Loved Track",
                                notifications = ["New Updates","New Messages"],
                                )
                # Register your app "Loved Track" with growl.
                #You can remove the below line once the application is successfully
                #registered.You will get a notification on successful
                #registration.           
                
                #self.growl.register()

        



        #Method to send notification
        def send_Notification(self,track,artist,playcount,code):

                #code to check whether track already loved or not. It's main logic is in "Spotify_last.fm_love.py"
                if code == 1:
                        descp = "Title: {0} \n\n PlayCount: {1}".format(track,playcount)
                elif code == 0:
                        descp = "track already loved on last.fm"

                #Sending notification to growl.        
                self.growl.notify(
                        noteType = "New Messages",
                        title = "Artist: {0}".format(artist),
                        description = descp,
                        #url for notification icon.
                        icon =r"http://aux4.iconpedia.net/uploads/985580273209885575.png",
                        sticky = False,
                        priority = 1,
                        )


