import os
import shutil
import time
import PySimpleGUI as sg

def backup(source_folder, destination_folder):
    #source_folder = r"C:\Users\mlcra\Desktop\source"
    #destination_folder = r"C:\Users\mlcra\Desktop\destination"
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

def display(b1, b2, b3): #display modul with variable amounts of buttons
    layout = [[sg.Text("Welcher Ordner soll Kopiert werden")], 
          [sg.Button(b1)],
          [sg.Button(b2)],
          [sg.Button(b3)]

          ]
    window = sg.Window("HDD Backup", layout)



    while True:
        event, values = window.read()

        if event == b1: 
            backup(r"C:\Users\mlcra\Desktop\source", r"C:\Users\mlcra\Desktop\destination")
        if event == b2:
            ()
        if event == b3: #quit button
            quit()
            
        

        if event == sg.WINDOW_CLOSED: #endet programm
            quit()

def main():
    display("Button1", "Button2", "Quit_Button")

main()