import os
import cv2

def check_images(files, valid_extensions):
  """
  Hello this helps in the conversion of the file from one to another
  **`Args`
  -->`files`: The location of the file which has the subdirectories
  -->`valid_extension`: the type of extension you want to save
  """
  parent_path=os.listdir(files)
  for i in range (len(parent_path)):
    another_path=os.listdir(files+'/'+parent_path[i])
    for m in range (len(another_path)):
      extent=another_path[m]
      ext=extent.rfind('.')
      ext=extent[ext+1:].lower()
      if ext in valid_extensions:
        print (f"{extent} is good with {ext}")
        continue
      if ext not in valid_extensions:
        os.remove(another_path+'/'+another_path[m])
        print (f"removed {another_path[m]} having extension {ext}")
        continue
"""
any file converter to jpeg format function
"""
def converter (original_path, duplicate_path):
  images=os.listdir(original_path)
  for i in range (len(images)):
    path=original_path+'/'+images[i]
    png_img = cv2.imread(path)
    spliter=images[i].split('.')
    path_2=duplicate_path+'/'+f"{spliter[0]}.jpeg"
    cv2.imwrite(path_2, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    

    
    
"""
Converting any images to jpeg format ina any directory
"""

def converter_2 (original_path, extension):
  """
  This folder helps in renaming all the images to any extension format in your directory
  Args*
  original _path: path which has the images or the directories in it
  """
  orig_path=os.listdir(original_path)
  print (orig_path)
  if __name__ == "__main__":
    try:
      for m in range (len(orig_path)):
        images=os.listdir(original_path+'/'+orig_path[m])
        for i in range (len(images)):
          path=original_path+'/'+orig_path[m]+'/'+images[i]
          png_img = cv2.imread(path)
          spliter=images[i].split('.')
          path_2=original_path+'/'+orig_path[m]+'/'+f"{spliter[0]}.{extension}"
          os.remove(path=path)
          cv2.imwrite(path_2, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    except Exception as e:
      for dirpath, dirnames, filenames in os.walk(original_path):
        files=filenames
        for l in range (len(filenames)):
          path2=original_path+'/'+filenames[l]
          png_img = cv2.imread(path2)
          spliter=filenames[l].split('.')
          path_2=original_path+'/'+filenames[l]+'/'+f"{spliter[0]}.jpeg"
          os.remove(path=path2)
          cv2.imwrite(path_2, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
