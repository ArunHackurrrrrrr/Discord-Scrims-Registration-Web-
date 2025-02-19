import requests
from datetime import datetime
from Registration_soft.models import OneTimeDatas
def registration_pro(msgtime,scrim_id,uid):
        # data = OneTimeDatas.objects.filter(UserUniqueId = uid)
        current_time = datetime.now()
        url = f"https://discord.com/api/v9/channels/{scrim_id}/messages"
    
        headers = {
            "Authorization": "MTM0MDY2NzU5NTI2NjcxOTc2Nw.Gk5Qz6.3_Br9c_nWvxv3C2QNYI49qca4q6eOT4o3FmUwQ",    
            "Content-Type": "application/json"
        }
# MTExNzgzMzkxODY5NjEyODUxMg.GvYaAS.WztT9Mv0ajNvgZHlnGNh2pzzHzZPRZmoBynSg0

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

