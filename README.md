# 🧠 Jarvis AI Assistant
Jarvis is a Python-based voice assistant that can respond to voice commands to perform various tasks such as opening websites, telling the date/time, launching applications, searching the web, playing YouTube videos, reporting news and weather, and more.

## 🔧 Features
- 🎤 Voice recognition using SpeechRecognition

- 🗣️ Text-to-speech responses using pyttsx3

- 📅 Tells the current time and date

- 🌐 Opens popular websites (Google, YouTube, Instagram, Wikipedia)

- 📂 Launches local applications (Notepad, Camera, Command Prompt, MS Word)

- 🔍 Performs voice-based search on:

   - YouTube

   - Google

   - Wikipedia

- 📰 Fetches and reads latest news headlines using NewsAPI

- 🌤️ Gives real-time weather reports using OpenWeather API

- 🔁 Repeats whatever you say

- 🙋‍♀️ Personalized greetings using your name and assistant name from .env

## 📦 Dependencies
Install all required Python libraries using pip:

pip install -r requirements.txt

## 📁 Project Structure

Jarvis/
│
├── main.py              # Main driver script (your Jarvis code)
├── online.py            # Handles internet-based tasks (YouTube, news, weather, etc.)
├── conv.py              # Stores finetext and goodbye responses
├── .env                 # Stores API keys and config variables
├── requirements.txt     # List of Python dependencies

## 🔐 Environment Variables
Create a .env file in the root directory and add: 

USER=YourName
BOT=Jarvis
NEWS_API=your_newsapi_key_here

## ▶️ How to Run

python main.py
Jarvis will greet you based on the time of day and start listening for your commands.

🎙 Example Commands
You can try saying:

Open YouTube

Search on YouTube

Search on Google

Search on Wikipedia

What is the time?

Tell me news

What's the weather like?

Open command prompt

Repeat after me

Stop or Exit or Bye to close Jarvis

❗ Notes
Ensure your microphone is working for voice commands to be detected.

The assistant only activates once you speak after it says "Listening..."

Some paths like MS Word may need to be updated based on your system.

🛠️ To-Do Ideas (Optional)
Add GPT-based conversation ability (via OpenAI API)

Add music player, alarm, or email functionality

## 🙌 Author Aaima Farrukh 
CS Student | Passionate about AI & ML
