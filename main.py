from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Miles to Kilometer Converter & Vice Versa")
window.config(padx=30, pady=18)

# Função para realizar a conversão
def convert():
    value_str = value_entry.get().replace(',', '.')  # Substitui vírgula por ponto
    value = float(value_str)
    if operation_var.get() == "to_km":
        result = round(value * 1.609, 2)
    else:  # operation_var.get() == "to_mi"
        result = round(value / 1.609, 2)
    result_label.config(text=str(result))

# Criando widgets
operation_var = StringVar(window)
operation_var.set("to_km")  # default value
operation_combobox = Combobox(window, values=["to_km", "to_mi"], state="readonly", textvariable=operation_var)
operation_combobox.current(0)  # Set default value
operation_combobox.grid(row=0, column=0, padx=10, pady=5)

value_entry = Entry(window, width=10)
value_entry.grid(row=0, column=1, padx=10, pady=5)

result_label = Label(window, text="Result:")
result_label.grid(row=0, column=2, padx=10, pady=5)

# Configurando o botão para converter
convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=0, column=3, padx=10, pady=5)

window.mainloop()
