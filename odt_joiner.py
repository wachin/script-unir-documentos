import tkinter as tk
from tkinter import filedialog
import subprocess
import os

TEMP_DIR = "temp"

def convert_documents(input_files, output_file):
    try:
        # Crear el directorio temporal si no existe
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

        # Convertir los archivos de entrada a ODT
        temp_files = [os.path.join(TEMP_DIR, os.path.splitext(os.path.basename(f))[0] + ".odt") for f in input_files]
        subprocess.run(["soffice", "--headless", "--convert-to", "odt", "--outdir", TEMP_DIR] + input_files, check=True)

        # Combinar los archivos ODT en el archivo de salida
        subprocess.run(["soffice", "--headless", "--convert-to", "odt", output_file] + temp_files, check=True)

        # Eliminar los archivos temporales
        for f in temp_files:
            os.remove(f)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error al unir los archivos: {e}")

class ODTMerger:
    def __init__(self, master):
        self.master = master
        master.title("ODT Merger")

        # Crear widgets de la interfaz
        self.label_select_files = tk.Label(master, text="Selecciona los archivos .odt a unir:")
        self.label_select_files.pack()

        self.listbox_files = tk.Listbox(master, width=50, selectmode=tk.EXTENDED)
        self.listbox_files.pack()

        self.button_add_files = tk.Button(master, text="Agregar archivos", command=self.add_files)
        self.button_add_files.pack()

        self.button_select_all = tk.Button(master, text="Seleccionar todos", command=self.select_all)
        self.button_select_all.pack()

        self.button_merge = tk.Button(master, text="Unir archivos", command=self.merge_files)
        self.button_merge.pack()

        self.label_output_file = tk.Label(master, text="Nombre del archivo de salida:")
        self.label_output_file.pack()

        self.entry_output_file = tk.Entry(master)
        self.entry_output_file.pack()

    def add_files(self):
        filetypes = [("Archivos ODT", "*.odt")]
        filenames = filedialog.askopenfilenames(filetypes=filetypes)
        for filename in filenames:
            self.listbox_files.insert(tk.END, os.path.basename(filename))

    def select_all(self):
        self.listbox_files.selection_set(0, tk.END)

    def merge_files(self):
        selected_indices = self.listbox_files.curselection()
        input_files = [self.listbox_files.get(i) for i in selected_indices]
        output_file = self.entry_output_file.get()

        if not input_files or not output_file:
            tk.messagebox.showerror("Error", "Debes seleccionar los archivos a unir y proporcionar un nombre de archivo de salida.")
            return

        try:
            convert_documents(input_files, output_file)
            tk.messagebox.showinfo("Éxito", "Los archivos se han unido correctamente.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Ocurrió un error al unir los archivos: {e}")

root = tk.Tk()
app = ODTMerger(root)
root.mainloop()
