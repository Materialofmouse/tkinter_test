# -*- coding: utf8 -*-
#! /usr/bin/python3
import sys
import tkinter as tk

class GUI_Config():
  def __init__(self):
    self.title = u'DockeFileに吐き出す'
    self.size = u'400x300'

class Write():
  def __init__(self,command_list):
    self.f = open('Dockerfile','w')
    self.f.write('FROM ubuntu:16.04\n')
    self.f.write('RUN apt-get update && ')
    
  def write_list(self,command_str):
    command = 'apt-get install -y '
    for i in command_str:
      command += (str(command_list[int(i)]) + ' \\\n')    
    
    self.f.write(command)
    print('writed Dockerfile')
    self.f.close()
    sys.exit()

#gui settings
#get check list
def get_check(event):
  global com_str
  global w
  for i,var in enumerate(var_check):
    if var.get() == True:
      com_str += str(i)
  
  return w.write_list(com_str)

#make checkbox
def make_checkbox():
  check = []
  for i,var in enumerate(command_list):
    var_check.append(tk.BooleanVar())
    var_check[i].set(False)
    check.append(tk.Checkbutton(frame,text=str(var),variable=var_check[i]))
    check[i].pack(padx=5,pady=5,anchor=tk.W)


#gui setting
config = GUI_Config() 

root = tk.Tk()
root.title(config.title)#window title
#root.geometry(config.size)#window size

frame = tk.Frame(root)
frame.pack()

#checkbox
var_check = []
com_str = ''

#command
command_list = ['python3.6','python2.7','git','mercurial','vim']
w = Write(command_list)

make_checkbox()
button = tk.Button(frame,text=u'Dockerfile吐き出し',width=20)
button.bind('<Button-1>',get_check)
button.pack()

tk.mainloop()
