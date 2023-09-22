import os
import shutil
import time
import PySimpleGUI as sg
import math

def backup(source_folder, destination_folder): # Checks if destination_folder is available and if so, copies from source_folder to destination_folder
    
    while True:
        if os.path.exists(destination_folder):
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(destination_folder, os.path.relpath(src_file, source_folder))
                    try:
                        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                        if os.path.exists(dst_file):
                            os.remove(dst_file)
                        shutil.copy2(src_file, dst_file)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Copying {src_file}")
                    except:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Error occured while copying {file}")
                        continue
                # copy Folders
                for d in dirs:
                    src_folder = os.path.join(root, d)
                    dst_folder = os.path.join(destination_folder, os.path.relpath(src_folder, source_folder))
                    try:
                        shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)
                    except:
                        print(f"Error occured while copying {d}")
                        continue
            print("Copying finished successfully!")
            break
        else:
            time.sleep(60)

def convert_size(size_bytes): #Convertes Bytes to kB, MB, GB, TB, or PB
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_size(start_path): #Works together with convert_size() and gives out the size of given path
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return convert_size(total_size)

def display(b1, b2, b3): #display modul with variable amounts of buttons
    layout = [[sg.Text("Choose Folder to Copy")], 
          [sg.Button(b1), sg.Text(get_size(r'C:\Users\mlcra\Desktop\source'))],
          [sg.Button(b2), sg.Text(get_size(r'C:\Users\mlcra\OneDrive - HTL-Rankweil'))],
          [sg.Button(b3), sg.Text('Quit')]
          ]
    window = sg.Window("Backup", layout,size=(300, 150))
    while True:
        event, values = window.read()

        if event == b1: 
            backup(r"C")
        if event == b2:
            backup(r"D")
        if event == b3: #quit button
            quit()
        if event == sg.WINDOW_CLOSED: #quit on x button
            quit()

def main():
    display("Button1", "Button2", "Quit_Button")

main()
