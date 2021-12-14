from tkinter import *
def switchoff():
    print("the switch is off") 

def switchon():
    print('the switch is on')

def Switch():
    
    print("the switch is off") 
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        toggle_button.config(bg= 'yellow') 
        toggle_button.config(fg= 'black') 
        

    else:
        toggle_button.config(text='ON')
        toggle_button.config(bg= 'black')
        toggle_button.config(fg= 'red') 
        print("the switch is on") 
    
         

ws = Tk()
ws.title("Python Guides")
ws.geometry("200x100")

toggle_button = Button(text="OFF", width=10, command=Switch)
toggle_button.pack(pady=10)

ws.mainloop()




    









