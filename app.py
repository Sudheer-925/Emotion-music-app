import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import urllib.parse

# 🌈 Page config
st.set_page_config(page_title="Emotion Music App", layout="centered")

# 🎨 Clean modern CSS
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
h2 {
    text-align: center;
    color: white;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.song-title {
    font-size: 18px;
    color: white;
    margin-bottom: 10px;
}
.link-btn {
    text-decoration: none;
    padding: 8px 14px;
    border-radius: 8px;
    margin-right: 10px;
    font-weight: bold;
}
.youtube {
    background-color: #ff0000;
    color: white;
}
.spotify {
    background-color: #1db954;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 🎭 Title
st.markdown("<h1>🎭 Emotion-Based Music App</h1>", unsafe_allow_html=True)

# 📦 Load model
model = load_model("emotion_model.h5")

# 👤 Face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# 🌍 Language (20+)
language = st.selectbox(
    "🌍 Choose Language",
    [
        "English", "Telugu", "Hindi", "Tamil", "Kannada",
        "Malayalam", "Punjabi", "Bengali", "Marathi", "Gujarati",
        "Urdu", "Spanish", "French", "German", "Korean",
        "Japanese", "Chinese", "Arabic", "Russian", "Portuguese"
    ]
)

# 🎤 Top singers
top_singers = {
    "Telugu": ["SP Balasubrahmanyam", "Sid Sriram", "Anurag Kulkarni"],
    "Hindi": ["Arijit Singh", "Shreya Ghoshal", "Sonu Nigam"],
    "Tamil": ["Anirudh", "Sid Sriram", "Dhanush"],
    "Kannada": ["Vijay Prakash", "Armaan Malik"],
    "Malayalam": ["KJ Yesudas", "Vineeth Sreenivasan"],
    "Punjabi": ["Diljit Dosanjh", "AP Dhillon"],
    "English": ["Ed Sheeran", "Taylor Swift", "Drake"],
    "Spanish": ["Bad Bunny", "Shakira"],
    "French": ["Indila"],
    "German": ["Rammstein"],
    "Korean": ["BTS", "BLACKPINK"],
    "Japanese": ["LiSA"],
    "Chinese": ["Jay Chou"],
    "Arabic": ["Amr Diab"],
    "Russian": ["Egor Kreed"]
}

# 🎤 Singer selection
st.subheader("🎤 Choose or Enter Singer")

selected_singer = st.selectbox(
    "🎧 Popular Singers",
    ["None"] + top_singers.get(language, [])
)

manual_singer = st.text_input("Or type singer name")

if manual_singer:
    singer = manual_singer
elif selected_singer != "None":
    singer = selected_singer
else:
    singer = None

# 🎵 Base songs
base_music = {
    "Happy": ["Happy songs", "Party songs"],
    "Sad": ["Sad songs", "Emotional songs"],
    "Angry": ["Calm music"],
    "Fear": ["Peaceful music"],
    "Surprise": ["Trending songs"],
    "Neutral": ["Chill music"],
    "Disgust": ["Motivational songs"]
}

# 🎵 Language-specific
language_specific = {
    "Telugu": {"Happy": ["Butta Bomma"], "Sad": ["Samayama"]},
    "Hindi": {"Happy": ["Kesariya"], "Sad": ["Tum Hi Ho"]}
}

# 📷 Camera
img_file = st.camera_input("📷 Capture your emotion")

if img_file is not None:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face = gray[y:y+h, x:x+w]

        face = cv2.resize(face, (48, 48))
        face = face / 255.0
        face = face.reshape(1, 48, 48, 1)

        prediction = model.predict(face)
        emotion = emotion_labels[np.argmax(prediction)]

        # 🖼 Image
        st.image(image, caption="📸 Captured Image", width=350)

        # 😊 Emotion
        st.markdown(f"<h2>😊 {emotion}</h2>", unsafe_allow_html=True)

        # 🤖 Assistant
        responses = {
            "Happy": "🎉 You look happy!",
            "Sad": "💙 Relax with music.",
            "Angry": "😠 Calm down.",
            "Fear": "😟 Stay relaxed.",
            "Surprise": "😲 Enjoy!",
            "Neutral": "😌 Chill."
        }
        st.success(responses.get(emotion, "🎵 Enjoy"))

        # 🎵 Song selection
        if singer:
            songs = [
                f"{singer} songs",
                f"Best of {singer}",
                f"{singer} hits",
                f"{singer} latest songs"
            ]
        elif language in language_specific and emotion in language_specific[language]:
            songs = language_specific[language][emotion]
        else:
            songs = base_music[emotion]

        # 🎵 Display
        st.markdown("<h2>🎵 Play Music</h2>", unsafe_allow_html=True)

        for song in songs:
            query = urllib.parse.quote(song + " " + language)

            youtube_url = f"https://www.youtube.com/results?search_query={query}"
            spotify_url = f"https://open.spotify.com/search/{query}"

            st.markdown(f"""
            <div class="card">
                <div class="song-title">🎶 {song}</div>
                <a href="{youtube_url}" target="_blank" class="link-btn youtube">▶ YouTube</a>
                <a href="{spotify_url}" target="_blank" class="link-btn spotify">🎧 Spotify</a>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.error("❌ No face detected. Try again.")