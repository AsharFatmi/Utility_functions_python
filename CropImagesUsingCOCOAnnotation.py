import os
import json
from PIL import Image


def main():

    annotation_path = '/home/kingashar/Downloads/annotation.json'
    img_path = '/home/kingashar/Downloads/images from video'
    save_dir = '/home/kingashar/Downloads/annotated_images'

    with open(annotation_path, 'r') as myfile:
        X=myfile.read()
    obj = json.loads(X)

    for annotation in obj['annotations']:
        #print(annotation)
        image_id = annotation['image_id']
        #print(image_id)

        for id in obj['images']:
            if (id['id'] == image_id):
                #print('True '+ str(image_id))
                img = id['file_name']
                imgName = img.split('/')
                #print(os.path.join(img_path,imgName[1]))
                imageObject  = Image.open(os.path.join(img_path,imgName[1]))
                
                x = annotation['bbox'][0]
                y = annotation['bbox'][1]
                width = annotation['bbox'][2]
                height = annotation['bbox'][3]
                
                cropped = imageObject.crop((x, y, x+width, y+height))
                cropped.save(os.path.join(save_dir, imgName[1]))


if __name__ == "__main__":
    main()
    