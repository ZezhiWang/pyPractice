# HW6 - Problem 2
# Encryption/Decryption 

from Tkinter import *

def preprocess(s):
    return [item.lower() for item in s if item not in ",./?';:! "]
     
def shift(ch,k):
    return chr(ord('a')+(ord(ch)-ord('a')+k)%26)

def char_encrypt(plaintextchar,keychar):
    return shift(plaintextchar,ord(keychar)-ord('a'))

def char_decrypt(ciphertextchar,keychar):
    return shift(ciphertextchar,ord('a')-ord(keychar))

def vig_encrypt(plaintext,key):
    keys = ""
    while len(keys) < len(plaintext):
        keys += key
    keys = keys[:len(plaintext)]
    return ''.join([char_encrypt(preprocess(plaintext)[i], keys[i]) for i in range(len(keys))])

def vig_decrypt(ciphertext,key):
    keys = ""
    while len(keys) < len(ciphertext):
        keys += key
    keys = keys[:len(ciphertext)]
    return ''.join([char_decrypt(ciphertext[i], keys[i]) for i in range(len(keys))])

############################################################################
# This code detects which button the user clicked on.
# If the user clicked on the Encrypt button, it will calle the function
# 'vig_encrpt' to encrypt the text. Otherwise, if the user clicked on the Decrypt
# button, it will call the function 'vig_decrypt' to decrypt   
def button_handler(event):
    window.update()
    w=event.widget
    if w==encrypt_button:
        plaintext=the_text.get(0.0,END)
        plaintext=plaintext[:len(plaintext)-1] #strip newline character
        key = the_key.get()
        ciphertext=vig_encrypt(plaintext,key)
        the_text.delete(0.0,END)
        the_text.insert(0.0,ciphertext)
        the_text.configure(bg="indian red")
    elif w==decrypt_button:
        ciphertext=the_text.get(0.0,END)
        ciphertext=ciphertext[:len(ciphertext)-1]#strip newline character
        key = the_key.get()
        plaintext=vig_decrypt(ciphertext,key)
        the_text.delete(0.0,END)
        the_text.insert(0.0,plaintext)
        the_text.configure(bg="light green")
 
# This code creates the GUI
window = Tk()
# creat the textbox for the user to enter the text (to encrypt/decrpt)
textlabel=Label(window,text='Plaintext/Ciphertext', font = ("comic sans ms", 16, "bold"))
textlabel.grid(row=0,column=0,columnspan=3)
the_text=Text(window,width=40,height=20,bg = "light green", font = ("comic sans ms", 14, "bold"))
the_text.grid(row=1,column=0,columnspan=3)
# create the textbox for user to enter the key
keylabel=Label(window,text='Key', font = ("comic sans ms", 14, "bold"))
keylabel.grid(row=2,column=0)
the_key=Entry(window, bg="goldenrod", text="<Enter Key>")
the_key.grid(row=3,column=0)
# create button to allow user to encrypt text
encrypt_button=Button(window,text='Encrypt')
encrypt_button.grid(row=4,column=0)
encrypt_button.bind('<Button-1>',button_handler)
# create button to allow user to decrypt text
decrypt_button=Button(window,text='Decrypt')
decrypt_button.grid(row=4,column=1)
decrypt_button.bind('<Button-1>',button_handler)
window.mainloop()