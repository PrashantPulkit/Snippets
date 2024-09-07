from tkinter import *
from PIL import ImageTk, Image
import requests

import datetime
from io import BytesIO
import keys
import webbrowser

window = Tk()
window.title("snippets")

apikey = keys.apikey

def pageConstructor(news,frame):
    #print(news)
    for frames in frame.winfo_children():
        frames.destroy()
    i = int(0)
    for article in news["articles"]:
        if i in [0,4,8,12,16,20]:
            vframe = Frame(frame,height=float((window.winfo_screenheight()-40)/2),width=float((window.winfo_screenwidth())),bg="#FF6969")
        
        t=str(article['title'])
        d=str(article['description'])
        img =str(article['urlToImage'])
        url = str(article['url'])
        c=str(article['content'])

        f = Frame(vframe,height=float((screen_height-40)/2),width=30,border=2,borderwidth=2,bg="#FFF5E1",bd=2)
 
        title = Label(f,text=f"{t[:35]}-\n-{t[35:70]}-\n-{t[70:105]}" ,font="lucida 15",anchor=W,width=30,justify="left",fg="#0C1844",bg="#FFF5E1")
        title.pack(fill=X)
        description = Label(f,text=f"{d[:60].replace('\n', '')}-\n-{d[60:120].replace('\n', '')}-\n-{d[120:180].replace('\n', '')}",anchor=W,width=30,justify="left",fg="#C80036",bg="#FFF5E1")
        description.pack(fill=X)
         
        b = Button(f,text="Open url",font="lucida ",bg="#0C1844",fg="#FFF5E1",relief="flat")
        b.pack(side="left", anchor="center", ipadx=5, padx=5, pady=5, fill="x")
        b.bind("<Button-1>", lambda x : redirecting(url) )

        f.pack(side=LEFT,fill=X,ipadx=10,ipady=10,padx=5,pady=5)

        if i in [3,7,11,15,19]:
            vframe.pack(fill=X)
        i+=1
        
        #print("frame created")
    
def redirecting( url):
    
    webbrowser.open(url)

def searching(event):
    label2.destroy()
    a=scvalue.get() 
    x = datetime.datetime.now()

    if int(x.strftime("%d")) in range(1,8):
        m = int(x.strftime("%m")) - 1
        d = 28
    else:
        m = int(x.strftime("%m"))
        d = int(x.strftime("%d"))-7
    apikey = keys.apikey
    url = ('https://newsapi.org/v2/everything?'
        f'q="{a}"&'
        f'from=2024-{m : 03d}-{d : 03}&'
        'sortBy=popularity&'
        f'apiKey={apikey}')
    print(keys.apikey)
    response = requests.get(url)
    news = response.json()
    #print(news)
    pageConstructor(news,frame1)


def popular():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&apiKey={apikey}')
    response = requests.get(url)
    news = response.json()
    pageConstructor(news,frame1)

def tech():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={apikey}')
    response = requests.get(url)
    news = response.json()
    pageConstructor(news,frame1)    

def entertainment():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={apikey}')
    response = requests.get(url)
    news = response.json()
    pageConstructor(news,frame1)

def sports():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={apikey}')
    response = requests.get(url)
    news = response.json()
    pageConstructor(news,frame1)

def business():
    url = (f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={apikey}')
    response = requests.get(url)
    news = response.json()
    pageConstructor(news,frame1)


def click(event):
    # Calls the requred func
    label2.destroy()
    text = event.widget.cget("text")

    if text == "Popular/Trending":
        popular()
        
    elif text == "Sports":
        sports()
    elif text == "Technology": 
        tech()   
    elif text == "Business":
        business()
    elif text == "Entertainment":
        entertainment()
    #print("request succesful from button")    
    


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

topFrame = Frame(window,bg="#0C1844",height=20 )


scvalue=StringVar()
scvalue.set("")
logolabel = Label(topFrame,text="snippets",font="Gothic 20 bold",fg = "#FF6969",bg="#0C1844")
logolabel.pack(side=LEFT,padx=(30,0))
ent = Entry(topFrame,textvariable=scvalue,font="lucida 20 ",bg="#FFF5E1",fg="#0C1844",width=80,relief="flat")
ent.pack(ipadx=2,ipady=2,padx=(30, 20),anchor="center",side=LEFT)
b = Button(topFrame,text="Search",font="lucida ",bg="#0C1844",fg="#FFF5E1",relief="flat")
b.pack(side="left", anchor="n", ipadx=5, padx=10, pady=10, fill="x")
b.bind("<Button-1>", searching)
topFrame.pack(fill=X)


midFrame = Frame(window,bg="#0C1844",height=50)
bt_name = ["Popular/Trending","Sports","Technology","Entertainment","Business"]
for i in range(5):
    b = Button(midFrame,text=f"{bt_name[i]}",font="lucida ",bg="#0C1844",fg="#FFF5E1",relief="flat")
    b.pack(side="left", anchor="center", ipadx=5, padx=5, pady=5, fill="x")
    b.bind("<Button-1>", click)
midFrame.pack(fill=X)
botFrame = Frame(window,height=float(screen_height-40),bg="#FF6969")

image = Image.open("logonew.jpg")

photo= ImageTk.PhotoImage(image)
label2 = Label(botFrame,image = photo,bd=0)
label2.pack()


frame1 =Frame(botFrame,height=float(screen_height-40),borderwidth=5, bg="#FF6969")

frame1.pack(fill=BOTH)


frame2 =Frame(botFrame,height=float(screen_height-40),borderwidth=5,bg = "#FF6969")
frame2.pack(fill=X)

botFrame.pack(fill=X)

window.mainloop()