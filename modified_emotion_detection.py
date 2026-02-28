def emotion_detector(text_to_analyse):

    # API Call code above here

    if response.status_code == 200:
        formatted_response = response.json()
        emotions = formatted_response['emotion']['document']['emotion']

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }
