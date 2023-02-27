from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    email_body = request.json.get('email_body')
    blob = TextBlob(email_body)
    sentiment_score = blob.sentiment.polarity
    sentiment = 'positive' if sentiment_score > 0 else 'negative' if sentiment_score < 0 else 'neutral'
    return jsonify({'sentiment': sentiment, 'sentiment_score': sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)
