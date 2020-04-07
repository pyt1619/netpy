import tkinter as tk
import decimal
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import os, random
root = Tk()
root.title("netpy")
root.geometry("720x420")
root.resizable(width=False, height=False)

tab_control = ttk.Notebook(root)  
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='сеть TOR')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='MAC')  
tab_control.pack(expand=1, fill='both')  

rm = Label(tab1,text = '     ', font="Arial 1100")
rm.pack()
rm.place(relx=0.5, rely=0.5,anchor="c", bordermode=OUTSIDE)

rm2 = Label(tab2,text = '     ', font="Arial 1100")
rm2.pack()
rm2.place(relx=0.5, rely=0.5,anchor="c", bordermode=OUTSIDE)

# сеть тор

def connect_tor():
	os.system("toriptables2.py -l > /root/py_clock/doc.txt ; curl suip.biz/ip/ > doc.txt")
	my_file = open("doc.txt")
	my_string = my_file.read()
	my_file.close()
	r2_7.configure(text = 'IP - '+my_string)
def disconnect_tor():
	os.system("toriptables2.py -f > /root/py_clock/doc.txt ; curl suip.biz/ip/ > doc.txt")
	my_file = open("doc.txt")
	my_string = my_file.read()
	my_file.close()
	r2_7.configure(text = 'IP - '+my_string)
def rebconnect_tor():
	os.system("sudo kill -HUP $(pidof tor) ; curl suip.biz/ip/ > doc.txt ; curl suip.biz/ip/ > doc.txt")
	my_file = open("doc.txt")
	my_string = my_file.read()
	my_file.close()
	r2_7.configure(text = 'IP - '+my_string)
r1_7 = Label(tab1,text = 'ТОР', font="Arial 34")
r1_7.pack()
r1_7.place(relx=0.5, rely=0.15,anchor="c", bordermode=OUTSIDE)

r2_7 = Label(tab1,text = 'IP - NONE', font="Arial 26")
r2_7.pack()
r2_7.place(relx=0.5, rely=0.7,anchor="c", bordermode=OUTSIDE)

btn_1_7 = Button(tab1, text="Подключиться", command=connect_tor,font="Arial 20", borderwidth=0)
btn_1_7.pack()
btn_1_7.place(relx=0.2, rely=0.4,anchor="c", bordermode=OUTSIDE)

btn_2_7 = Button(tab1, text="Отключиться", command=disconnect_tor,font="Arial 20", borderwidth=0)
btn_2_7.pack()
btn_2_7.place(relx=0.5, rely=0.4,anchor="c", bordermode=OUTSIDE)

btn_3_7 = Button(tab1, text="Переподключ.", command=rebconnect_tor,font="Arial 20", borderwidth=0)
btn_3_7.pack()
btn_3_7.place(relx=0.8, rely=0.4,anchor="c", bordermode=OUTSIDE)

os.system("curl suip.biz/ip/ > doc.txt")
# my_filex =  open("doc.txt", 'w')
# # my_stringx = my_filex.read()s
# my_filex.close()

my_filex = open("doc.txt")
my_stringx = my_filex.read()
my_filex.close()
r2_7.configure(text = 'IP - '+my_stringx)
# сеть тор

# MAC
# global net_interface
def question():
	res=messagebox.askyesno('Сменить MAC', 'Подтвердить смену MAC адреса?')
	return(res)
net_interface = ["eth0","80:7a:bf"]

def interface(selection):
	net_interface[0]=selection
def new_mac(selection):
	# pass
	text_v2.set((selection[0:8]).lower()+":00:00:00")

def new_mac_random(selection):
	net_interface[1]=selection[0:8].lower()
	print(net_interface)
def random_mac():
	if question():
		os.system("macchanger -r "+net_interface[0])
def rych_mac():
	if len(text_1.get()) == 17 and question():
		os.system("macchanger --mac "+text_1.get().lower()+" "+net_interface[0])
def rand_mac_pr():
	# net_interface[1]+=':'
	if question():
		if len(net_interface[1])==len("80:7a:bf"):
			for i in range(3):
				x=random.randint(10,99)
				net_interface[1]+=":"+str(x)

		os.system("macchanger --mac "+net_interface[1].lower()+" "+net_interface[0])
def rych_mac_pr():
	if len(text_2.get()) == 17 and question():
		os.system("macchanger --mac "+text_2.get().lower()+" "+net_interface[0])
def reboot_mac():
	if question():
		os.system("macchanger -p "+net_interface[0])
r1_2 = Label(tab2,text = 'MAC', font="Arial 34")
r1_2.pack()
r1_2.place(relx=0.5, rely=0.15,anchor="c", bordermode=OUTSIDE)

