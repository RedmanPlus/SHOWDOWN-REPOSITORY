import tkinter as tk
import random

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
signs = ['/', '?', ';', ':', '|', '*', '-', '+', '$', '%', '#', '&']
mainlist = [nums, letters, signs]

password = "Тут будет готовый пароль"


def randomize():
    global password
    ent_result.delete(0, tk.END)
    len_of_pass = int(ent_len_password.get())
    check_nums = nums_state.get()
    check_letters = letters_state.get()
    check_signs = signs_state.get()
    res_pass = []
    for i in range(len_of_pass):
        if check_nums and check_letters and check_signs:
            which_one = mainlist[random.randint(0, 2)]
            res_pass.append(which_one[random.randint(0, len(which_one) - 1)])
        elif check_nums and check_letters:
            which_one = mainlist[random.randint(0, 1)]
            res_pass.append(which_one[random.randint(0, len(which_one) - 1)])
        elif check_letters and check_signs:
            which_one = mainlist[random.randint(1, 2)]
            res_pass.append(which_one[random.randint(0, len(which_one) - 1)])
        elif check_nums and check_signs:
            which_one = mainlist[random.randrange(0, 2, 2)]
            res_pass.append(which_one[random.randint(0, len(which_one) - 1)])
        elif check_nums:
            res_pass.append(mainlist[0][random.randint(0, len(mainlist[0]) - 1)])
        elif check_letters:
            res_pass.append(mainlist[1][random.randint(0, len(mainlist[1]) - 1)])
        elif check_signs:
            res_pass.append(mainlist[2][random.randint(0, len(mainlist[2]) - 1)])
    password = ''.join(res_pass)
    ent_result.insert(0, password)


root = tk.Tk()

frm_master = tk.Frame(master=root)
frm_master.grid(column=0, row=0)

lbl_test = tk.Label(master=frm_master, text='Генератор паролей v:1.0', font=('Calibri', 13))
lbl_test.grid(column=0, row=0, sticky="W", pady=10, padx=10)

frm_sup = tk.Frame(master=frm_master, pady=5, padx=5, relief=tk.RAISED, borderwidth=3)
frm_sup.grid(column=1, row=0, pady=5, padx=5)

ent_len_password = tk.Entry(master=frm_sup, width=2)
ent_len_password.grid(row=2, column=0, sticky="W", padx=5, pady=10)

lbl_info = tk.Label(master=frm_sup, text='Длинна пароля', font=('Calibri', 8))
lbl_info.grid(row=2, column=1, sticky="W")

frm_main = tk.Frame(master=root, pady=5, padx=5, relief=tk.RAISED, borderwidth=3)
frm_main.grid(column=0, row=2, pady=5, padx=5)

nums_state = tk.IntVar()
letters_state = tk.IntVar()
signs_state = tk.IntVar()

chk_nums = tk.Checkbutton(master=frm_main, text='Использовать \nв пароле цифры', font=('Calibri', 8),
                          variable=nums_state)
chk_letters = tk.Checkbutton(master=frm_main, text='Использовать \nв пароле буквы', font=('Calibri', 8),
                             variable=letters_state)
chk_signs = tk.Checkbutton(master=frm_main, text='Использовать в \nпароле прочие символы', font=('Calibri', 8),
                           variable=signs_state)

chk_nums.grid(row=3, column=0, sticky="W")
chk_letters.grid(row=4, column=0, sticky="W")
chk_signs.grid(row=5, column=0, sticky="W")

btn_generate = tk.Button(master=frm_main, text="Создаем пароль", command=randomize)
btn_generate.grid(row=6, column=0, pady=20, padx=20, sticky="W")

ent_result = tk.Entry(master=frm_main, width=20)
ent_result.grid(row=6, column=1, pady=20, padx=20, sticky="W")

root.mainloop()
