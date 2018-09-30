def HC():
    import numpy as np
    import cv2
    data={'cat':'Door'}
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    frontalcatface_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    #https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    #upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    #'http://192.168.43.1:8080/video'
    cap = cv2.VideoCapture('http://192.168.43.1:8080/video')

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        frontalcatface = frontalcatface_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in frontalcatface:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,data['cat'],(x,y), font, (h/80), (0,255,155), 2, cv2.LINE_AA)
            

        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
