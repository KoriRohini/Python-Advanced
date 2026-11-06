from time import sleep

def download_file(name):
    print("Downloading", name)
    sleep(0.5)
    print("Downloaded", name)

files = ["image.png", "video.mp4", "data.csv"]

for f in files:
    download_file(f)

print("Bye")