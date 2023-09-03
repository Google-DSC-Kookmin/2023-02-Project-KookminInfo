import requests
from PIL import Image
import pytesseract

class Reader:
    @staticmethod
    def read_text_from_image_url(image_url):
        # Open the image from the URL
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            image = Image.open(response.raw)

            # OCR for Korean text only
            # 영어를 원한다면 'kor+eng' 옵션으로 변경가능. 
            text = pytesseract.image_to_string(image, lang='kor')
            
            return text
        else:
            return None  # Return None in case of image retrieval failure
