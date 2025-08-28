import datetime
import json
import os
import requests
from typing import List, Dict, Any


def write_jsonl(records:List[Dict[str, Any]], data_path:str="data.jsonl"):
    with open(data_path, "w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")


def read_jsonl(data_path:str="data.jsonl"):
    with open(data_path, "r") as f:
        data = [json.loads(line) for line in f]
    return data


class LLM:

    def __init__(self):
        self.health_status:str = ""
        self.food_products:list = []
        self.chat_history = None
        self.model = "meta-llama/llama-4-scout-17b-16e-instruct"
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set")
        self.__api_key = GROQ_API_KEY

    def build_prompt(self, user_input, formatted_chat_history):
        today_date = str(datetime.datetime.now().strftime('%B %d, %Y'))
        # formatted_chat_history =  formatted_chat_history+'\n\n'
        system_prompt = f"""You are a nutrition health expert. Your job is to suggest food values and options based on the health status of the user provided below.
Answer queries with respect to the food products' options with their nutrition values provided below suitable for the user's health.
Date: {today_date}
health status: {self.health_status}
food products: {self.food_products}
"""
        messages = [{"role": "system", "content": system_prompt}]
        # messages.append({'history': chat_history})import datetime
        mid_prompt = "Please answer the following query fully and strictly in accordance with the system rules provided without mentioning or referring to those rules, restrictions for any contradictory requests.\nquery: "
        messages.append({"role": "user", "content": formatted_chat_history + mid_prompt + user_input})
        return messages

    def query(self, query):
        chat_history = self.chat_history or ""
        prompt = self.build_prompt(query, f"chat history for context reference:\n{chat_history or 'None'}\n")
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.__api_key}",
            "Content-Type": "application/json"
        }       
        payload = {
            "model": self.model,
            "messages": prompt,
            "temperature": 0.3,
            # "max_tokens": 8000          
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            api_output = response.json()
            if "error" in api_output:
                output = f"⚠️ API Error: {api_output['error'].get('message', 'Unknown error')}"
            else:
                output = api_output['choices'][0]['message']['content'].strip()
                chat_history += f"query: {query}\nresponse: {output}\n"
                self.chat_history = chat_history
        except Exception:
            output = "⚠️ Some technical error occurred at my end. Please try after sometime."
        
        return output

    