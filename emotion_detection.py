import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions']['anger']
        disgust_score = formatted_response['emotionPredictions']['disgust']
        fear_score = formatted_response['emotionPredictions']['fear']
        joy_score = formatted_response['emotionPredictions']['joy']
        sadness_score = formatted_response['emotionPredictions']['sadness']
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        sadness_score = None
        joy_score = None
        fear_score = None
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score}