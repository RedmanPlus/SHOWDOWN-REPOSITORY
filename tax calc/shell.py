import tkinter as tk
import clipboard
from main import transcribe
from dict import rubles, pennies


def calculate(amount, tax, premium):
    no_tax_amount = int(amount) - int(amount) * (int(tax) / 100)
    tax_amount = int(amount) * (int(tax) / 100)
    ent_result_one.delete(0, 100)
    ent_result_one.insert(0, str(round(no_tax_amount, 2)))
    ent_result_two.delete(0, 100)
    ent_result_two.insert(0, str(round(tax_amount, 2)))

    premium_amount = int(amount) * (int(premium) / 100)
    premium_tax_amount = premium_amount * (int(tax) / 100)
    ent_result_three.delete(0, 100)
    ent_result_three.insert(0, str(round(premium_amount, 2)))
    ent_result_four.delete(0, 100)
    ent_result_four.insert(0, str(round(premium_tax_amount, 2)))

    after_premium = int(amount) - premium_amount
    after_premium_tax = after_premium * (int(tax) / 100)
    ent_result_five.delete(0, 100)
    ent_result_five.insert(0, str(round(after_premium, 2)))
    ent_result_six.delete(0, 100)
    ent_result_six.insert(0, str(round(after_premium_tax, 2)))


def translate(number):
    a = number.split('.')
    if len(a[1]) < 2:
        a[1] = a[1] + '0'
    number = '.'.join(a)
    result_text = transcribe(a[0])
    clipboard.copy(f'{number} р. ({result_text}{rubles[a[0][-1]]}, {a[1]} {pennies[a[1][-1]]})')


# Displayed block

root = tk.Tk()
root.title('НДС')

# Entry block

lbl_enter = tk.Label(master=root, text='Введите сумму договора', font='Arial 9')
ent_summ = tk.Entry(master=root, width=22)
lbl_tax = tk.Label(master=root, text='Введите ставку НДС', font='Arial 9')
ent_tax = tk.Entry(master=root, width=5)
ent_tax.insert(0, '18')
lbl_per_one = tk.Label(master=root, text='%', font='Arial 9')
lbl_premium = tk.Label(master=root, text='Введите сумму предоплаты', font='Arial 9')
ent_premium = tk.Entry(master=root, width=5)
ent_premium.insert(0, '30')
lbl_per_two = tk.Label(master=root, text='%', font='Arial 9')

lbl_enter.grid(row=0, column=0, sticky='e', padx=5, pady=3)
ent_summ.grid(row=0, column=1, columnspan=4, padx=5, pady=3)
lbl_tax.grid(row=1, column=0, sticky='e', padx=5, pady=3)
ent_tax.grid(row=1, column=1, sticky='w', padx=5)
lbl_per_one.grid(row=1, column=2, sticky='w')
lbl_premium.grid(row=2, column=0, sticky='e', padx=5, pady=3)
ent_premium.grid(row=2, column=1, sticky='w', padx=5, pady=3)
lbl_per_two.grid(row=2, column=2, sticky='w')

frm_format = tk.Frame(master=root)
frm_format.grid(row=3, column=0, padx=5, pady=15)

# result block

frm_result = tk.Frame(master=root)
frm_result.grid(row=4, column=0, columnspan=4)

lbl_summ_result_one = tk.Label(master=frm_result, text='Сумма без НДС', font='Arial 9')
lbl_summ_result_two = tk.Label(master=frm_result, text='НДС в том числе', font='Arial 9')
lbl_summ_result_one.grid(row=0, column=0)
lbl_summ_result_two.grid(row=0, column=1)

ent_result_one = tk.Entry(master=frm_result, width=20)
ent_result_two = tk.Entry(master=frm_result, width=20)
ent_result_one.grid(row=1, column=0, padx=14, pady=4)
ent_result_two.grid(row=1, column=1, padx=14, pady=4)

btn_copy_ro = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_one.get()))
btn_copy_rt = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_two.get()))
btn_copy_ro.grid(row=2, column=0, sticky='e', padx=12)
btn_copy_rt.grid(row=2, column=1, sticky='e', padx=12)

lbl_summ_result_three = tk.Label(master=frm_result, text='Сумма предоплаты', font='Arial 7')
lbl_summ_result_four = tk.Label(master=frm_result, text='в том числе НДС', font='Arial 7')
lbl_summ_result_three.grid(row=3, column=0)
lbl_summ_result_four.grid(row=3, column=1)

ent_result_three = tk.Entry(master=frm_result, width=20)
ent_result_four = tk.Entry(master=frm_result, width=20)
ent_result_three.grid(row=4, column=0, padx=14)
ent_result_four.grid(row=4, column=1, padx=14)

btn_copy_rth = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_three.get()))
btn_copy_rf = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_four.get()))
btn_copy_rth.grid(row=5, column=0, sticky='e', padx=12)
btn_copy_rf.grid(row=5, column=1, sticky='e', padx=12)

lbl_summ_result_five = tk.Label(master=frm_result, text='Последующая оплата', font='Arial 7')
lbl_summ_result_six = tk.Label(master=frm_result, text='в том числе НДС', font='Arial 7')
lbl_summ_result_five.grid(row=6, column=0)
lbl_summ_result_six.grid(row=6, column=1)

ent_result_five = tk.Entry(master=frm_result, width=20)
ent_result_six = tk.Entry(master=frm_result, width=20)
ent_result_five.grid(row=7, column=0, padx=14)
ent_result_six.grid(row=7, column=1, padx=14)

btn_copy_rfi = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_five.get()))
btn_copy_rs = tk.Button(master=frm_result, text='прописью', font='Arial 7', fg='Steel blue', borderwidth=0,
                        command=lambda: translate(ent_result_six.get()))
btn_copy_rfi.grid(row=8, column=0, sticky='e', padx=12)
btn_copy_rs.grid(row=8, column=1, sticky='e', padx=12)

btn_calculate = tk.Button(master=frm_result, text='Выделить НДС', command=lambda: calculate(ent_summ.get(),
                                                                                            ent_tax.get(),
                                                                                            ent_premium.get()))
btn_exit = tk.Button(master=frm_result, text='ВЫХОД', command=quit)
btn_calculate.grid(row=9, column=0, padx=10, pady=7)
btn_exit.grid(row=9, column=1, padx=10, pady=7)

root.mainloop()