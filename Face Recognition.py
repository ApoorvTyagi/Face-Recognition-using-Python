import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder


image=face_recognition.load_image_file("img1.jpg")
unknown_face=face_recognition.load_image_file("harry.jpg")


#count the number of faces in the image->img1.jpg
face_locations = face_recognition.face_locations(image)
print("I found {} face(s) in this photograph.".format(len(face_locations)))

try:
    #find the face encodings of the image->MSD.jpg
    unknown_face_encoding = face_recognition.face_encodings(unknown_face)[0] #since we know the image has only one face, we only care about the first encoding in image, so we grab index 0.

    #find the face encodings of the image->img1.jpg
    face_encodings=[]
    for i in range(0,len(face_locations)):
        face_encodings.append(face_recognition.face_encodings(image)[i])
        
except IndexError:
    print("Can't locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

#Array to store our final results, true->match found and false->match not found
known_faces=[]
for i in range(0,len(face_encodings)):
    known_faces.append(face_encodings[i])
results=face_recognition.compare_faces(known_faces, unknown_face_encoding)


print(results)
