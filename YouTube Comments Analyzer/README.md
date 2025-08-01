# 📊 YouTube Comments Sentiment Analysis

This project analyzes the sentiment of YouTube comments using **TextBlob** and **BERT-based transformers**. It classifies comments as **Positive, Negative, or Neutral**, and visualizes the distribution.

## 🚀 Features
- ✅ Fetches comments from a YouTube video using the **YouTube Data API v3**.
- ✅ Performs **sentiment analysis** using **TextBlob** and **BERT**.
- ✅ Visualizes sentiment distribution using **Matplotlib & Seaborn**.
- ✅ Identifies **most frequently used Positive & Negative comments**.
- ✅ Determines the **overall impact** of the video.

## 🛠️ Installation

To run this project, install the required dependencies:

```bash
pip install google-api-python-client pandas textblob nltk requests streamlit pyngrok transformers
```
### 📝 Usage
1.Run the script:
``` bash
python youtube_comments_sentimate_analysis.py

```
2.Enter the YouTube Video ID when prompted.
3.View sentiment distribution and most frequent comments.

### 📌 Example Output
```bash
Enter the YouTube video ID: VrU_uFCwXX8
Analyzed 100 comments.

Most Used Positive Comments:
- Great video! (used 10 times)
- Very informative! (used 8 times)

Most Used Negative Comments:
- Poor audio quality (used 5 times)
- Boring content (used 3 times)

Overall Video Impact: Positive Impact
```
### 📊 Visualization

The script generates a sentiment distribution graph:

✔️ Green → Positive

✔️ Pink → Neutral

✔️ Blue → Negative

### 🔑 API Key Setup
Replace API_KEY in the script with your YouTube Data API v3 key.
```bash
API_KEY = 'YOUR_YOUTUBE_API_KEY'
```
### 🖥️ Running the Streamlit App
Run the interactive Streamlit dashboard:

```bash
streamlit run youtube_comments_sentimate_analysis.py

```
### 🏗️ Technologies Used

-Python 🐍

-Google API Client (YouTube Data API v3)

-TextBlob (Sentiment Analysis)

-BERT (Transformers)

-Matplotlib & Seaborn (Visualization)

-Streamlit (Dashboard UI)


🎯 Developed by Riddhi 💡
