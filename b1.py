import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 =sg.FilesBrowse("Choose")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")
compress = sg.Button("Compress")
window = sg.Window("Files to compress",label[[label1,input1,choose_button1],[label2,input2,choose_button2],[compress]])

window.read()
window.close()