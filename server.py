''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the responce for the provided text.
    '''
    text_to_detecte = request.args.get('textToDetecte')
    emotion = emotion_detector(text_to_detecte)
    anger_score = emotion['anger']
    disgust_score = emotion['disgust']
    fear_score = emotion['fear']
    joy_score = emotion['joy']
    sadness_score = emotion ['sadness']
    dominant_emotion = joy_score
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return "For the given statement, the system response is 'anger': {},"+\
        "'disgust': {}, 'fear': {}, 'joy': {},'sadness':{} and 'dominant_emotion':{}.".format+\
        (anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion )

@app.route("/")
def render_index_page():
    '''
         This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
