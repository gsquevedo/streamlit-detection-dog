# 🐶 App de Detecção de Cachorros

**Aplicativo web em Streamlit para detectar cachorros em imagens usando um modelo de deep learning.**

---

## 📝 Descrição

Este projeto é um aplicativo web simples construído com **Streamlit** que permite aos usuários enviar imagens e detectar cachorros nelas usando um modelo de deep learning pré-treinado. É ideal para quem deseja aprender sobre **visão computacional**, **classificação de imagens** e **desenvolvimento de aplicações web**.

---

## 🚀 Funcionalidades

- Envio de imagens para detectar cachorros.
- Predições em tempo real utilizando um modelo pré-treinado.
- Interface amigável construída com **Streamlit**.

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/) ou [TensorFlow] (dependendo do modelo)
- [OpenCV](https://opencv.org/) (para processamento de imagens)
- [PIL / Pillow](https://pillow.readthedocs.io/)

---

## 📁 Estrutura do Projeto

streamlit-detection-dog/
│
├── app.py # Aplicativo principal em Streamlit
├── model.py # Carregamento e predição do modelo pré-treinado
├── requirements.txt # Dependências Python
├── assets/ # Imagens ou ícones de exemplo
└── README.md # Documentação do projeto

## 💻 Como Rodar

1. Clone o repositório:
  ```bash
  git clone https://github.com/gsquevedo/streamlit-detection-dog.git
  cd streamlit-detection-dog

2. Instale as dependências:
  ```bash
  pip install -r requirements.txt

3. Execute o aplicativo:
  ```bash
  streamlit run app.py
