"""
Using Webex Teams API to create a new webex room called DevNet High, 
post a message to the newly created room.
Includes error detection. 
"""

import requests
import json

myWebexToken = " "  # your personal token
WebexRoomID = " "
room_url = "https://webexapis.com/v1/rooms"
message_url = "https://webexapis.com/v1/messages"

room_data = {  ## create a webex teams room called DevNet High
    
}

message_data = {  ## post a message to the newly created room
    
}

header = {
    # api key authorization header 
}


def post_message():
    """
    Post text to newly created room.
    Display a confirmation message on the console with message and room name text
    """
    
    rsp = requests.SOMETHING(message_url, headers=header, data=message_data)  ##post to room
     


if __name__ == '__main__':
    """
    Main method which creates the room and calls the post_message() method.
    Error detection prints message if room was not created.
    """
    response = requests.SOMETHING(room_url, headers=header, data=room_data)  ##create room

    if response.SOMETHING == 200:
        
        WebexRoomID = text['id']  ## **hint - get room id for later**
        post_message()  ##post method
    else:
        print('An error occurred')  ##error detection
