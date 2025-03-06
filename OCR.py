import sys 
import pytesseract # type: ignore
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QLineEdit # type: ignore
from PyQt6.QtGui import QFont, QPixmap # type: ignore
from PyQt6.QtCore import QPropertyAnimation, QRect, Qt # type: ignore
from googletrans import Translator # type: ignore
from PIL import Image # type: ignore
import os

#Wygląd przycisku
class Btn(QPushButton):
  def __init__(self, text):
    super().__init__(text)
    self.setStyleSheet("""
      QPushButton{
        background-color: #87e8e8;
        color: #000000;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px
      }
      QPushButton::hover{
        background-color: #000000;
        color: #ffffff;
      }"""
    )


class OCR_translator(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Tłumaczenie OCR")
    self.setGeometry(100,100,700,500)

    self.translator = Translator()
    self.app_UI()

  def app_UI(self):
    layout = QVBoxLayout()

    self.label = QLabel("Wybierz obraz do OCR")
    self.label.setFont(QFont("Arial", 14))
    layout.addWidget(self.label)

    #Przycisk otwierania obrazu
    self.btn_open = Btn("Otwórz obraz")
    self.btn_open.clicked.connect(self.open_image)
    layout.addWidget(self.btn_open)
    
    #Miejsce do odczytu tłumaczenia
    self.text_output = QTextEdit()
    self.text_output.setReadOnly(True)
    layout.addWidget(self.text_output)
    
    #Podanie nazwy do zapisu pliku 
    self.filename_input = QLineEdit()
    self.filename_input.setPlaceholderText("Podaj nazwę")
    layout.addWidget(self.filename_input)

    #Przycisk zapisu
    self.save_btn = Btn("Zapisz wynik tłumaczenia")
    self.save_btn.clicked.connect(self.save_result)
    layout.addWidget(self.save_btn)

    self.setLayout(layout)
  
  def open_image(self):
    path, _ = QFileDialog.getOpenFileName(self, "Wybierz obraz", "", "Images (*.jpg, *.png, *.jpeg) ")
    if path:  
      self.label.setText(f"Wybrany plik: {path}")
      self.image_processing(path)

  def image_processing(self, path):
    ocr_text = pytesseract.image_to_string(Image.open(path), lang = 'jpn')
    translated_text = self.translator.translate(ocr_text,src = 'ja', dest = 'pl').text
    self.text_output.setText(f"Rozpoznany tekst:\n{ocr_text}\n\nTłumaczenie:\n{translated_text}")

  def save_result(self):
    filename = self.file_name_input.text().strip()

    if not filename:
      self.label.setText("Podaj nazwę pliku przed zapisaniem")
      return
    
    dir_path = QFileDialog.getExistingDirectory(self,"Wybierz folder do zapisu")
    if not dir_path:
      return
    
    path = os.path.join(dir_path, f"{filename}.txt")
    with open (path, 'w', encoding = 'utf-8') as file:
      file.write(self.text_output.toPlainText())

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = OCR_translator()
  window.show()
  sys.exit(app.exec())


