from tkinter import *
from tkinter import ttk
from pytube import YouTube,Playlist
from tkinter import filedialog
folder_name=""
 
def downloadvideo():
    try:
        ch=ytbchoice.get()
        url=URLEntry.get()
        if(len(url)>1):
            URLerror.config(text="")
            video_yt=YouTube(url)  
            if(ch==choices[0]):
                select=video_yt.streams.filter(progressive=True,file_extension="mp4").get_highest_resolution()
            elif(ch==choices[1]):
                select=video_yt.streams.filter(progressive=True,file_extension="mp4").get_lowest_resolution()
            elif(ch==choices[2]):
                select=video_yt.streams.filter(only_audio=True).first()
            elif(ch == choices[3]):
                select=video_yt.streams.filter(
                    file_extension='mp4', type='video', progressive="True", res=choices[3]).download(folder_name)
            elif(ch == choices[4]):
                select=video_yt.streams.filter(
                    file_extension='mp4', type='video', progressive="True", res=choices[4]).download(folder_name)
            elif(ch == choices[5]):
                select=video_yt.streams.filter(
                    file_extension='mp4', type='video', progressive="True", res=choices[5]).download(folder_name)
                     
                     
             
        else:
            URLerror.config(text="paste URL again",fg="red")    
        select.download(folder_name)
        Downloadlabel.config(text="Download completed!",fg="green")
    except Exception as err:
        print(err)

#def downloadPlaylist(): 
       # For Download PlayLists

        #ch=ytbchoice.get()
        #url=URLEntry.get()
        #playlist = Playlist(url)

       #for pl in playlist.videos:
            #for video in pl.streams.filter(type='video',file_extension='mp4', progressive="True", res=ch):
               # video.download(output_path=folder_name)        
def openlocation():
    global folder_name
    folder_name=filedialog.askdirectory()
    if(len(folder_name)>1):
        Downloadlabel.config(text=folder_name,fg="#7697A0")
        #if(vd.get()==1):
        downloadvideo()
        #else:
          #  downloadPlaylist()
    
        
    else:
        Downloadlabel.config(text="choose folder to save",fg="red") 
pd=Tk()
pd.title("Youtube video Downloader")
#pd.iconbitmap(r'E:\YouTube_icon.ico')
#pd.columnconfig(0,width=1)#set all content in center
label1=Label(pd,text="__Youtube video Downloader__",fg="#092147",font=("arial",20))
label1.grid(row=0,padx=100,pady=30)
URLlabel=Label(pd,text="Please Paste Video URL",fg="#092147",font=("arial",15))
URLlabel.grid(row=1)
URLEntry=Entry(pd,width=20,font=("arial",15))
URLEntry.grid(row=2,pady=6)
#vd = IntVar()
#e1= Radiobutton(pd, text='Video', variable=vd,value=1).grid(row=3)
#e2= Radiobutton(pd, text='Playlist', variable=vd,value=2).grid(row=4)
URLerror=Label(pd,text="",font=("arial",15),fg="red")
URLerror.grid(row=5,pady=10)
choicelabel=Label(pd,text="choose quality of video",fg="#092147",font=("arial",15))
choicelabel.grid(row=6)
choices=["High quality video","Low quality video","Audio file",'360p ','480p' ,'720p' ]
#qty= StringVar()
#qty.set(choices[2])
ytbchoice =ttk.Combobox(pd,values=choices ,font=("arial",15))
ytbchoice.grid(row=7,pady=10)
m_Label = Label(pd, text='Developed by Mirna mohamed', foreground='black', font=("arial",15))
m_Label.grid(row=8)
downloadbotton=Button(pd,text="Download",command=openlocation,bg="#97B2DE",fg="#092147",width=50,font=("arial",15))
downloadbotton.grid(row=9,pady=10)
Downloadlabel=Label(pd,text="",font=("arial",15))
Downloadlabel.grid(row=10,padx=1,pady=10)
pd.mainloop()
