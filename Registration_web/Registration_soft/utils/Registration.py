import requests
def registration_pro(scrim_id):
        url = f"https://discord.com/api/v9/channels/{scrim_id}/messages"
    
        headers = {
            "Authorization": "MTExNzgzMzkxODY5NjEyODUxMg.GvYaAS.WztT9Mv0ajNvgZHlnGNh2pzzHzZPRZmoBynSg0",    
            "Content-Type": "application/json"
        }

        msg = {
            'content': 'TEAM NAME : SUGARx <@1117833918696128512> <@896979044837511188> <@1216632380815573035> <@745564134103318539> '
        }

        response = requests.post(url, headers=headers, json=msg)

        print(response.status_code)
        print(response.json())
        a = str(response.status_code )

