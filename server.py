from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_detecte = request.args.get('textToDetecte')
    emotion = emotion_detector(text_to_detecte)
    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion ['sadness']
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness':{}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)