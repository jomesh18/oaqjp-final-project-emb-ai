import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=my_obj, headers=header)
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    res = json.loads(response.text)
    emotions = res['emotionPredictions'][0]['emotion']
    curr_max, dominant_emotion = float('-inf'), 'anger'
    for key, val in emotions.items():
        if val > curr_max:
            curr_max = val
            dominant_emotion = key
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
