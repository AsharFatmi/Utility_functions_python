import cv2
import os
import json


def select_images():

    img_path = '/home/kingashar/Downloads/images_from_video'
    save_dir = '/home/kingashar/Downloads/annotated_images'
    annotation = '/home/kingashar/Downloads/annotation.json'


    with open(annotation, 'r') as myfile:
        X=myfile.read()
    obj = json.loads(X)


    for img_obj in obj['images']:

        img_name = img_obj['file_name']
        print(img_obj['id'])
        
        img = img_name.split('/')
        #print(img[1])

        image = cv2.imread(os.path.join(img_path,img[1]))

        #cv2.imshow('image', image)

        # if cv2.waitKey(1) == 0x1b: # ESC
        #     print('ESC pressed. Exiting ...')
        #     break
        #print(os.path.join(save_dir,img[1]))

        cv2.imwrite(os.path.join(save_dir,img[1]), image)


if __name__ == "__main__":

    select_images()