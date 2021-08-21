from tkinter import *
import base64


'''

mozna dodac funkcjonalnosc wysylania na maila od razu do kogos wiadomosci

i wtedy moze to tak wygladac
dwie os maja apke na kompie
odszyfrowuje sobie w apce co mu przyszlo
szyfruje wlasna wiadomosc i jednym przyciskiem wysyla mu na maila

oczywiscie obie osoby musza miec jeden klucz do komunikacji


'''

root = Tk()
root.geometry('500x300')
root.resizable(0,0)

root.title("Message encoding and decoding")



#Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()


#define variables

Text = StringVar()
private_key = StringVar()
mode_decoding = StringVar()
mode_encoding = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    try:
        enc=[]
        for i in range(len(message)):
            key_c = key[i % len(key)]
            enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
            
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    except:
        return 'lack of key'

#function to decode

def Decode(key,message):
    try:
        dec=[]
        message = base64.urlsafe_b64decode(message).decode()
        for i in range(len(message)):
            key_c = key[i % len(key)]
            dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
            
        return "".join(dec)

    except:
        return 'invalid data'

#function to set mode
def Mode(typee):
    if(typee == 1):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(typee == 2):
        Result.set(Decode(private_key.get(), Text.get()))



#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode_decoding.set("")
    mode_encoding.set("")
    Result.set("")

def copytoclipboard():

    root.clipboard_clear()
    root.clipboard_append(Result.get())
    root.update()



#################### Label and Button #############

#Message
Label(root, font= 'helvetica 13 bold', text='Message').place(x= 120,y=60)
Entry(root, font = 'helvetica 13', textvariable = Text).place(x=220, y = 57)

#key
Label(root, font = 'helvetica 13 bold', text ='Key').place(x=120, y = 90)
Entry(root, font = 'helvetica 13', textvariable = private_key).place(x=220, y = 87)


#mode
Label(root, font = 'helvetica 13 bold', text ='Mode').place(x=120, y = 120)
Radiobutton(root, font = 'helvetica 13', text='encoding', command=lambda:Mode(1)).place(x=220, y = 118)
Radiobutton(root, font = 'helvetica 13', text='decoding', command=lambda:Mode(2)).place(x=310, y = 118)



#result
Entry(root, font = 'helvetica 13 bold', textvariable = Result).place(x=220, y = 148)
Button(root, font = 'helvetica 11', text='Copy', command=copytoclipboard).place(x=400,y=148)

######result button
Label(root, font = 'helvetica 13 bold', text = 'Result'  ,padx =2).place(x=120, y = 150)


#reset button
Button(root, font = 'helvetica 13 bold', text ='Reset' ,width =6, command = Reset, padx=2).place(x=205, y = 220)

root.mainloop()
