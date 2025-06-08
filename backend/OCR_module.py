import pytesseract as ptsc
import cv2
from PIL import Image

ptsc.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
file = Image.open("photo.png")

data = ptsc.image_to_data