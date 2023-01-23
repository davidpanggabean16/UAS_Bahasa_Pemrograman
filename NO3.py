import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku disentuh")
    label2.pack()

label = tkinter.Label(main_window, text="Hallo, saya adalah \n GUI yang sangat sederhana \n dibuat dengan bahasa pemrograman pyhton")
tombol = tkinter.Button(main_window, text="tekan saya", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()
