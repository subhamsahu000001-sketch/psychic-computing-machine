# psychic-computing-machine
Python Desktop Projects Collection
This repository contains a collection of desktop applications built using Python and tkinter. These projects range from utility tools like calculators and password generators to more complex applications involving API integration and voice recognition.

📁 Projects Included
Basic Weather App: A GUI application to fetch real-time weather data for various cities.
BMI Calculator: A tool to calculate Body Mass Index and determine health categories.
Password Generator: A secure utility to generate random passwords with customizable criteria.
Voice Assistant: A desktop assistant capable of voice commands, web searching, and system control.
1️⃣ Basic Weather App
A weather forecasting application that allows users to select a city (with autocomplete support) and view current weather details including temperature, humidity, wind speed, and pressure.

Features
City Autocomplete: Start typing a city name to see suggestions from a predefined list.
Real-time Data: Fetches live data from OpenWeatherMap.
Unit Conversion: Displays temperature in both Celsius and Fahrenheit.
Dependencies
tkinter (usually built-in)
requests
Setup & Usage
Install the required library:
bash

pip install requests
Run the script:
bash

python Basic_weather_app.py
Note: This script uses a demo API key. For consistent usage, register at OpenWeatherMap and replace the api_key variable in the code with your own key.
2️⃣ BMI Calculator
A simple graphical interface to calculate Body Mass Index (BMI) based on height and weight inputs.

Features
Metric Units: Accepts height in centimeters and weight in kilograms.
Health Categories: Classifies the result as Underweight, Normal weight, Overweight, or Obese.
Input Validation: Ensures positive numerical values are entered.
Dependencies
tkinter (usually built-in)
Setup & Usage
Run the script directly:
bash

python BMI_Calculator.py
Enter your height and weight and click "Calculate BMI".
3️⃣ Simple Password Generator
A robust tool to create strong, random passwords tailored to user requirements.

Features
Customizable Length: Set the desired length of the password.
Character Selection: Toggle inclusion of Uppercase, Lowercase, Digits, and Symbols.
Clipboard Support: One-click copy to clipboard functionality.
UI Animations: Includes interactive hover effects on buttons.
Dependencies
tkinter (usually built-in)
pyperclip
Setup & Usage
Install the required library:
bash

pip install pyperclip
Run the script:
bash

python Simple_Password_Generator.py

4️⃣ Voice Assistant (Jarvis)
An intelligent voice assistant named "Jarvis" that interacts with the user via speech recognition and text-to-speech. It can perform web searches, open applications, tell the time, and manage system tasks.

Features
Greeting: Wishes the user based on the time of day.
Web Control: Opens YouTube, Google, and performs search queries (including in Hindi and Gujarati).
System Control: Opens Notepad, Calculator, CMD, and can Shutdown/Restart the PC.
Wikipedia Integration: Summarizes topics from Wikipedia.
Email: Can send emails via voice command (requires configuration).
Dependencies
pyttsx3
speech_recognition
pyautogui
wikipedia
pyaudio (Often required for microphone access)
Setup & Usage
Install the required libraries:
bash

pip install pyttsx3 speech_recognition pyautogui wikipedia
# If you face microphone errors, try installing pyaudio:
# pip install pyaudio
Configuration: Open Voice_Assistant.py and update the following lines with your own details for the email feature to work:
python

email_dict = {"friend": "friend@example.com", "family": "family@example.com"}
server.login('your_email@gmail.com', 'your_password')
Run the script:
bash

python Voice_Assistant.py
Voice Commands
"Open YouTube" / "Open Google"
"Search Google for [query]"
"Play music"
"Time"
"Send email to [contact]"
"Shutdown" / "Restart"
"Exit"
⚙️ Global Installation
To install dependencies for all projects at once, run:

bash

pip install requests pyperclip pyttsx3 speech_recognition pyautogui wikipedia


Python Socket Chat Application
A real-time, multi-user chat application built with Python socket programming and threading. It features a modern, responsive GUI built with tkinter and ttkthemes, allowing multiple clients to connect to a central server and exchange messages instantly.

🌟 Features
Real-time Messaging: Instant text communication between multiple clients.
Multi-User Support: The server handles multiple concurrent connections using threading.
Modern GUI: A polished, theme-based user interface (inspired by Discord dark mode).
Emoji Support: Clients can send emojis that are rendered in the chat.
User Management: Users can set a custom username upon joining, and the server announces their arrival.
File Upload UI: Includes a file selection interface (simulated notification).
📂 Project Structure
The project consists of two main scripts:

server.py: The backend server that listens for connections and broadcasts messages to all connected clients.
client.py: The frontend GUI application that users interact with to send and receive messages.