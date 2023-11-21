from roboflow import Roboflow
import cv2
import os

# Initialize Roboflow with your API key
rf = Roboflow(api_key="4V69D2ZdRCtg7FrxNNyh")
project = rf.workspace('soroush-mirzaee-omf8x').project("smart-glasses-nv4nt")
model = project.version(1).model

# Folder to save images
save_folder = 'captured_images'
os.makedirs(save_folder, exist_ok=True)

def is_good_picture(prediction):
    labels = ['nature', 'building', 'people', 'sky']
    count = sum(label in prediction for label in labels)
    return count > 2

def display_classification(frame, prediction):
    for item in prediction['predictions']:
        label = item['class']
        confidence = item['confidence']
        cv2.putText(frame, f'{label}: {confidence:.2f}',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

camera = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        temp_image_path = os.path.join(save_folder, 'temp_image.jpg')
        cv2.imwrite(temp_image_path, frame)

        prediction = model.predict(temp_image_path, confidence=50, overlap=50).json()
        print(prediction)

        # Display classification on the frame
        display_classification(frame, prediction)

        # Show the frame
        cv2.imshow('Camera Feed', frame)

        if is_good_picture(prediction):
            save_path = os.path.join(save_folder, 'good_picture.jpg')
            cv2.imwrite(save_path, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    camera.release()
   # cv2.destroyAllWindows()
