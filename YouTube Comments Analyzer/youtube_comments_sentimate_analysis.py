# -*- coding: utf-8 -*-
"""Youtube comments sentimate analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18o941MhcdEcQT4BHOCtBcifnepMgLOU4
"""

pip install google-api-python-client pandas textblob nltk requests

!pip install streamlit
!pip install pyngrok

from googleapiclient.discovery import build
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import pipeline
import streamlit as st
from collections import Counter

# Replace with your own API key
API_KEY = 'AIzaSyApL52wDY4m9LTVazepPHEKNmVSjNso25Y'

# Initialize YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id, max_results=100):
    """
    Fetches comments from a YouTube video.
    :param video_id: ID of the YouTube video
    :param max_results: Number of comments to fetch
    :return: List of comments
    """
    comments = []
    try:
        results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        ).execute()

        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
    except Exception as e:
        st.error(f"Error fetching comments: {e}")

    return comments

def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)
        sentiments.append(sentiment)

    return sentiments

def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def plot_sentiment_distribution(sentiments):
    """
    Plots the distribution of sentiments with color coding for Positive, Neutral, and Negative.
    :param sentiments: List of classified sentiments
    """
    plt.figure(figsize=(8, 6))

   # Create a color map based on sentiment types
    colors = ['green', 'pink', 'blue']  # Order: Positive, Negative, Neutral
    color_map = {
    'Positive': 'green',
    'Negative': 'blue',
    'Neutral': 'pink'
}


    sns.countplot(x=sentiments, palette=colors)

    plt.title('Sentiment Distribution (Positive, Neutral, Negative)', fontsize=16)
    plt.xlabel('Sentiment', fontsize=14)
    plt.ylabel('Count', fontsize=14)

    plt.show()

    st.pyplot(plt)

def get_most_frequent_comments(comments, sentiments, sentiment_type, top_n=5):
    """
    Get the most frequently used positive or negative comments.
    :param comments: List of comments
    :param sentiments: List of corresponding sentiments for the comments
    :param sentiment_type: 'Positive' or 'Negative' to filter comments
    :param top_n: Number of top frequent comments to return
    :return: List of most frequent comments
    """
    filtered_comments = [comment for comment, sentiment in zip(comments, sentiments) if sentiment == sentiment_type]
    comment_counter = Counter(filtered_comments)
    return comment_counter.most_common(top_n)

# Initialize sentiment analysis pipeline
classifier = pipeline('sentiment-analysis')

# Analyze sentiment using BERT
def analyze_sentiment_bert(comments):
    return [classifier(comment)[0]['label'] for comment in comments]

def determine_overall_impact(classified_sentiments):
    """
    Determines whether the overall impact of the video is positive, neutral, or negative.
    :param classified_sentiments: List of classified sentiments ('Positive', 'Neutral', 'Negative')
    :return: Overall impact as a string
    """
    sentiment_counts = Counter(classified_sentiments)

    positive_count = sentiment_counts['Positive']
    neutral_count = sentiment_counts['Neutral']
    negative_count = sentiment_counts['Negative']

    st.write(f"Positive comments: {positive_count}")
    st.write(f"Neutral comments: {neutral_count}")
    st.write(f"Negative comments: {negative_count}")

    # Determine the overall impact based on the most frequent sentiment
    if positive_count > negative_count:
        return 'Positive Impact'
    elif negative_count > positive_count:
        return 'Negative Impact'
    else:
        return 'Neutral Impact'

def main():
    """
    Main function to fetch comments, analyze sentiment, and plot sentiment distribution.
    """

    # User input for YouTube video ID
    video_id = input("Enter the YouTube video ID: ")  # Example: 'VrU_uFCwXX8'

    if video_id:
        # Fetch comments
        comments = get_comments(video_id)

        if not comments:
            print("No comments found.")
            return

        # Analyze sentiment using TextBlob
        sentiments = analyze_sentiment(comments)
        classified_sentiments = [classify_sentiment(p) for p in sentiments]

        # Display the results
        print(f"\nAnalyzed {len(comments)} comments.")
        plot_sentiment_distribution(classified_sentiments)

        # Most frequent positive and negative comments
        most_used_positive = get_most_frequent_comments(comments, classified_sentiments, 'Positive', top_n=5)
        most_used_negative = get_most_frequent_comments(comments, classified_sentiments, 'Negative', top_n=5)

        print("\nMost Used Positive Comments:")
        for comment, count in most_used_positive:
            print(f"{comment} (used {count} times)")

        print("\nMost Used Negative Comments:")
        for comment, count in most_used_negative:
            print(f"{comment} (used {count} times)")

        # Determine and display overall impact
        overall_impact = determine_overall_impact(classified_sentiments)
        print(f"\nOverall Video Impact: {overall_impact}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

