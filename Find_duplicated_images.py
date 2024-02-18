#This script helps you find identical photos

import os
import shutil
from PIL import Image
import imagehash
from tqdm import tqdm #Progressbar
#Don't forget to install PIL and imagehash, if you didn't

pic_name = "Pictures"
dup_name = "Duplicates"

pic_path = os.path.join(os.getcwd(), pic_name)

# Create a work-directory and a directory for duplicates
if not (os.path.exists(pic_path) and os.path.isdir(pic_path)):
    os.mkdir(pic_name)
os.chdir(pic_name)

print("\n***This script helps you find identical photos***")
print("\nWork directory: " + os.getcwd())
pic_path = os.getcwd()

dup_path = os.path.join(os.getcwd(), dup_name)
if not (os.path.exists(dup_path) and os.path.isdir(dup_path)):
    os.mkdir(dup_name)
# print("Sub directories: ", os.listdir(os.getcwd()))

print("\nPlace the pictures into the directory", os.getcwd())
input("and press Enter")

#Loop to search for all the images
files = os.listdir(os.getcwd())
pics = []

def calculate_hash(img_path):
    with Image.open(img_path) as img:
        hash_value = imagehash.average_hash(img)
        return str(hash_value)

#Placing only images into the list "pics", to have the right length
print("Making a list of images...")
for file in tqdm(files):
    try:
        with Image.open(file) as img:
            pics.append(file)

    except (IOError, OSError):
        pass

print("Searching the duplicates...")
for i in tqdm(range(len(pics)-1)):  #taking all the indexes of the photos
    try:
        hash1 = calculate_hash(pics[i])
        thereisdouble = False
        #the path for copies, if we find them:
        copie_path = os.path.join(dup_path, f"{pics[i]}".replace(".","_"))
        #compare the hashsum with the hashsum of all the other files:
        for j in range(i+1, len(pics)):
            if hash1 == calculate_hash(pics[j]):
                thereisdouble = True
                #make a directory for the copy, move the copy there:
                if not (os.path.exists(copie_path)):
                    os.mkdir(copie_path)
                shutil.move(pics[j], copie_path)
        #if there was a duplicate, make a copy in the copy-directory to compare, if we need it
        if thereisdouble == True:
            shutil.copy(pics[i], copie_path)
    except (IOError, OSError):
        pass
    except Exception as e:
        print(f"Error {e}")

print("\nReady!")








