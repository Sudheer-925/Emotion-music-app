🎭 Emotion-Based Music Recommendation System

🚀 Project Overview
This project is a real-time AI-based application that detects a user’s facial emotion using computer vision and recommends music accordingly. It provides a personalized music experience by integrating with platforms like YouTube and Spotify.

 🎯 Key Features
- Real-time facial emotion detection using camera  
- Deep Learning model (CNN trained on FER-2013 dataset)  
- Face detection using OpenCV Haar Cascade  
- Multi-language support (20+ languages)  
- Singer-based music recommendation (manual + suggested)  
- Direct music access via YouTube and Spotify  
- Interactive and user-friendly UI using Streamlit  

🛠️ Tech Stack
- Python  
- Streamlit  
- OpenCV  
- TensorFlow / Keras  
- NumPy  

📂 Project Structure
emotion-music-app/
│
├── app.py  
├── haarcascade_frontalface_default.xml  
├── requirements.txt  
└── README.md  

📥 Download Model File

Due to GitHub file size limits, the trained model file is not included in this repository.

👉 Download the model from:
https://drive.google.com/file/d/1qpeEBf7MeM3tdf6FhMXwF5Ouz7U0FtOz/view?usp=drive_link

After downloading, place the file in the project folder:
emotion_model.h5

⚙️ Installation & Setup

1. Clone the repository
git clone https://github.com/your-username/emotion-music-app.git
cd emotion-music-app

2. Install dependencies
pip install -r requirements.txt

3. Run the application
streamlit run app.py

 📸 How It Works
1. Capture an image using the camera  
2. Detect face using OpenCV  
3. Predict emotion using a trained CNN model  
4. Recommend songs based on:
   - Detected emotion  
   - Selected language  
   - Singer preference (optional)  
5. Open songs directly in YouTube or Spotify  

💡 Use Cases
- Mood-based music recommendation  
- Smart entertainment systems  
- Mental wellness applications  

🚀 Future Enhancements
- Live video emotion detection  
- Spotify API integration for direct playback  
- Voice-based input  
- Cloud deployment  

👨‍💻 Author
Sudheer Reddy  
B.Tech CSE (AI & ML)  


## ⭐ Support
If you like this project, give it a star on GitHub!
