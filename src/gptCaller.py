import openai
from config import OPENAI_API_KEY

class GPTAPICaller:
    def __init__(self, api_key, model="text-davinci-002"):
        # Initialize the OpenAI API client with your API key and the model you want to use
        openai.api_key = api_key
        self.model = model

    def generate_text(self, text):
        try:
            # Call the OpenAI API to generate text based on the provided prompt
            response = openai.Completion.create(
                engine=self.model,
                prompt=text,
                max_tokens=100,  # You can adjust the number of tokens based on your needs
            )

            # Extract and return the generated text from the API response
            return response.choices[0].text.strip()

        except Exception as e:
            print("Error calling the GPT API:", e)
            return None
    
    def generate_Integrated_text(self, text_first, text_second):
        try:
                # Example text prompt
            prompt = f"""Hi you are here for summarizing and anlayzing texts I'll give you.
            the sentence starts from ::: is the text what I want you to work. there is two kind of text. 
            
            this is the fist text which is grammerly correct ::: {text_first} 
            this is the second text which is grammerly incorrect. so you need to make it clear. ::: {text_second}
            
            this is command.
            
            STEP 1 : The first or second one could be empty In this case you just return "No Content" 
            If there is at least one kind of text, try to find below infomation from the sentences.
            
            this is korean. So I'll give you the korean word category that I ask you to find.
            ["신청기간", "지원자격", "지원혜택", "전반적인 장학금 요약"]
            
            
            STEP 2 :So In case there is some text infomation, 
            please return following Json type Including above category(by korean word)
            """
            
            integrated_text = self.generate_text(prompt)
            return integrated_text
        
        except Exception as e:
            print("Error calling the GPT API:", e)
            return None
        
        
if __name__ == "__main__":
    text_info = """
        '텍스트 크롤링 불가, 첨부파일 참고',
    """
    image_text = """'\n' +
      '사 량 의 열 매 44\n' +
      '자 의 비 지 공 등 모 렴 마\n' +
      '2023 시 설 보 호 여\n' +
      '성 청 소 년 자 립 지 원 사 업\n' +
      "94846 @ 멘 토 링 ' 여 성 대 학 생 멘 토 모 집\n" +
      '이 사 업\n' +
      '의 기 금 으 로 지 원 됩 니 다 .\n' +
      '모 집 기 간 | 2023 년 7 월 5 일 ( 수 ) ~ 7 윌 23 일 ( 일 )\n' +
      '모 집 대상 ㅣ 전 국 소 재 대 학 에 재 ( 휴 ) 학 중 인 여 성 대 학 생\n' +
      '활 동 내 용 ㅣ 시 설 보 호 여 성 청 소 년 대상 학 습 / 진 로 지도 및\n' +
      '정 서 지 원 활 동 8 신 체 활 동 지 원\n' +
      '주 6 시 간 시 설 방 문 멘 토 링 진 행\n' +
      '대 학 생 - 청 소 년 、 ( 여 성 대 학 생 멘 토 1{ 여 성 청 소 년 2 매 칭 )\n' +
      '멘 토 링 ㅇ 학 습 / 진 로 지도 및 정 서 지 원 활 동 (4 시 간 )\n' +
      'ㅇ 여 성 청 소 년 맞 춤형 신 체 활 동 (2 시 간 )\n' +
      '0 문 화 활 동 , 진 로 탐 색 활 동 등 여 성 청 소 년 멘 티 와 함 께 참 여 ( 연 간 )\n' +
      '* 멘 토 링 활 동 은 여 성 대 학 생 멘 토 가 아 동 복 지 시 설 에 방 문 하 여 오 프 라 인 으 로 진 행 됩 니 다 .\n' +
      '# 여 성 대 학 생 멘 토 대 상 으 로 신 체 활 동 멘 토 링 을 위 한 사 전 교 육 이 진 행 됩 니 다 .\n' +
      '활 동 기 간 | 2023 년 8 월 ~ 2024 년 2 월 ( 총 7 개 월 )\n' +
      '활 동 혜 택 ㅣ ㆍ 학 업 생 활 장 려 장 학 금 연 간 300 만 원 제 공\n' +
      '사 회 인 멘 토 링 ( 취 업 , 진 로 , 라 이프 멘 토 링 제 공 )\n' +
      '대 학 생 교 육 봉 사 자 네 트 워 크 교 류 기회 제 공\n' +
      '신 청 방 법 ㅣ 온 라 인 서 류 접 수 (0007@0(009.0.9)\n' +
      '문 . 의 | 0484 멘 토 링 운 영 사 무 국\n' +
      '3 메 일 .11080006040009. 아 9\n' +
      '@ 전 화 .02-2088-1448.',
    """
    # Initialize the GPT API caller with your API key
    openai_api_key = OPENAI_API_KEY
    gpt_caller = GPTAPICaller(openai_api_key)
    # Call the GPT API to generate text based on the prompt
    generated_text = gpt_caller.generate_Integrated_text(text_info, image_text)
    print("api call is done")
    print()
    print(generated_text)