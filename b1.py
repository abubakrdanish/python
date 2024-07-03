import FreeSimpleGUI as sg
import zip_creator
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 =sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress = sg.Button("Compress")
output = sg.Text(key="output")
window = sg.Window("Files to compress",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[compress,output]])


while True:

    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepaths,folder)
    window["output"].update(value = "Compression Completed!")
window.close()