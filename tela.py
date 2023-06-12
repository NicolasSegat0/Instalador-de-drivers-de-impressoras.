from tkinter import *
import urllib.request
import os

window = Tk()
window.title('Driver Impressoras')
window.geometry('440x300')
window.minsize(440, 300)
window.maxsize(440, 300)
window.configure(background='#3282d2')


def download(url, file_name):
    user_download_folder = os.path.expanduser('~/Downloads')

    file_path = os.path.join(user_download_folder, file_name)

    try:
        urllib.request.urlretrieve(url, file_path)
        print('Download concluído com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro durante o download: {e}')


def download_xerox():
    url = 'https://download.support.xerox.com/pub/drivers/6510/drivers/win10/ar/XeroxSmartStart_1.8.10.0.exe'
    file_name = 'XeroxSmartStart_1.8.10.0.exe'
    download(url, file_name)


def download_brother1():
    url = 'https://download.brother.com/welcome/dlf102382/Y15B_C1_ULWT-inst-J1.EXE'
    file_name = 'Y15B_C1_ULWT-inst-J1.exe'
    download(url, file_name)


def download_brother2():
    url = 'https://download.brother.com/welcome/dlf102770/Y15C_C1-hostm-J1.EXE'
    file_name = 'Y15C_C1-hostm-J1.exe'
    download(url, file_name)


lblNome1 = Button(window, text='Xerox Altalink B8170', command=download_xerox)
lblNome1.place(x=120, y=10, width=200, height=30)

lblNome2 = Button(window, text='Brother 6402', command=download_brother1)
lblNome2.place(x=120, y=50, width=200, height=30)

lblNome3 = Button(window, text='Brother 6902', command=download_brother2)
lblNome3.place(x=120, y=90, width=200, height=30)


window.mainloop()
