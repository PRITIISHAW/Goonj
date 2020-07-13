import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import *
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
# capture audio from the microphone
def func():
        r = sr.Recognizer()
        isl_gif=['any questions', 'are you angry', 'are you hungry', 'be careful',
                'did you finish homework', 'do you have money',
                'do you want something to drink', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good morning', 'good question',
                'i am a clerk', 
                'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i like pink colour', 'lets go for lunch',
                'nice to meet you', 'open the door', 'please call me later',
                'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam',
                'what is the problem', 'what is today\'s date', 'what does your father do',
                'what is your name', 'whats up',
                'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'ahemdabad', 'all', 'assam', 'august', 'banana', 'banaras', 'banglore',
'bridge', 'cat', 'christmas', 'church', 'clinic', 'dasara',
'december', 'grapes', 'hello',
'hindu', 'hyderabad', 'job', 'july', 'june', 'karnataka', 'kerala', 'krishna', 'mango',
'may', 'mile', 'mumbai', 'nagpur', 'pakistan', 'police station',
'post office', 'pune', 'punjab', 'saturday', 'shop',
'temple', 'thursday', 'toilet', 'tomato', 'tuesday', 'usa', 'village',
'wednesday']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print('Say something')
                        audio = r.listen(source)

                                                        # to recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                print("You Said: " + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye'):
                                        print("Bye! Have a good day.")
                                        break
                                
                                elif(a.lower() in isl_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label for displaying images or playing them if they are gifs"""
                                            def load(self, im):
                                                if isinstance(im, str):
                                                    im = Image.open(im)
                                                self.loc = 0
                                                self.frames = []

                                                try:
                                                    for i in count(1):
                                                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                        im.seek(i)
                                                except EOFError:
                                                    pass

                                                try:
                                                    self.delay = im.info['duration']
                                                except:
                                                    self.delay = 100

                                                if len(self.frames) == 1:
                                                    self.config(image=self.frames[0])
                                                else:
                                                    self.next_frame()

                                            def unload(self):
                                                self.config(image=None)
                                                self.frames = None

                                            def next_frame(self):
                                                if self.frames:
                                                    self.loc += 1
                                                    self.loc %= len(self.frames)
                                                    self.config(image=self.frames[self.loc])
                                                    self.after(self.delay, self.next_frame)

                                    root = tk.Tk()
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'C:/Users/Priti/Desktop/Goonj/Gifs/{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:

                                    for i in range(len(a)):
                                                    #a[i]=a[i].lower()
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'Alphabets/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(1) # number of seconds to pause each image
                                                            
                                                    else:
                                                            continue

                        except:
                               print("Can you please repeat.")
                        plt.close()


while 1:
  image   = "img.jpg"
  msg="GOONJ"
  choices = ["Live Voice","All Done!"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
 