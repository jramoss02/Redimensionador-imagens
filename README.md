# Redimensionador de Imagens com Interface Gráfica

Este é um aplicativo para redimensionar imagens de forma prática, preservando a qualidade e com uma interface amigável e moderna. Desenvolvido em Python com **Tkinter**, o programa permite selecionar uma imagem, definir novas dimensões, manter a proporção (opcional) e salvar a imagem redimensionada com um nome padrão.

---

## 🖼️ Funcionalidades

- **Seleção de imagem**: Suporte para os formatos PNG, JPG, JPEG, BMP e GIF.
- **Exibição do nome da imagem**: Apenas o nome do arquivo selecionado é exibido na interface.
- **Entrada de dimensões**: Defina manualmente a largura e altura desejadas.
- **Manter proporção**: Opção de travar a proporção original da imagem.
- **Salvar com nome padrão**: O arquivo redimensionado é salvo com o nome padrão `imagem-redimensionada`, mas o nome pode ser alterado pelo usuário.
- **Interface moderna**: Uso de widgets do **ttk** para uma aparência mais amigável.

---

## 🛠️ Tecnologias utilizadas

- **Python**: Linguagem principal do projeto.
- **Tkinter**: Para a interface gráfica.
- **Pillow (PIL)**: Para manipulação de imagens.

---

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina (versão 3.7 ou superior). Além disso, instale a biblioteca Pillow para manipulação de imagens:

```bash
pip install pillow
```

---

## 🚀 Como executar o projeto

1. Clone este repositório ou baixe os arquivos.
2. Navegue até o diretório do projeto no terminal.
3. Execute o script principal:
   ```bash
   python redimensionador.py
   ```
4. Utilize o aplicativo:
   - Clique em **Procurar** para selecionar uma imagem.
   - Insira as dimensões (largura e altura) desejadas.
   - (Opcional) Marque a opção **Manter proporção** para ajustar automaticamente as dimensões enquanto mantém a proporção original.
   - Clique em **Redimensionar e Salvar** para salvar a imagem redimensionada.

---

## 📂 Estrutura do projeto

```
📂 Redimensionador
├── redimensionador.py   # Código principal do aplicativo
├── README.md            # Documentação do projeto
```

---

## 🔧 Como funciona

1. **Selecionar a imagem**:
   - Apenas o nome do arquivo será exibido no campo correspondente.
   - A largura e altura da imagem original serão automaticamente carregadas nos campos de dimensões.

2. **Definir dimensões**:
   - Digite a largura e altura desejadas.
   - Caso a opção **Manter proporção** esteja marcada, os valores serão ajustados automaticamente com base na proporção original da imagem.

3. **Salvar imagem**:
   - Clique no botão **Redimensionar e Salvar**.
   - Um diálogo de salvar será aberto com o nome padrão `imagem-redimensionada`. O formato padrão será PNG, mas você pode alterá-lo.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se deseja melhorar este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para suas alterações: `git checkout -b minha-melhoria`.
3. Commit suas alterações: `git commit -m "Melhoria: descrição da melhoria"`.
4. Envie para o branch principal: `git push origin minha-melhoria`.
5. Abra um Pull Request.

---

## 🛡️ Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo conforme necessário.

---

## 📞 Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **E-mail**: [02.jrsramos@gmail.com] 
- **GitHub**: [https://github.com/jramoss02]
- **LinkedIn**: [José Ramos](https://linkedin.com/in/josé-roberto-ramos)

😊 Obrigado por usar este projeto!
