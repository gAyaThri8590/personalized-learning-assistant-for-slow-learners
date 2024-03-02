import streamlit as st
import pandas as pd
st.title("Simple Login App")
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
     return hashed_text
    return False
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def main():
    """Simple Login App"""
st.title("Simple Login App")

menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Home")

elif choice == "Login":
    st.subheader("Login Section")

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password",type='password')
if st.sidebar.checkbox("Login"):
    # if password == '12345':
    create_usertable()
    hashed_pswd = make_hashes(password)

    result = login_user(username,check_hashes(password,hashed_pswd))
    if result:

        st.success("Logged In as {}".format(username))

        task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
        if task == "Add Post":
            st.subheader("Add Your Post")

        elif task == "Analytics":
            st.subheader("Analytics")
        elif task == "Profiles":
            st.subheader("User Profiles")
            user_result = view_all_users()
            clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
            st.dataframe(clean_db)
    else:
        st.warning("Incorrect Username/Password")

elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username",key='1')
    new_password = st.text_input("Password",type='password',key='2')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")
import cv2
from random import randrange

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
webcam = cv2.VideoCapture(0)
import cv2
from random import randrange

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()
    gray_style_picture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    face_coordinates = face_cascade.detectMultiScale(gray_style_picture)
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(0, 255), randrange(0, 255), randrange(0, 255)), 7)
    
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()

