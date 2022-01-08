from youtube_search import YoutubeSearch
from pytube import YouTube
import os
def SearchYoutube():
    results = YoutubeSearch(input("Search:"), max_results=10).to_dict()
    #print(results)
    for i in range(10):
        print(i+1,results[i]["title"])
    
    selectedInd= int(input("Selecione Video:"))
    VidURL=results[selectedInd-1]["url_suffix"]
    return VidURL
def downladVid(yt):
    #print(yt.streams.filter(file_extension='mp4'))
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download()
    except:
        print("Qualidade nao Encontrada:")

def menu():
    os.system("cls")
    print("YoutubeDownload \n")
    op=int(input("1-Introduzir Link\n2-Procurar Video\n"))
    
    if(op==1):
        link = input("Introduza Link:\n")
        yt=YouTube(link)
        downladVid(yt)
    elif(op==2):
        link="https://www.youtube.com"+SearchYoutube()
        yt = YouTube(link)
        downladVid(yt)
    else:
        print("Introduza Opcao Valida\n")

menu()



