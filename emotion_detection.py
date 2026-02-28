import requests

def emotion_detector(text_to_analyse):

    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2022-04-07"
    
    headers = {
        "Content-Type": "application/json"
    }

    input_json = {
        "text": text_to_analyse,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    return response.json()
