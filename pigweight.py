import datetime
import tkinter as tk

window = tk.Tk()
window.title("pig weight Calculator")
window.geometry('250x300')
class pig(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def show(self):
        print('{} \n{} months old'.format(self.name, self.age))


heart_girth = tk.Label(text="heart girth")
heart_girth.grid(column=0, row=1)

girth = tk.Entry(master=window)
girth.grid(column=1, row=1)

space=tk.Label(window, text=' ')
space.grid(column=0, row=2)

lenght = tk.Label(text="lenght")
lenght.grid(column=0, row=3)

back = tk.Entry(master=window)
back.grid(column=1, row=3)

def calc_weight():
    ans = []
    girth_result = float(girth.get()) ** 2
    pndz = girth_result * float(back.get())/400
    kg = pndz/2.2046
    ans.append(kg)
    text_answer = tk.Text(master=window, height=2, width=15)
    text_answer.grid(column=1, row=6)
    answer_text = ans[0]
    text_answer.insert(tk.END, answer_text)
    text_answer.tag_configure('bold_italics', font=('Helvetica', 12, 'bold', 'italic'))
    

button1 = tk.Button(text="Calculate", command=calc_weight)
button1.grid(column=1, row=4)




'''
class calc(object):
    def __init__(self, heart_girth, lenght):
        self.heart_girth=heart_girth
        self.lenght=lenght
    def soul(self):
        girth_result=self.heart_girth**2
        pndz=girth_result*self.lenght/400
        kg=pndz/2.2046
        print('pig weight: {} kg'.format(kg))

        #print('{}'.format())


        

big_joe=pig('big joe', 16)
big_joe.show()

k=calc(int(input('heart girth: ')), int(input('lenght: ')))
k.soul()'''

window.mainloop()