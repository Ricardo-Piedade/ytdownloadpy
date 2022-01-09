from youtube_search import YoutubeSearch
from pytube import YouTube,Playlist
from tkinter import Tk, filedialog
import os
def SearchYoutube():
    results = YoutubeSearch(input("Search:"), max_results=10).to_dict()
    #print(results)
    for i in range(10):
        print(i+1,results[i]["title"])
    
    selectedInd= int(input("Selecione Video:"))
    VidURL=results[selectedInd-1]["url_suffix"]
    return VidURL

def downladVid(yt,path):
    #print(yt.streams.filter(file_extension='mp4'))
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
    except:
        print("Stream Not Found")

def downladMus(yt,path):
    try:
        stream = yt.streams.filter(only_audio=True)[1]
        print(stream)
        stream.download(output_path=path)
    except:
        print("Stream Not Found")
def pathChooser():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost',True)
    path = filedialog.askdirectory()
    return path
def menu():
    os.system("cls")
    print("Youtube Download \n")
    op=int(input("1-Introduzir Link\n2-Procurar Video\n3-Playlist\n"))

    if(op==1):
        link = input("Introduza Link:\n")
        yt=YouTube(link)
        v=int(input("1-Audio \n2 - Video\n"))
        if(v==1):
            downladMus(yt,pathChooser())
        else:
            downladVid(yt,pathChooser())
    elif(op==2):
        link="https://www.youtube.com"+SearchYoutube()
        yt = YouTube(link)
        v=int(input("1-Audio \n2-Video\n"))
        if(v==1):
            downladMus(yt,pathChooser())
        else:
            downladVid(yt,pathChooser())
    elif(op==3):
        link = input("Introduza Link da Playlist:\n")
        p=Playlist(link)
        v=int(input("1-Audio\n2-Video\n"))
        path=pathChooser() 
        for i in p.videos:
            if(v==1):
                i.streams.get_audio_only().download(output_path=path)
            else:
                i.streams.filter(file_extension="mp4").get_highest_resolution().download(output_path=path)     
    else:
        print("Introduza Opcao Valida\n")

menu()



