from selenium import webdriver
from tkinter import *
import tkinter as tk
from selenium.webdriver.chrome.options import Options
import urllib.request
from tkinter import filedialog

def login():
    if(a.get()):
        q=a.get()
        #print(q)
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(r'C:\Users\Shivani Agarwal\Downloads\chromedriver_win32\chromedriver.exe',options=options)
        driver.get("https://instagram.com/"+q)

        images= driver.find_elements_by_tag_name('img')
        file_path = 'C:/Users/Shivani Agarwal/PycharmProjects/ml/images/'
        i=0
        for img in images:
            source = img.get_attribute("src")
            #print(source)
            filename = 'image-{}.jpg'.format(i)
            full_path = '{}{}'.format(file_path, filename)
            i = i + 1
            urllib.request.urlretrieve(source,full_path)
        driver.close()
        #print('Save')
        file()
    else:
        q=b.get()
        file_path = 'C:/Users/Shivani Agarwal/PycharmProjects/ml/images/'
        i = 1
        filename = 'image-{}.jpg'.format(i)
        full_path = '{}{}'.format(file_path, filename)
        i = i + 1
        urllib.request.urlretrieve(q, full_path)
        file()

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="C:/Users/Shivani Agarwal/PycharmProjects/ml/images/",
                                          title="Select a File",
                                          filetypes=(("JPEG image",
                                                      "*.jpg*"),
                                                     ("all files",
                                                      "*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)

def file():
    global label_file_explorer
    root2 = tk.Tk()
    root2.title("INSTAGRAM IMAGE DOWNLOADER")
    root2.geometry("600x300")
    root2.configure(bg='black')
    q2 = tk.Label(root2, text="Hurray..", fg='white',bg='black', font=('Gigi', 30, 'bold'))
    q2.place(x=250, y=0)
    q2=tk.Label(root2,text="Your downloading completed.",bg='black',fg='white',font=('Andalus', 30, 'bold'))
    q2.place(x=50,y=50)
    button2 = Button(root2, text="Click on", bg='#adadaa', font=('Rockwell', 12, 'bold', 'italic'), command=lambda: browseFiles())
    button2.place(x=270, y=130)
    label_file_explorer = tk.Label(root2, text="", bg='black', fg='white', font=('Andalus', 12, 'bold'))
    label_file_explorer.place(x=0, y=180)
    root2.mainloop()



root=tk.Tk()
root.title("INSTAGRAM IMAGE DOWNLOADER")
root.geometry("900x600")
root.configure(bg='black')
global a,b
w=tk.Label(root, text="INSTAGRAM IMAGE DOWNLOADER!!!", padx=30, bg='black',fg = 'grey', font=('cooper black', 30))
w.place(x=40,y=4)
w1=tk.Label(root, text="Enter instagram_id:", padx=30, fg='#8c8b88',bg = 'black', font=('Andalus', 20))
w1.place(x=100,y=250)
w2=tk.Label(root, text="Download image and enjoy....", padx=30, fg='white',bg = 'black', font=('Curlz mt', 50))
w2.place(x=70,y=80)
a=Entry(root, width=20,bg='#ede5cc', font=('Arial', 20, 'bold'))
a.place(x=370,y=250,height=40)
w3=tk.Label(root, text="OR", padx=30, fg='white',bg = 'black', font=('Curlz mt', 30))
w3.place(x=370,y=300)
w4=tk.Label(root, text="Enter Image URL:", padx=30, fg='#8c8b88',bg = 'black', font=('Andalus', 20))
w4.place(x=130,y=380)
b=Entry(root, width=20,bg='#ede5cc', font=('Arial', 20, 'bold'))
b.place(x=370,y=380,height=40)
button1 = Button(root,text="Submit",bg='#adadaa',font=('Arial', 12, 'bold', 'italic'), command=lambda: login())
button1.place(x=400,y=480)
root.mainloop()
