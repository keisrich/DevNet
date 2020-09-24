"""
Using Webex Teams API to create a new webex room called DevNet High, 
post a message to the newly created room.
Includes error detection. 
"""

import requests
import json

myWebexToken = "XXXXXXXXXXXXXX"  # your personal token
WebexRoomID = ""
room_url = "https://webexapis.com/v1/rooms"
message_url = "https://webexapis.com/v1/messages"

room_data = {  ## create a webex teams room called DevNet High
    "title": "DevNet High 2020"
}

message_data = {  ## post a message to the newly created room
    "roomId": WebexRoomID,
    "text": "Welcome to the Webex Teams API!"
}

header = {
    "Authorization": "Bearer" + myWebexToken,  # api key header
    "Accept": "application/json",  # specify json content type header
    "Content-Type": "application/json"  # accept json response header
}


def post_message():
    """
    Post text to newly created room.
    """
    rsp = requests.post(room_url/{WebexRoomID}, headers=header, data=message_data)  ##post to room
    message_dict = json.loads(rsp.text)  ##store json response
    webex_msg = message_dict['text']
    print(f"{webex_msg} was successfully displayed in the {room_data['title']} space.")  ##display confirmation


if __name__ == '__main__':
    """
    Main method which creates the room and calls the post_message() method.
    Error detection prints message if room was not created.
    """
    response = requests.post(message_url, headers=header, data=room_data)  ##create room

    if response.status_code == 200:
        text = json.loads(response.text)  ##store json response
        WebexRoomID = text['id']  ##get room id for later
        post_message()  ##post method
    else:
        print(response.text)
        print('An error occurred')  ##error detection

    print("done!")
