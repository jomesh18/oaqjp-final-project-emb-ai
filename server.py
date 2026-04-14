"""
This is the server app for the emotion detector app developed
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route('/')
def render_index():
    """ This function renders the index.html """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_detector():
    """ This function gets the text to analyze and returns the output string """
    text_to_analyze = request.args.get('textToAnalyze')
    res_obj = emotion_detector(text_to_analyze)
    if res_obj['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {res_obj['anger']}, \
    'disgust': {res_obj['disgust']}, 'fear': {res_obj['fear']}, 'joy': {res_obj['joy']} and \
    'sadness': {res_obj['sadness']}. The dominant emotion is {res_obj['dominant_emotion']}."

if __name__ == "__main__":
    app.run(port=5000)
