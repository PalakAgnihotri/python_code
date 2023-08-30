
import cv2
import mediapipe as mp

# Function to handle the hand gestures
def handle_gesture(hand_landmarks):
    # Access individual landmarks
    # Example: x = hand_landmarks.landmark[0].x
    # Replace the index with the required landmark

    # TODO: Implement your logic to handle gestures
    # Here's a simple example to detect an open hand gesture
    # based on the y-coordinate of the landmarks:
    
    # Get the y-coordinate of the wrist landmark (landmark[0])
    wrist_y = hand_landmarks.landmark[0].y

    # Check if the hand is open based on the wrist position
    if wrist_y < hand_landmarks.landmark[5].y and wrist_y < hand_landmarks.landmark[9].y:
        print("Hand is open")
    else:
        print("Hand is not open")

# Initialize Mediapipe's solutions
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# Initialize the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    
    if not success:
        break
    
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image to detect hands
    results = hands.process(image_rgb)
    
    # Check if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Call the gesture handling function
            handle_gesture(hand_landmarks)
            
            # Draw landmarks on the image
            mp_hands.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Display the image
    cv2.imshow('Hand Gestures', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
