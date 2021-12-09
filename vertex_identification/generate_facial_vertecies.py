import cv2
import numpy as np
import dlib
import math
import random

#note, could use contours too connect verticies to their ajacents

side_features = []
def get_facial_features(gray):
    # Load the detector
    detector = dlib.get_frontal_face_detector()
    # Load the predictor
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # Convert image into grayscale
    # gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    # Use detector to find landmarks
    faces = detector(gray)
    landmarks = []
    for face in faces:
        landmarks.append(predictor(image=gray,box=face).parts())
    return faces,landmarks

def get_edge_features(gray, faces, draw = False):
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    high_thresh, thresh_im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    lowThresh = 0.5*high_thresh
    edge = cv2.Canny(blurred,lowThresh, high_thresh,apertureSize = 5, L2gradient=True)
    rows,cols = edge.shape
    edge_list = []
    for face in faces:
        for i in range(face.top(),face.bottom()):
            for j in range(face.left(),face.right()):
                if edge[i,j] > 0:
                    edge_list.append((i,j))
    if draw == True:
        cv2.imshow(winname='edge', mat=edge)
    return edge_list

def assign_edges_euclidian(landmarks, edge_list):
    assigned_edge_list = {}
    for i in edge_list:
        closest_landmark = 0
        d_closest = (i[1]-landmarks[0][0].x)**2+(i[0]-landmarks[0][0].y)**2
        for face in landmarks:
            for j in range(len(face)):
                # print(face[j].x)
                # print(face[j].y)
                d = (i[1]-face[j].x)**2+(i[0]-face[j].y)**2
                if d_closest > d:
                    closest_landmark = j
                    d_closest = d
            assigned_edge_list[i] = closest_landmark
    return assigned_edge_list

def draw_features(img,landmarks,assigned_edge_list,feature_color_list = None,draw_name = "Face"):
    for face in landmarks:
        # Create landmark object
        # Loop through all the points
        temp_iter = 0
        for n in face:
            x = n.x
            y = n.y
            # Draw a circle
            if feature_color_list != None:
                cv2.circle(img=img, center=(x, y), radius=5, color=feature_color_list[temp_iter], thickness=-1)
            else:
                cv2.circle(img=img, center=(x, y), radius=3, color=[0,255,0], thickness=-1)
            temp_iter += 1
    for key,val in assigned_edge_list.items():
        if feature_color_list != None:
            img[key[0],key[1]] = feature_color_list[val]
        else:
            img[key[0],key[1]] = [125,125,125]
    cv2.imshow(winname=draw_name, mat=img)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def draw_edges_of_facial_feature(img,face,landmark,assigned_edge_list,feature_color_list):
    landmark_pos = face[landmark]
    cv2.circle(img=img, center=(landmark_pos.x, landmark_pos.y), radius=5, color=feature_color_list[landmark], thickness=-1)
    for key, val in assigned_edge_list.items():
        if val == landmark:
            img[key[0],key[1]] = feature_color_list[landmark]
            # print(key)
    return img


def main():
    img = cv2.imread("Riely_front.png")
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    faces, landmarks = get_facial_features(gray)
    feature_color_list = [[random.randint(0,255) for i in range(3)] for j in range(len(landmarks[0]))]
    edge_list = get_edge_features(gray,faces,draw = True)
    assigned_edgelist = assign_edges_euclidian(landmarks,edge_list)
    # cv2.imshow(winname='face', mat=img)
    # cv2.waitKey(delay=0)
    # cv2.destroyAllWindows()
    # draw_features(img.copy(), landmarks,assigned_edgelist, draw_name="uncolored face")
    # draw_features(img.copy(), landmarks,assigned_edgelist,feature_color_list = feature_color_list, draw_name = "colored face")
    # for i in range(68):
    #     temp = draw_edges_of_facial_feature(img.copy(), landmarks[0],i,assigned_edgelist,feature_color_list)
    #     cv2.imshow(winname='face', mat=temp)
    #     cv2.waitKey(100)
    #     cv2.destroyAllWindows()
    
    return -1

if __name__ == "__main__":
    main()