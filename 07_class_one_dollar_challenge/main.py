import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
import datetime
import time
import threading
import dotenv
import os
import google.generativeai as genai

# Initialize TTS engine
engine = pyttsx3.init()


class Jarvis:
    def __init__(self, gemini_api_key, weather_api_key):
        self.reminders = []
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash-002")
        self.weather_api_key = weather_api_key

    def speak(self, text):
        print("Jarvis:", text)
        engine.say(text)
        engine.runAndWait()

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except Exception as e:
            print("Sorry, I couldn't understand that.")
            return ""

    def open_website(self, query):
        websites = {
            "open youtube": "https://youtube.com",
            "open google": "https://google.com",
            "open facebook": "https://facebook.com",
            "open instagram": "https://instagram.com",
            "open linkedin": "https://linkedin.com",
            "open x": "https://x.com",
        }

        for key in websites:
            if key in query:
                self.speak(f"Opening {key}")
                webbrowser.open(websites[key])
                return

        if "google search" in query.lower():
            search_term = query.replace("google search", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            self.speak(f"Searching Google for {search_term}")
        elif "youtube search" in query.lower():
            search_term = query.replace("youtube search", "").strip()
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={search_term}"
            )
            self.speak(f"Searching YouTube for {search_term}")

    def play_youtube_video(self, link):
        if "youtube.com" in link:
            self.speak("Playing the YouTube video.")
            webbrowser.open(link)

    def get_weather(self, city="Karachi"):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
        try:
            res = requests.get(url).json()
            temp = res["main"]["temp"]
            description = res["weather"][0]["description"]
            self.speak(f"Temperature in {city} is {temp}°C with {description}.")
        except Exception as e:
            self.speak("Sorry, I couldn't fetch weather data.")

    def ask_gemini(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            answer = response.text
            self.speak(answer)
        except Exception as e:
            self.speak("Gemini AI service not responding.")

    def set_reminder(self, reminder_text, reminder_time):
        self.reminders.append((reminder_text, reminder_time))
        self.speak(f"Reminder set for {reminder_time}.")

    def check_reminders(self):
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            for reminder in self.reminders:
                if reminder[1] == now:
                    self.speak(f"Reminder: {reminder[0]}")
                    self.reminders.remove(reminder)
            time.sleep(30)

    def run(self):
        threading.Thread(target=self.check_reminders, daemon=True).start()

        self.speak("Hello! I'm Jarvis. say 'Jarvis' to wake me up.")
        while True:
            query = self.listen()

            if "jarvis" in query:
                self.speak("Ya?")
                command = self.listen()

                if "exit" in command or "stop" in command:
                    self.speak("Goodbye!")
                    break
                elif "open" in command or "search" in command:
                    self.open_website(command)
                elif "play video" in command:
                    self.speak("Please paste the YouTube link.")
                    link = self.listen()
                    self.play_youtube_video(link)
                elif "weather" in command:
                    self.get_weather()
                elif "ask ai" in command:
                    self.speak("What do you want to ask?")
                    question = self.listen()
                    self.ask_gemini(question)
                elif "remind me" in command:
                    self.speak("What should I remind you?")
                    text = self.listen()
                    self.speak("At what time? Say in HH:MM format.")
                    time_text = self.listen()
                    self.set_reminder(text, time_text)
                else:
                    self.speak("Sorry, I can't handle that yet.")


# === CONFIGURATION ===
dotenv.load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if __name__ == "__main__":
    jarvis = Jarvis(GEMINI_API_KEY, WEATHER_API_KEY)
    jarvis.run()
