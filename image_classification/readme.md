- image loading with vaex
- image centering and cropping
- image augmentation 0: base hue of skin --> "whiteness"
- image augmentation 1: affine transformation
- image augmentation 2: HOG
- image augmentation 3: canny edges
- image augmentation 4: Shades of Gray color constancy method
- image augmentation 5: Gaussian filter
- image augmentation 6: Haar wavelets
- image augmentation 7: histogram equalisation
- image augmentation 8: adaptive equalisation
- image augmentation 9: SIFT
- image augmentation 10: radiomics feature mapping
- image augmentation 11: local binary pattern
- image augmentation 12: Random brightness
- image augmentation 13: HSV
- image augmentation 14: CLAHE
- image augmentation 15: background subtraction (see below) 
- image augmentation 16: CutMix, MixUp, AugMix

- image desampling 1: random cutout
- image desampling 2: noise

- feature extraction 1: image diff
- feature extraction 2: integrated image gradient
- feature extraction 3: fractal dimensionality
- feature extraction 4: spatio-color entropy
- meta features: age, localisation, gender, etc.

- image segmentation: segmentation\_models 
- image classifier training Exception, SENet154, ResNet, ResNEXT, InceptionV4
- image arch: segmentation, transformers, multi-modality

- spec: GELU, LeakyRelu
- optimizer: Adam, SGD, RMSProp, SWA, AdaTune

# Example code

* https://github.com/ngessert/isic2019

Background subtraction:
```
fgbg = cv.createBackgroundSubtractorMOG2()
    
def view_images_aug(images, title = '', aug = None):
    width = 6
    height = 5
    fig, axs = plt.subplots(height, width, figsize=(15,15))
    for im in range(0, height * width):  
        data = pydicom.read_file(os.path.join(train_images_dir, list(images)[im]+ '.dcm'))
        image = data.pixel_array
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (256, 256))
        image= fgbg.apply(image)
        i = im // width
        j = im % width
        axs[i,j].imshow(image, cmap=plt.cm.bone) 
        axs[i,j].axis('off')
        
    plt.suptitle(title)
view_images_aug(train[train['diagnosis']=='lentigo NOS']['image_name'], title="Lentigo NOS's growth");
```

Grayscale
```
import cv2
def view_images_aug(images, title = '', aug = None):
    width = 6
    height = 5
    fig, axs = plt.subplots(height, width, figsize=(15,15))
    for im in range(0, height * width):  
        data = pydicom.read_file(os.path.join(train_images_dir, list(images)[im]+ '.dcm'))
        image = data.pixel_array
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (256, 256))
        i = im // width
        j = im % width
        axs[i,j].imshow(image, cmap=plt.cm.bone) 
        axs[i,j].axis('off')
        
    plt.suptitle(title)
view_images_aug(train[train['diagnosis']=='lentigo NOS']['image_name'], title="Lentigo NOS's growth");
```

Circling and Gaussian blur
```
def view_images_aug(images, title = '', aug = None):
    width = 6
    height = 5
    fig, axs = plt.subplots(height, width, figsize=(15,15))
    for im in range(0, height * width):  
        data = pydicom.read_file(os.path.join(train_images_dir, list(images)[im]+ '.dcm'))
        image = data.pixel_array
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (256, 256))
        image=cv2.addWeighted ( image,4, cv2.GaussianBlur( image , (0,0) , 10) ,-4 ,128)
        i = im // width
        j = im % width
        axs[i,j].imshow(image, cmap=plt.cm.bone) 
        axs[i,j].axis('off')
        
    plt.suptitle(title)
view_images_aug(train[train['diagnosis']=='lentigo NOS']['image_name'], title="Lentigo NOS's growth");
```
