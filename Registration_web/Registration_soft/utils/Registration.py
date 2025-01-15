import requests
from datetime import datetime
def registration_pro(msgtime,scrim_id):
        current_time = datetime.now()
        url = f"https://discord.com/api/v9/channels/{scrim_id}/messages"
    
        headers = {
            "Authorization": "MTExNzgzMzkxODY5NjEyODUxMg.GvYaAS.WztT9Mv0ajNvgZHlnGNh2pzzHzZPRZmoBynSg0",    
            "Content-Type": "application/json"
        }


        message_content = (
        "TEAM NAME - DARK DYNASTY\n\n"
        "**PLAYER DETAILS:**\n"
        "PLAYER 1 IGN: DDxSouLsGOD \n PLAYER UID :- 55500148681\n\n"
        "PLAYER 2 IGN: DDxCOPYCAT   \n PLAYER UID:- 55505309777\n\n"
        "PLAYER 3 IGN: DDxARUN      \n PLAYER UID:- 55600311304\n\n"
        "PLAYER 4 IGN: DVxZEUS      \n PLAYER UID:- 55514990741\n\n"
        "Substitute: \n"
        "Player 5 IGN: DDxSarkar    \n UID: 55539790333\n\n"
        
        "<@896979044837511188>\n"
        "<@1117833918696128512>\n"
        "<@975042201937657927>\n"
        "<@691313191824785459>\n\n"
        f"{msgtime}----> This is msg time , {current_time}------> This is current time , aur agar msg late aa raha hai to webhostmost ki ma ki choot"
        )

        # Build the payload
        msg = {
        "content": message_content
        }
        response = requests.post(url, headers=headers, json=msg)

        print(response.status_code)
        print(response.json())
        a = str(response.status_code )

