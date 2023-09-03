class Filter:
    @staticmethod
    def filter_text(text):
        # Preprocess the text obtained from a URL
        # 1. Replace consecutive newline characters with a single newline
        text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())
        
        # 2. Check if the text consists only of newline or tab characters and no Korean characters
        if not any(char.isalpha() or char.isspace() for char in text):
            return "텍스트 크롤링 불가, 첨부파일 참고"  # Return this message if text is not suitable for crawling
        
        return text
    
