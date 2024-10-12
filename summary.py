# Our objective is to develop a novel web browser that provides summaries of web pages.
# Given a URL, it will respond with a concise summary - essentially creating a "Reader's Digest" for the internet.

# Before proceeding, ensure you have set up your OpenAI API key in the .env file.

# imports
import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
openai = OpenAI()

# Uncomment the line below if you encounter any issues:
# openai = OpenAI(api_key="your-key-here")

# A class to represent a Webpage
class Website:
    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        # Remove irrelevant elements from the page
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        # Extract the text content of the page
        self.text = soup.body.get_text(separator="\n", strip=True)

# Test the Website class
# anth = Website("https://anthropic.com")
# print(anth.title)
# print(anth.text)

# Define system and user prompts for the AI
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "The contents of this website is as follows; \
                please provide a short summary of this website in markdown. \
                If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# Prepare messages for the OpenAI API
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# Function to summarize a website
def summarize(url):
    # Create a Website object from the given URL
    website = Website(url)
    # Send a request to the OpenAI API for summarization
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )
    # Return the generated summary
    return response.choices[0].message.content

# Function to format the markdown summary
def format_markdown(text):
    lines = text.split('\n')
    formatted = []
    for line in lines:
        # Convert main headers to uppercase
        if line.startswith('# '):
            formatted.append(line[2:].upper())
        # Convert subheaders to title case
        elif line.startswith('## '):
            formatted.append(line[3:].title())
        # Convert bullet points to a different style
        elif line.startswith('- '):
            formatted.append('  • ' + line[2:])
        else:
            formatted.append(line)
    return '\n'.join(formatted)

# Function to display the summary
def display_summary(url):
    # Get the summary for the given URL
    summary = summarize(url)
    # Format the summary
    formatted_summary = format_markdown(summary)
    # Print the formatted summary
    print(f"\nRésumé pour {url}:")
    print("-" * 40)
    print(formatted_summary)
    print("-" * 40)

# Example usage
display_summary("https://www.artificialintelligence-news.com/")
display_summary("https://fr.euronews.com/tag/paris")
display_summary("https://cnn.com")


# Note: Some websites with complex JavaScript might not work with this simple scraping method.
# Advanced techniques like using Selenium or Playwright could be employed for such cases.
# This summarization technique has wide-ranging applications across various business sectors.
# It can be used for summarizing news, financial reports, resumes, and much more.
# Consider how you might apply this summarization capability in your own business context.
# Feel free to share your ideas or discuss potential applications. Collaboration and
# exchange of ideas can lead to exciting new perspectives in this rapidly evolving field.
