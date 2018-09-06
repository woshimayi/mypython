import face_recognition

know_image = face_recognition.load_image_file('123.jpg')
unknow_image = face_recognition.load_image_file('unknow_image.jpg')

biden_encoding = face_recognition.face_encodings(know_image)[0]
unknow_image = face_recognition.face_encodings(unknow_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknow_encoding)
