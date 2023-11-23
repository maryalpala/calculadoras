import tkinter as tk

class Calculadora:
    def _init_(self, root):
        self.root = root
        root.title("Calculadora")
        
        # Pantalla
        self.pantalla = tk.Entry(root, width=16, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
        self.pantalla.grid(row=0, column=0, columnspan=4)
        
        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for boton_text in botones:
            tk.Button(root, text=boton_text, width=4, height=2, command=lambda text=boton_text: self.click_boton(text)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Botón de limpiar
        tk.Button(root, text='C', width=4, height=2, command=self.limpiar_pantalla).grid(row=row_val, column=col_val)

    def click_boton(self, texto):
        if texto == '=':
            try:
                resultado = eval(self.pantalla.get())
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, 'Error')
        else:
            self.pantalla.insert(tk.END, texto)

    def limpiar_pantalla(self):
        self.pantalla.delete(0, tk.END)


if __name__ == "_main_":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()