# r2_7 = Label(tab2,text = 'IP - NONE', font="Arial 26")
# r2_7.pack()
# r2_7.place(relx=0.5, rely=0.7,anchor="c", bordermode=OUTSIDE)

btn_1_2 = Button(tab2, text="Сменить рандомно", command=random_mac,font="Arial 17", borderwidth=0)
btn_1_2.pack()
btn_1_2.place(relx=0.2, rely=0.3,anchor="c", bordermode=OUTSIDE)

btn_2_2 = Button(tab2, text="Сменить вручную >>", command=rych_mac,font="Arial 17", borderwidth=0)
btn_2_2.pack()
btn_2_2.place(relx=0.2, rely=0.4,anchor="c", bordermode=OUTSIDE)

btn_3_2 = Button(tab2, text="      Сменить рандомно      >>\n для этого производителя >>", command=rand_mac_pr,font="Arial 17", borderwidth=0)
btn_3_2.pack()
btn_3_2.place(relx=0.23, rely=0.55,anchor="c", bordermode=OUTSIDE)

btn_4_2 = Button(tab2, text="      Сменить вручную      >>\n для этого производителя >>", command=rych_mac_pr,font="Arial 17", borderwidth=0)
btn_4_2.pack()
btn_4_2.place(relx=0.23, rely=0.75,anchor="c", bordermode=OUTSIDE)

btn_5_2 = Button(tab2, text="Восстановить MAC адрес", command=reboot_mac,font="Arial 17", borderwidth=0)
btn_5_2.pack()
btn_5_2.place(relx=0.5, rely=0.9,anchor="c", bordermode=OUTSIDE)

variable = StringVar(root)
variable.set("eth0")

w = OptionMenu(tab2, variable, "eth0", "eth1", "wlan0", "wlan1", "wlan0mon", "wlan1mon", command=interface)
w.pack()
w.place(relx=0.93, rely=0.09,anchor="c", bordermode=OUTSIDE)
r6 = Label(tab2,text = 'Интерфес', font="Arial 10")
r6.pack()
r6.place(relx=0.93, rely=0.03,anchor="c", bordermode=OUTSIDE)

text_v1 = StringVar()

text_1 = Entry(tab2, width=14,font="Arial 17", textvariable=text_v1) # тобы отключить добавить state='disabled'
text_1.pack()
text_1.place(relx=0.5, rely=0.4,anchor="c", bordermode=OUTSIDE)
text_v1.set('00:00:00:00:00:00')

os.system("ifconfig | grep ether > doc2.txt")
my_filex = open("doc2.txt")
my_stringx = my_filex.read()
my_filex.close()
my_stringx=my_stringx[14:31]
text_v1.set(my_stringx)

variable2 = StringVar(root)
variable2.set("80:7A:BF HTC")
w2 = OptionMenu(tab2, variable2, "00:50:BA D-Link", "00:E0:FC Huawei Technologies", "80:7A:BF HTC", "00:1A:11 Google", "00:11:75 Intel", "74:A7:8E zte","E0:05:C5 Tp-link Technologies","44:E0:8E Cisco Spvtg","48:50:73 Microsoft","C8:A9:FC Goyoo Networks","A8:C8:7F Roqos","08:3A:5C Junilab","84:DF:19 Chuango Security Technology","F8:5B:9C SB Systems", command=new_mac_random)
w2.pack()
w2.place(relx=0.75, rely=0.55,anchor="c", bordermode=OUTSIDE)

variable3 = StringVar(root)
variable3.set("80:7A:BF HTC")
w3 = OptionMenu(tab2, variable3, "00:50:BA D-Link", "00:E0:FC Huawei Technologies", "80:7A:BF HTC", "00:1A:11 Google", "00:11:75 Intel", "74:A7:8E zte","E0:05:C5 Tp-link Technologies","44:E0:8E Cisco Spvtg","48:50:73 Microsoft","C8:A9:FC Goyoo Networks","A8:C8:7F Roqos","08:3A:5C Junilab","84:DF:19 Chuango Security Technology","F8:5B:9C SB Systems", command=new_mac)
w3.pack()
w3.place(relx=0.75, rely=0.7,anchor="c", bordermode=OUTSIDE)

text_v2 = StringVar()

text_2 = Entry(tab2, width=14,font="Arial 17", textvariable=text_v2) # тобы отключить добавить state='disabled'
text_2.pack()
text_2.place(relx=0.75, rely=0.8,anchor="c", bordermode=OUTSIDE)
text_v2.set(('80:7A:BF:00:00:00').lower())
# MAC


root.mainloop()