import cv2
cap = cv2.VideoCapture(0)
width = 1290
height = 960
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    ret, frame = cap.read()    
    if not ret:
        print("Failed to grab frame")
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", frame)
    cv2.imshow("Grayscale Image", img)
    cv2.imwrite('captured_image.jpg', frame)
    input_str = cv2.waitKey(20)
    if input_str == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
