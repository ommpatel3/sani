import cv2
import numpy as np
import paho.mqtt.client as mqtt
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

cap=cv2.VideoCapture(0)

while (True):
    ret,frame = cap.read()
    flipped =cv2.flip(frame,1)

    cv2.rectangle(flipped,(520,245),(120,200),(0,0,255),1)#number
    cv2.rectangle(flipped,(520,300),(320,330),(0,0,255),1)#birthdate
    cv2.rectangle(flipped,(520,200),(120,165),(0,0,255),1)#name

    cv2.imshow('frame',flipped)    
    if cv2.waitKey(1)%256 == 32: #when spece is pressed, stop showing video
        break
while True:
    #show frame until q is pressed
    cv2.imshow('frame',frame) 

    #isolating card
    num=frame[200:245,120:520]

    date=frame[300:330,120:320]

    name=frame[165:200,120:520]

    img=cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
    img2=cv2.cvtColor(date, cv2.COLOR_BGR2GRAY)
    img3=cv2.cvtColor(name, cv2.COLOR_BGR2GRAY)

    #dilating and eroding
    kernel=np.ones((1,1),np.uint8)

    img=cv2.dilate(img,kernel,iterations=10)
    img=cv2.erode(img,kernel,iterations=7)

    img2=cv2.dilate(img2,kernel,iterations=75)
    img2=cv2.erode(img2,kernel,iterations=75) 

    img3=cv2.dilate(img3,kernel,iterations=1)
    img3=cv2.erode(img3,kernel,iterations=1)

    #thresholding
    img=cv2.medianBlur(img,3)
    img=cv2.GaussianBlur(img,(5,5),0)
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)

    img2=cv2.medianBlur(img2,3)
    img2=cv2.GaussianBlur(img2,(5,5),0)
    img2=cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)

    img3=cv2.GaussianBlur(img3,(7,7),0)
    img3=cv2.adaptiveThreshold(img3,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,2)

    cv2.imwrite("thres1.png", img)
    result1=pytesseract.image_to_string(Image.open("thres1.png"))

    cv2.imwrite("thres2.png", img2)
    result2=pytesseract.image_to_string(Image.open("thres2.png"))

    cv2.imwrite("thres3.png", img3)
    result3=pytesseract.image_to_string(Image.open("thres3.png"))

    print(result1+"	X "+result2+" X "+result3)

    ##################JSON NOT NEEDED
    #data = {}
    #data['people']=[]
    #data['people'].append({
    #    'name':result3,
    #    'number':result1,
    #    'birth':result2
    #})

    #with open('data.txt','w') as outfile:
    #    json.dump(data,outfile)
    
    #cv2.imshow('num', img)
    #cv2.imshow('date',img2)
    #cv2.imshow('name',img3)

    
    def on_connect(client, userdata, flags, rc):
        print('connected')
        client.publish('kismet',result3+"+"+result1+"+"+result2)
    
    def on_publish(client, userdata, mid):
        print("published")
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect("broker",8883) #insert broker link
    client.loop_forever()

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows