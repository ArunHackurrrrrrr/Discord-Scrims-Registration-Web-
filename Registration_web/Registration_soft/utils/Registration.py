import requests
from datetime import datetime
from Registration_soft.models import OneTimeDatas
def registration_pro(msgtime,scrim_id,uid):
        # data = OneTimeDatas.objects.filter(UserUniqueId = uid)
        current_time = datetime.now()
        url = f"https://discord.com/api/v9/channels/{scrim_id}/messages"
    
        headers = {
            "Authorization": "YOUR KEY HERE",    
            "Content-Type": "application/json"
        }
        

        message_content = (
        f"TEAM NAME - ahej\n\n"
        "**PLAYER DETAILS:**\n"
        f"PLAYER 1 IGN:     \n PLAYER UID:- 55514990741\n\n"
        f"Substitute: \n"
        f"Player 5 IGN: DDxSarkar    \n UID: 55539790333\n\n"
        
        "<@1117833918696128512>>\n"
        f"{msgtime}----> This is msg time , {current_time}------> This is current time "
        )

        # Build the payload
        msg = {
        "content": message_content
        }
        response = requests.post(url, headers=headers, json=msg)

        print(response.status_code)
        print(response.json())
        a = str(response.status_code )

