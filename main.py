import pytube

url = input("enter video url: ")

pytube.YouTube(url).streams.get_audio_only().download()