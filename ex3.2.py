import cv2

def ImageHash(fileName):
    image = cv2.imread(fileName) 
    resized = cv2.resize(image, (8,8), interpolation = cv2.INTER_AREA) 
    gray_image = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY) 
    avg=gray_image.mean() 
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0) 
    

    _hash=""
    for x in range(8):
        for y in range(8):
            value=threshold_image[x,y]
            if value==255:
                _hash=_hash+"1"
            else:
                _hash=_hash+"0"
            
    return _hash
 
def CompareHash(hash1,hash2):
    l=len(hash1)
    i=0
    count=0
    while i<l:
        if hash1[i]!=hash2[i]:
            count=count+1
        i=i+1
    return count


hash1=ImageHash("HSV.jpg")
hash2=ImageHash("res3.1.jpg")
print(hash1)
print(hash2)
print(CompareHash(hash1, hash2))