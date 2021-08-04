from stegano import exifHeader
import os.path
import time

def encrypting(input_img,  output_img, crypto):
    secret = exifHeader.hide(input_img, output_img, crypto)
    print('Image encrypted')

def decoding(input_img):
    result = exifHeader.reveal(input_img)
    result = result.decode()
    print('Decoding. Please wait')
    time.sleep(2)
    print('Result:', result)

print('Hi! Pls enter the exact path to the encryption and decryption file. The file format must be .jpg or .jpeg!')

while True:
    choice = int(input('\nencrypting - 1, decoding - 2 (please enter 1/2):'))
    if type(choice) != int:
        print('Select the function, 1 or 2')
    else:
        suffix_end = ('.jpg', '.jpeg')
        if choice == 1:
            input_img = input('Enter the path to the file:')
            if os.path.isfile(input_img):
                if not input_img.endswith(suffix_end):
                    print('You need to enter a file with the extension jpg or jpeg!')
                else:
                    output_img = input('Enter where to save the encrypted image:')
                    if not input_img.endswith(suffix_end):
                        print('You need to enter a file with the extension jpg or jpeg!')
                    else:
                        crypto = input('Enter your message:')
                        encrypting(input_img, output_img, crypto)
                        print()
            else:
                print("File is doesn't exist!Try again.")

        if choice == 2:
            input_img = input('Enter the path to the file:')
            if os.path.isfile(input_img):
                if not input_img.endswith(suffix_end):
                    print('You need to enter a file with the extension jpg or jpeg!')
                else:
                    decoding(input_img)
                    print()
            else:
                print("File is doesn't exist!Try again.")
