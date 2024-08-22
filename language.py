from translate import Translator
import tkinter as tk

window = tk.Tk()
window.title('Language Translator')
window.config(bg='pink')
window.geometry('900x450')

def translate():
  textbox2.delete('1.0','end')
  var1 = textbox1.get('1.0','end-1c')
  translator = Translator(from_lang=lang1.get()
  ,to_lang=lang2.get())
  translation = translator.translate(str(var1))
  textbox2.insert('end',translation)

title_label = tk.Label(window,text='Language Translator',font=('Bell MT',30),fg='red')
title_label.pack(pady=(20,0))

lang1 = tk.StringVar()
lang2 = tk.StringVar()

choices = ['English','Spanish','German','Chinese']
lang1.set('English')
lang2.set('Spanish')

lan1_menu = tk.OptionMenu(window,lang1,*choices)
lan1_menu.config(font=('Helvetica',20))
lan1_menu.pack(side=tk.LEFT,padx=(130,0),pady=(0,150))

lan2_menu = tk.OptionMenu(window,lang2,*choices)
lan2_menu.config(font=('Helvetica',20))
lan2_menu.pack(side=tk.RIGHT,padx=(0,100),pady=(0,150))

textbox1 = tk.Text(window, height = 8, width = 30
                , font=('Verdana',10))
textbox1.place(in_=lan1_menu,relx = 0, x = -60,
               rely = 1.5)
textbox2 = tk.Text(window, height=8, width=30,
                font=('Verdana',10))
textbox2.place(in_=lan2_menu, relx = 0, x = -60,
               rely = 1.5)
translate_Button = tk.Button(window,text='Translate',
                  width=10,font=('Agency Fb',30)
                  ,command=translate)
translate_Button.pack(pady=(0,40),side=tk.BOTTOM)

window.mainloop()