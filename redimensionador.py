import os
from tkinter import Tk, Label, Button, filedialog, Entry, StringVar, ttk, IntVar
from PIL import Image, ImageTk


class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Redimensionador de Imagens")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Variáveis
        self.image_path = StringVar()
        self.width = StringVar()
        self.height = StringVar()
        self.keep_aspect_ratio = IntVar(value=1)  # 1 = Manter proporção

        # Título
        Label(root, text="Redimensionador de Imagens", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Seleção da imagem
        Label(root, text="Selecione uma imagem:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        frame = ttk.Frame(root)
        frame.pack(pady=5)
        self.path_entry = ttk.Entry(frame, textvariable=self.image_path, width=40, state="readonly")
        self.path_entry.grid(row=0, column=0, padx=5)
        ttk.Button(frame, text="Procurar", command=self.select_image).grid(row=0, column=1)

        # Dimensões
        Label(root, text="Dimensões (pixels):", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        dims_frame = ttk.Frame(root)
        dims_frame.pack(pady=5)
        Label(dims_frame, text="Largura:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.width_entry = ttk.Entry(dims_frame, textvariable=self.width, width=10)
        self.width_entry.grid(row=0, column=1, padx=5)

        Label(dims_frame, text="Altura:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=2, padx=5)
        self.height_entry = ttk.Entry(dims_frame, textvariable=self.height, width=10)
        self.height_entry.grid(row=0, column=3, padx=5)

        # Checkbox para manter proporção
        ttk.Checkbutton(root, text="Manter proporção", variable=self.keep_aspect_ratio).pack(pady=5)

        # Botão de redimensionar e salvar
        ttk.Button(root, text="Redimensionar e Salvar", command=self.resize_image).pack(pady=20)

        # Área para mensagens
        self.message_label = Label(root, text="", font=("Arial", 10), bg="#f0f0f0", fg="green")
        self.message_label.pack(pady=10)

    def select_image(self):
        """Abre uma caixa de diálogo para selecionar a imagem."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_path:
            # Define o caminho e exibe apenas o nome do arquivo
            self.image_path.set(os.path.basename(file_path))
            self.full_image_path = file_path

            # Atualiza largura e altura com base na imagem selecionada
            img = Image.open(file_path)
            self.width.set(img.width)
            self.height.set(img.height)

    def resize_image(self):
        """Redimensiona e salva a imagem."""
        try:
            if not hasattr(self, "full_image_path"):
                raise ValueError("Nenhuma imagem foi selecionada.")

            original_img = Image.open(self.full_image_path)
            original_width, original_height = original_img.size

            # Obtém largura e altura desejadas
            new_width = int(self.width.get())
            new_height = int(self.height.get())

            # Mantém proporção, se habilitado
            if self.keep_aspect_ratio.get():
                aspect_ratio = original_width / original_height
                if new_width != original_width:
                    new_height = int(new_width / aspect_ratio)
                    self.height.set(new_height)
                elif new_height != original_height:
                    new_width = int(new_height * aspect_ratio)
                    self.width.set(new_width)

            # Redimensiona e salva a imagem
            resized_img = original_img.resize((new_width, new_height), Image.LANCZOS)
            save_path = filedialog.asksaveasfilename(
                initialfile="imagem-redimensionada",
                defaultextension=".png",
                filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("Todos os arquivos", "*.*")]
            )
            if save_path:
                resized_img.save(save_path)
                self.message_label.config(text="Imagem salva com sucesso!", fg="green")
        except Exception as e:
            self.message_label.config(text=f"Erro: {str(e)}", fg="red")


if __name__ == "__main__":
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()
