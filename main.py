import os
import shutil
downloads=os.path.join(os.path.expanduser("~"), "Downloads")
#now defining subfolders to store stuff
folders={
    "Pictures":[".png",".jpeg",".jpg",".gif",".bmp"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".epub"],
    "Archives/compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Applications": [".exe", ".msi"],
    "Projects/randomshiz?": [".sb3", ".bmpr"],
}
#for other things
folders["Others"]=[]

#making those folders
for i in folders:
    folder_path=os.path.join(downloads,i)
    os.makedirs(folder_path, exist_ok=True) #dont use mkdir cuz it throws error if it already exists

for item in os.listdir(downloads):
    item_path=os.path.join(downloads, item)

    if os.path.isdir(item_path): #if its a folder then move to "folders"
        os.makedirs(os.path.join(downloads, "Folders"), exist_ok=True)
        dest_path=os.path.join(downloads, "Folders", item)
        shutil.move(item_path,dest_path)

        print(f"moved {item} to folders")
        continue

    file_ext=os.path.splitext(item)[1].lower()
    


