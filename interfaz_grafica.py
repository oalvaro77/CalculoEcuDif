import tkinter as tk
from tkinter import ttk, messagebox
from analizador_ecuaciones import analizar_ecuacion

class AnalizadorEcuacionesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Ecuaciones Diferenciales")
        self.root.geometry("600x400")
        
        # Configurar el estilo
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))
        
        # Crear el marco principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="Analizador de Ecuaciones Diferenciales", 
                          font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Etiqueta y campo de entrada
        ttk.Label(main_frame, text="Ingrese la ecuación diferencial:").grid(row=1, column=0, sticky=tk.W)
        self.ecuacion_var = tk.StringVar()
        self.entrada_ecuacion = ttk.Entry(main_frame, textvariable=self.ecuacion_var, width=50)
        self.entrada_ecuacion.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón de análisis
        ttk.Button(main_frame, text="Analizar", command=self.analizar).grid(row=2, column=0, columnspan=2, pady=20)
        
        # Frame para resultados
        self.frame_resultados = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        self.frame_resultados.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Etiquetas para resultados
        self.tipo_var = tk.StringVar()
        self.orden_var = tk.StringVar()
        self.linealidad_var = tk.StringVar()
        
        ttk.Label(self.frame_resultados, text="Tipo:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self.frame_resultados, textvariable=self.tipo_var).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(self.frame_resultados, text="Orden:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(self.frame_resultados, textvariable=self.orden_var).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(self.frame_resultados, text="Linealidad:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(self.frame_resultados, textvariable=self.linealidad_var).grid(row=2, column=1, sticky=tk.W)
        
        # Ejemplos
        frame_ejemplos = ttk.LabelFrame(main_frame, text="Ejemplos", padding="10")
        frame_ejemplos.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ejemplos = [
            "dy/dx + 2y = x",
            "∂y/∂x + ∂y/∂t = 0",
            "d²y/dx² + 3dy/dx + 2y = 0",
            "y'' + 2y' + y = 0"
        ]
        
        for i, ejemplo in enumerate(ejemplos):
            ttk.Button(frame_ejemplos, text=f"Ejemplo {i+1}", 
                      command=lambda e=ejemplo: self.ecuacion_var.set(e)).grid(
                          row=i//2, column=i%2, padx=5, pady=5)
    
    def analizar(self):
        ecuacion = self.ecuacion_var.get().strip()
        if not ecuacion:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una ecuación.")
            return
            
        try:
            resultado = analizar_ecuacion(ecuacion)
            self.tipo_var.set(resultado['tipo'])
            self.orden_var.set(str(resultado['orden']))
            self.linealidad_var.set(resultado['linealidad'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al analizar la ecuación: {str(e)}")

def main():
    root = tk.Tk()
    app = AnalizadorEcuacionesGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 