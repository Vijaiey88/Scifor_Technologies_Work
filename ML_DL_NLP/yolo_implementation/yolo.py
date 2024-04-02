import numpy as np
import argparse
import cv2

## construct argument parse to pass image as argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections, IoU threshold")
ap.add_argument("-t", "--threshold", type=float, default=0.3, help="Threshold when applying non-maxima suppression")
args = vars(ap.parse_args())

## load labels
labels_path = "yolo\\coco.names"
labels = open(labels_path).read().strip().split("\n")

## color representation for labels
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

## paths to yolo weights and model configuration
weights_path = "yolo\\yolov3.weights"
model_config = "yolo\\yolov3.cfg"

## load model
net = cv2.dnn.readNetFromDarknet(model_config, weights_path)

## load input image
image = cv2.imread(args["image"])
(H, W) = image.shape[:2]

## get only output name from yolo
ln = net.getLayerNames()
ln = [ln[i-1] for i in net.getUnconnectedOutLayers()]

blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)
layer_outputs = net.forward(ln)

boxes = []
confidences = []
classIds = []

for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        classId = np.argmax(scores)
        confidence = scores[classId]
        
        if confidence > args["confidence"]:
            box = detection[0:4] * np.array([W, H, W, H])
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width/2))
            y = int(centerY - (height/2))  
            boxes.append((x, y, int(width), int(height)))  
            confidences.append(float(confidence))
            classIds.append(classId)

idx = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"], args["threshold"])

if len(idx) > 0:
    for i in idx.flatten():
        (x, y)  = (boxes[i][0], boxes[i][1])
        (w, h)  = (boxes[i][2], boxes[i][3])            
        color = [int(c) for c in colors[classIds[i]]]
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
        text = "{}: {:4f}".format(labels[classIds[i]], confidences[i])
        cv2.putText(image, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv2.imshow("image", image)
cv2.waitKey(0)
