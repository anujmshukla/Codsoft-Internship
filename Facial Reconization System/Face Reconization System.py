# Name            : Anuj Mukesh Shukla
# College         : Saffrony Institute of Technology
# File Name       : ChatBot.py
# File Task       : This is an file whose task is to take user input and respod it to according min max algorith 
# Support Files   : None
# Dependent Files : None 
# Email Id        : anujmshukla2002@gmail.com
# Task Title      : FACE DETECTION AND RECOGNITION
# Description     : Develop an AI application that can detect and recognize faces in images or videos. Use pre-trained face detection models like Haar cascades or deep learning-based face detectors, and optionally add face recognition capabilities using techniques like Siamese networks or ArcFace



# Importing libraries to run face detection and recognition
import cv2   # This package is used to take video or image from the camera and process it an gave it to face_recognition module 
import face_recognition  #this module will recognise the faces and compare it with the already present faces in our database
import numpy as np #this module is used to manipulates array 
import csv  # this module is used to handle the csv file we are going to make  
import os #this module is used to access the fine 
from datetime import datetime   # this module is used to get the exact date and time for noting it into csv file
 
# Getting videos from the camera  
videoCapturing = cv2.VideoCapture(0)
# Setting the size of camera wnindow
width = 400
height = 400
videoCapturing.set(cv2.CAP_PROP_FRAME_WIDTH, width)
videoCapturing.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

known_face_encoding=[]
known_face_name =[]

def ProcessingImage(image_name,image_path):
    temp_image=face_recognition.load_image_file(image_path)
    temp_encoding=face_recognition.face_encodings(temp_image)[0]
    known_face_encoding.append(temp_encoding)
    known_face_name.append(image_name)
    
ProcessingImage("Steve_Jobs","Faces_Data/Steve_Jobs.png")
ProcessingImage("Ratan_Tata","Faces_Data/Ratan_Tata.jpeg")
ProcessingImage("Mukesh_Ambani","Faces_Data/Mukesh_Ambani.jpg")
ProcessingImage("Elon_Musk","Faces_Data/Elon_Musk.jpeg")
ProcessingImage("Anuj Shukla","Faces_Data/Mukesh_Shukla.jpg")
# ProcessingImage("Shubhangi_Chaturvedi","Faces_Data/Shubhangi_Chaturvedi.jpg")
# ProcessingImage("Vinita_Shukla","Faces_Data/Vinita_Shukla.jpg")

print(known_face_name)
Known_Faces = known_face_name.copy()

# these variables are used to capture faces comming from camera 
face_location = [] #store face cordinates 
face_encoding = [] #stores face in numerial data 
face_name = [] #name of the face it is present in known_face_name
Condition=True

#used to get the date time and month 
now = datetime.now()
#we are going to fetch only date 
current_date = now.strftime("%d-%m-%y")

# lets create a csv file with gaving writing permission
# the fromate for opean is (file name,mode of opeaning)
file = open('Maked Person.csv','a+',newline='')
#below variable is used to write data in file it is an instant of write class in csv module 
file_write = csv.writer(file)
file_write.writerow(["Name", "Current_Time", "Current_date"])
# our main loop which run for infinfite time 
face_locations = []

while True:
    _, frame = videoCapturing.read()
    new_width = int(frame.shape[1] * 0.25)
    new_height = int(frame.shape[0] * 0.25)
    smallFrame = cv2.resize(frame, (new_width, new_height))
    
    # Convert the image to RGB format
    rgbSmallFrame = cv2.cvtColor(smallFrame, cv2.COLOR_BGR2RGB)
    
    if Condition:
        face_locations = face_recognition.face_locations(rgbSmallFrame)
        
        face_encodings = face_recognition.face_encodings(rgbSmallFrame, face_locations)
        
        face_name = []
        
        for faceEncoding in face_encodings:
            # This willl simplly compare the face detect in the camera to the face we have in our database
            # It will compare the numerical data of the faces we have given to it
            # The  face_recognition.compare_faces returns a list of boolean values indicating whether detected face from camera matches any of the known faces in the database.
            # For those whose face matches in the database gives true otherwise false
            matches = face_recognition.compare_faces(known_face_encoding,faceEncoding)
            # print(matches)
            name = ""
            # The face_recognition.face_distance() function calculates the Euclidean distance between the detected face encoding (faceEncoding) and each of the known face encodings in the database (known_face_encoding). This distance represents the similarity between the detected face and each known face.
            faceDistance=face_recognition.face_distance(known_face_encoding,faceEncoding)
            # hear we used np.argmin function which will return the minium value from the list The smaller the Euclidean distance the higher the face match
            bestMatchIndex = np.argmin(faceDistance)
            # print(bestMatchIndex)
            #this will cheeck that index given by the above line is true or not in the list given by .compare_faces function 
            if 0 <= bestMatchIndex < len(matches) and matches[bestMatchIndex]:
                name = known_face_name[bestMatchIndex]
                
                
            face_name.append(name)
            #hear it will cheeck that name is present in the known_face_name 
            if len(matches) == 0:
                name = "Unknown"
            elif matches[bestMatchIndex]:
                name = known_face_name[bestMatchIndex]
                face_name.append(name)
                # Here we check if the name is present in Known_Faces (which is a copy of known_face_name) then perform further operations; otherwise, skip writing data to CSV
                if name in Known_Faces:
                    # Now once "name" is found, we simply remove it from the Known_Faces so that if that face appears again, it won't be marked again
                    Known_Faces.remove(name)
                    print(Known_Faces)
                    current_time = now.strftime("%I:%M %p")
                    # Write data to CSV file
                    file_write.writerow([name, current_time, current_date])
                    # Flush the buffer to make sure the data is written to the file immediately
                    file.flush()
    
    #to show the output to user in that what text need to show and video(frame) we want to show  
    cv2.imshow("AttendenceSystem",frame)
    # as soon as we press q button the while loop will be broken 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
             
videoCapturing.release()
cv2.destroyAllWindows()
file.close()       