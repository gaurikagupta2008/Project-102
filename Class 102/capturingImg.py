import cv2 
import dropbox
def takeSnapShot():
    videoCaptureObj=cv2.VideoCapture(0)
    flag=True
    while(flag):
        #ret=checks if flag is read
        #frame=reads the image
        ret,frame=videoCaptureObj.read()
        img_name="firstImg.jpg"
        cv2.imwrite(img_name,frame)
        flag=False
    return img_name
    print("SnapShot taken!")
    videoCaptureObj.release()   
    cv2.destroyAllWindows()  

def uploadFile(image_name):
    file_to='/testFolder/'+(image_name)
    access_token='sl.BA66UpXT6Wj1ceDPAU6EmSJCJ9JJppC21FQDG72Kw5-AcL0jK2d45n8LfyMtRI-SWFEiw_iEkIuu3BiQNfQg0aP9sIXOlcjmeSPx_CDoLDHeXAQ79ftYEq3Kx_qCoEd9nVQYIyw'
    dbx=dropbox.Dropbox(access_token)
    storedImg=image_name
    file_from=open(storedImg,'rb')
    newFile=file_from.read()
    dbx.files_upload(newFile,file_to)
    print("Files uploaded")

def main():
    image=takeSnapShot()
    uploadFile(image)

main()

