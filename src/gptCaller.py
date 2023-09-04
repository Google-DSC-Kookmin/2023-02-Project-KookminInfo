import openai

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
