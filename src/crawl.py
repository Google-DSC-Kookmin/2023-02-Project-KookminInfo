import requests
from bs4 import BeautifulSoup
from filter import Filter
from reader import Reader
import pymongo
from gptCaller import GPTAPICaller
from config import OPENAI_API_KEY


def scrape_kookmin_news(url):
    # Send a GET request to the URL and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all post elements on the page
    posts = soup.find('div', class_='board_list').find_all('li')

    post_info = []

    for post in posts:
        # Extract title and link for each post
        title = post.find('p', class_='title').text
        link = 'https://www.kookmin.ac.kr' + post.find('a')['href']

        # Send a GET request to the post's link and parse the HTML
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text information from the post
        text_info = soup.find("div", class_="view_inner").text
        text_info = Filter.filter_text(text_info)

        # Extract image information from the post
        # url 에서 장학금 관련 이미지만 추출하는 코드. 
        image_info = [img["src"] for img in soup.find_all("img") if img["src"].startswith("https://")]
        image_text = ""
        
        for img_url in image_info:
            # Use the Reader class to extract text from the image URL
            img_text = Reader.read_text_from_image_url(img_url)
            img_text = Filter.filter_text(img_text)
            img_text = img_text.replace(" ", "")
            # Add the extracted text to the post_info
            image_text += "\n" + (img_text)
        
        # filter dummy text data (made by OCR) into better data
        generated_text = Filter.filter_priority_fulfill(text_info, image_text)
        
        
        # # Initialize the GPT API caller with your API key
        # openai_api_key = OPENAI_API_KEY
        # gpt_caller = GPTAPICaller(openai_api_key)

        # # Call the GPT API to generate text based on the prompt
        # generated_text = gpt_caller.generate_text(text_info, image_text)
    

        # Add the post information to the post list
        # 개선 필요 -> 데이터 요구사항에 따라 변경해야 함 EX : 장학금제목 / 모집기간 / 모집조건-자격 / 장학금 혜택 / 전체 text data / 이미지 png url 
        post_info.append({
            "title": title,
            "url": link,
            "image_info": image_info,
            "generated_text": generated_text
        })

    return post_info

if __name__ == "__main__":
    url = 'https://www.kookmin.ac.kr/user/kmuNews/notice/7/index.do'
    post_info = scrape_kookmin_news(url)

    for i, post in enumerate(post_info):
        # Create a separate file for each data item using the index (i)
        file_name = f'data/post_{i}.txt'  # You can use a different extension like .csv for CSV files

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Title: {post['title']}\n")
            file.write(f"URL: {post['url']}\n")
            # file.write(f"Text Info: {post['text_info']}\n")
            # file.write(f"Image Text: {post['image_text']}\n")
            file.write(f"filtered Text: {post['generated_text']}\n")

            # Write image URLs as a list
            file.write("Image URLs:\n")
            for image_url in post['image_info']:
                file.write(f"{image_url}\n")

            # Add a separator between data items
            file.write("\n")
        
        print(f"Data saved to {file_name}")
