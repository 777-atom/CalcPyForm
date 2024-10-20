# Библиотека
from tkinter import*

# Шаблон вызывающий при нажатие на клавишу 
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
    
# Шаблон вызывающий при нажатие стирания
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
    
# Шаблон вызывающий при нажатие равно
def btnEqualsInput():
    global operator
    summup=str(eval(operator))
    text_Input.set(summup)
    operator=summup

# Форма 
calc = Tk()
# Титулник
calc.title("Калькулятор")
# создаем операнды
operator=""
text_Input = StringVar()

txtDisplay = Entry(calc, font=('Times New Roman', 21, 'bold'), textvariable=text_Input, bd=1, insertwidth=4, bg="#E0E0E0", justify='right').grid(columnspan=4)

# Создаем кнопки ( чем то мне напоминает Javasript)
btn7=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="7", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="-", command=lambda:btnClick("-")).grid(row=1, column=3)

btn4=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
Addition=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="*", command=lambda:btnClick("*")).grid(row=2, column=3)

btn1=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="1", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="3", command=lambda:btnClick(3)).grid(row=3, column=2)
Addition=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="/", command=lambda:btnClick("/")).grid(row=3, column=3)

btn0=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="0", command=lambda:btnClick(0)).grid(row=4, column=0)
btn_del=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="C", command=lambda:btnClearDisplay()).grid(row=4, column=1)
Addition=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="+", command=lambda:btnClick("+")).grid(row=4, column=2)
btnEqualsInput=Button(calc, padx=16, bd=1, fg="#000", font=('Times New Roman', 21, 'bold'), text="=", command=btnEqualsInput).grid(row=4, column=3)



# Выводим
calc.mainloop()

