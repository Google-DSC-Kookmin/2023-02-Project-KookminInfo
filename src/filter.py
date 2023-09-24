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
    
    # 수정 필요한 부분 -> open ai api 로 처리하면 한번엔 되는데, 비용 문제 등으로 전처리를 할 필요가 있음. 
    # 전처리 키워드를 찾고, 그 인근 데이터를 모으는 식으로 해야 할듯함.
    @staticmethod
    def filter_incorrect_text(text):
        target_word_list = ["조건", "자격", "기준", "기간", "일정", "혜택"]
        checked_dict = dict()
        text_list = text.split("\n")
        for text_splitted in text_list:
            for target in target_word_list:
                if target in text_splitted:
                    checked_dict[target] = text_splitted
        return checked_dict
    
    
    @staticmethod
    def filter_priority_fulfill(correct_text, incorrect_text):
        # 고안 방법 -> 1번 correct text 에서 필요한 데이터를 모두 뽑을 수 있으면 충분.
        # 1번 데이터에서 필요한 데이터 칼럼(신청기한, 혜택, 신청조건)을 모두 찾을 수 없다면 2번 데이터까지 서칭.
        if correct_text is not None:
            return correct_text
        elif incorrect_text is not None:
            return incorrect_text
        return "No data from the URL"


if __name__ == "__main__":
    file_name_path = "data/"
    data_list = []  # Initialize a dictionary to store the data
    current_key = None  # Initialize the current key

    for i in range(20):
        data = dict()
        with open(f"{file_name_path}post_{i}.txt", 'r', encoding='utf-8') as file:
            # Read the lines from the file and process them
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if ':' in line:
                    splitted = line.split(': ', 1)
                    key = splitted[0]
                    value = ""
                    if len(splitted) > 1:
                        value = splitted[1]
                    data[key] = value
                    current_key = key
                elif current_key:
                    # If no ":", associate the line with the previous key
                    data[current_key] += " " + line
        data_list.append(data)
    # Print the processed data
    
    for dt_dict in data_list:
        correct_text = dt_dict.get("Image Text:", "")  # Use "Image Text" as correct_text
        incorrect_text = dt_dict.get("Text Info:", "")  # Use "Text Info" as incorrect_text
        data = Filter.filter_priority_fulfill(correct_text, incorrect_text)

        print("Text preprocessing result : ")
        print(data)
        print("crawl done")
        print()

