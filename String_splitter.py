#!%usr%bin%env python

# transform sentences to maximum 30 chars per line
# encoding=utf8


from os import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf8')
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

#vStr='Easy to melts so regularly used for fondue with Gruyere and sauce'
#vStr= 'Good for cold sandwich, baking and grated for pizza and pasta.'
#vStr='Have this on cheese platter with dried nuts and bread. Perfect for sandwich, grated for pasta and fondue.

def words_slice(vStr):

    len(vStr.split())

    #print vStr.index()
    list=[]
    i=0
    vWord=''
    for vChar in vStr.split():        
        list.append(vChar) 
        
        i=i+1
        lWord=float(len(vWord))
        vlimit=float(30)
        vResult= len(vWord)/30
        dPoint= round((lWord/vlimit)%1,1)
        vMod= len(vWord)%30
        
        if (dPoint<=1.0 and vResult==0 and vMod <25): 
            if (len(vWord)+len(' '+vChar)<30 and len(vWord.split('\n'))>0):
                if (vWord==''):
                    vWord+=vChar
                else:
                    vWord+=' '+vChar
        elif (dPoint<=1.0 and vResult>0 and vMod <25):
            if (len(vWord)+(len(' '+vChar)-30)<30 and len(vWord.split('\n'))>0):
                if (vWord==''):
                    vWord+=vChar
                else:
                    vWord+=' '+vChar
            else:
                    if ((len(vWord)+len(' '+vChar))-30<60 and vMod<60 and len(vWord.split('\n'))>1):
                        if ('\n' in vWord): 
                            if (80>(len(vWord)+len(vChar))>50 and len(vWord.split('\n'))>2):
                                vWord+=' '+vChar
                            elif (100>(len(vWord)+len(vChar))>80 and len(vWord.split('\n'))>3):
                                vWord+=' '+vChar
                            elif (120>(len(vWord)+len(vChar))>100 and len(vWord.split('\n'))>4):
                                vWord+=' '+vChar                            
                            elif (140>(len(vWord)+len(vChar))>120 and len(vWord.split('\n'))>5):
                                vWord+=' '+vChar                                                            
                            else :
                                vWord+='\n'+vChar
                        else :
                            vWord+=' '+vChar    
                    else:                                      
                        vWord+=' '+vChar
        else:
            if ('\n' not in vWord): 
                if (len(vWord)+len(' '+vChar)>30):            
                    vWord+='\n'+vChar
                else:
                    vWord+=' '+vChar
            else:
                if (80>(len(vWord)+len(vChar))>50 and len(vWord.split('\n'))>2):
                    vWord+=' '+vChar
                elif (100>(len(vWord)+len(vChar))>80 and len(vWord.split('\n'))>3):
                    vWord+=' '+vChar
                elif (120>(len(vWord)+len(vChar))>100 and len(vWord.split('\n'))>4):
                    vWord+=' '+vChar                            
                elif (140>(len(vWord)+len(vChar))>120 and len(vWord.split('\n'))>5):
                    vWord+=' '+vChar                                                
                else :  
                    vWord+='\n'+vChar
    #numbering            
    vline=vWord.split('\n')    
    newWord=''
    for k,val in enumerate(vline):
        if (newWord==''):
            newWord+='+'+str(k+1)+val
        else:
            newWord+='\n+'+str(k+1)+val

        print '+'+str(k+1)+val        
            
    print newWord
    
    return newWord            


def show_entry_fields(event=None):

    tString=StringVar()
    tString=words_slice(userinput.get())

    master.clipboard_clear()
    master.clipboard_append(tString)
    messagebox.showinfo("Copy Done", "Already copied your transform sentence!")

master = Tk()

master.title("Words spliting by sentences Program")

userinput = StringVar()

Label(master, text="Import text ").grid(row=0)
e1 = Entry(master, textvariable=userinput).grid(row=0, column=1)

userinput.get()

Button(master, text='Quit', command=master.quit,underline=0).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Transform', command=show_entry_fields,underline=0).grid(row=3, column=1, sticky=W, pady=4)    

master.bind('<Alt_L><q>', lambda e:master.quit())
master.bind('<Alt_L><t>', lambda e:show_entry_fields())
mainloop( )


    