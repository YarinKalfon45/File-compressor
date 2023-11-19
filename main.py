import PySimpleGUI as pg
from zip_creator import create_dircetory

pg.theme("Black")
label1 = pg.Text("Select files to compress: ")
input_box1 = pg.Input()
choose_button1 = pg.FilesBrowse("Choose",key="files")

label2 = pg.Text("Select destination folder: ")
input_box2 = pg.Input()
choose_button2 = pg.FolderBrowse("Choose",key="dest")


compress_Button = pg.Button("Compress")
output = pg.Text("",key="output",text_color="Green")
window = pg.Window("File compressor",
                   layout=[[label1, input_box1, choose_button1],
                           [label2, input_box2, choose_button2],
                           [compress_Button,output]],
                   font=('Helvetica', 15))
while True:
    try:
        event, values = window.read()
        filepaths = values["files"].split(";")
        dest = values['dest']
        create_dircetory(filepaths,dest)
        window['output'].update(value="Compression completed!")
        # window['files'].update(value="")
        # window['dest'].update(value="")
        if event == pg.WIN_CLOSED:
            window.close()
    except TypeError:
        pg.popup("Please try again")

