import tkinter as tk
from tkinter import font

MAX_NUM = 12

num1, num2, operator = None, None, None
is_operation = False
is_result = False

last_button = None
last_button_bg = None
last_button_fg = None


def get_result():
    global num1, num2, operator, is_result
    result = 0
    num2 = input_.get()

    if num1 is not None:
        match operator:
            case '%':
                result = (float(num2) / 100) * float(num1)
            case '÷':
                result = float(num1) / float(num2)
            case 'x':
                result = float(num1) * float(num2)
            case '+':
                result = float(num1) + float(num2)
            case '-':
                result = float(num1) - float(num2)

        input_.delete(0, 'end')
        input_.insert('end', str(round(result, 3)))
        is_result = True


def clear_input():
    input_.delete(0, 'end')


def click_clear_button():
    input_.delete(0, 'end')
    input_.insert(0, '0')


def need_to_clear():
    global is_operation, is_result

    if input_.get().startswith('0') and len(input_.get()) == 1:
        clear_input()
    if is_result:
        clear_input()
        is_result = False
    if is_operation:
        clear_input()
        is_operation = False


def click_num_button(num):
    global last_button

    if len(input_.get()) <= MAX_NUM:
        if last_button is not None:
            change_button_color(last_button)

        need_to_clear()
        input_.insert('end', num)


def click_comma_button():
    if '.' not in input_.get():
        input_.insert('end', '.')


def click_operation_btn(btn_text, button):
    global num1, operator, is_operation

    change_button_color(button)

    operator = btn_text
    num1 = input_.get()
    is_operation = True


def click_pls_min_btn():
    if '-' in input_.get():
        input_.delete(0)
    else:
        input_.insert(0, '-')


def click_percent_btn():
    global num1, operator, is_operation

    num1 = input_.get()
    operator = '%'
    is_operation = True


def change_button_color(button):
    global last_button, last_button_bg, last_button_fg

    # Restore the color of the last pressed button
    if last_button is not None:
        last_button.config(background=last_button_bg, foreground=last_button_fg)
        last_button = None
    else:
        last_button = button
        last_button_bg = button.cget('background')
        last_button_fg = button.cget('foreground')

        button.config(background=last_button_fg, foreground=last_button_bg)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x550")
window.resizable(False, False)
window.config(background='black')

font_for_buttons = font.Font(family='Arial', size=20, weight='normal', slant='roman')
font_for_buttons2 = font.Font(family='Arial', size=20, weight='bold', slant='roman')
font_for_input = font.Font(family='Arial', size=30, weight='bold', slant='roman')

for c in range(4):
    window.columnconfigure(index=c, weight=1)
for r in range(7):
    window.rowconfigure(index=r, weight=1)

input_ = tk.Entry(window, width=105, font=font_for_input, justify='right', background='black', foreground='white')
input_.insert(0, '0')
input_.grid(row=0, column=0, rowspan=2, columnspan=4, ipady=50, padx=7, pady=7)

button_clear = tk.Button(window, text='c', font=font_for_buttons, background='grey100', command=click_clear_button)
button_clear.grid(row=2, column=0, ipadx=20, ipady=20, padx=7, pady=7)

button_pl_mns = tk.Button(window, text='+/-', font=font_for_buttons, background='grey100', command=click_pls_min_btn)
button_pl_mns.grid(row=2, column=1, ipadx=20, ipady=20, padx=7, pady=7)

button_percents = tk.Button(window, text='%', font=font_for_buttons, background='grey100',
                            command=lambda: click_percent_btn())
button_percents.grid(row=2, column=2, ipadx=20, ipady=20, padx=7, pady=7)

button_div = tk.Button(window, text='÷', font=font_for_buttons, background='gold3', foreground="white",
                       command=lambda: click_operation_btn('÷', button_div))
button_div.grid(row=2, column=3, ipadx=20, ipady=20, padx=7, pady=7)

button_7 = tk.Button(window, text='7', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('7'))
button_7.grid(row=3, column=0, ipadx=20, ipady=20, padx=7, pady=7)

button_8 = tk.Button(window, text='8', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('8'))
button_8.grid(row=3, column=1, ipadx=20, ipady=20, padx=7, pady=7)

button_9 = tk.Button(window, text='9', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('9'))
button_9.grid(row=3, column=2, ipadx=20, ipady=20, padx=7, pady=7)

button_mult = tk.Button(window, text='x', font=font_for_buttons, background='gold3', foreground="white",
                        command=lambda: click_operation_btn('x', button_mult))
button_mult.grid(row=3, column=3, ipadx=20, ipady=20, padx=7, pady=7)

button_4 = tk.Button(window, text='4', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('4'))
button_4.grid(row=4, column=0, ipadx=20, ipady=20, padx=7, pady=7)

button_5 = tk.Button(window, text='5', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('5'))
button_5.grid(row=4, column=1, ipadx=20, ipady=20, padx=7, pady=7)

button_6 = tk.Button(window, text='6', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('6'))
button_6.grid(row=4, column=2, ipadx=20, ipady=20, padx=7, pady=7)

button_minus = tk.Button(window, text='-', font=font_for_buttons, background='gold3', foreground="white",
                         command=lambda: click_operation_btn('-', button_minus))
button_minus.grid(row=4, column=3, ipadx=20, ipady=20, padx=7, pady=7)

button_1 = tk.Button(window, text='1', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('1'))
button_1.grid(row=5, column=0, ipadx=20, ipady=20, padx=7, pady=7)

button_2 = tk.Button(window, text='2', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('2'))
button_2.grid(row=5, column=1, ipadx=20, ipady=20, padx=7, pady=7)

button_3 = tk.Button(window, text='3', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('3'))
button_3.grid(row=5, column=2, ipadx=20, ipady=20, padx=7, pady=7)

button_plus = tk.Button(window, text='+', font=font_for_buttons, background='gold3', foreground="white",
                        command=lambda: click_operation_btn('+', button_plus))
button_plus.grid(row=5, column=3, ipadx=20, ipady=20, padx=7, pady=7)

button_0 = tk.Button(window, text='0', font=font_for_buttons2, background='DarkGray', foreground="white",
                     command=lambda: click_num_button('0'))
button_0.grid(row=6, column=0, columnspan=2, ipadx=65, ipady=20, padx=7, pady=7)

button_comma = tk.Button(window, text=',', font=font_for_buttons2, background='DarkGray', foreground="white",
                         command=lambda: click_comma_button())
button_comma.grid(row=6, column=2, ipadx=20, ipady=20, padx=7, pady=7)

button_result = tk.Button(window, text='=', font=font_for_buttons, background='gold3', foreground="white",
                          command=lambda: get_result())
button_result.grid(row=6, column=3, ipadx=20, ipady=20, padx=7, pady=7)

window.mainloop()
