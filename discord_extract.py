"""
I can't remember what this file was for, probably ctih1/MessageAi?
"""

import os
import json
from datetime import datetime

class Extraction:
    def __init__(self, file_location:str):
        self.file_location = file_location
        self.valid = self.__check_is_valid()
        self.convo_data = {} # {str id: str name}

        self.sentences = []

        self.get_channel_name_id()
        print(f"Is valid? {self.valid}")

    def __check_is_valid(self) -> bool:
        try:
            return "messages" in os.listdir(self.file_location)
        except FileNotFoundError:
            return False
    
    def get_channel_name_id(self):
        if not self.valid:
            print("File path is not valid!")
            raise AttributeError("File path is not valid!")
        with open(os.path.join(self.file_location,"messages","index.json"),"r", encoding="utf-8") as f:
            self.convo_data = json.load(f)
        return self.convo_data

    def loop_over_folders(self):
        message_path = os.path.join(self.file_location,"messages")
        for folder in [f.path for f in os.scandir(message_path) if f.is_dir()]:
            folder_path = os.path.join(message_path, folder)
            print(folder_path)

            with open(os.path.join(folder_path,"channel.json") ,"r", encoding="utf-8") as f:
                channel_id = json.load(f)["id"]
                print(f"Processing channel {self.convo_data[channel_id]} (folder {folder})")

            with open(os.path.join(folder_path,"messages.json") ,"r", encoding="utf-8") as f:
                messages = json.load(f)
            
            messages.sort(key=lambda x: datetime.strptime(x["Timestamp"], "%Y-%m-%d %H:%M:%S"))
            for message in messages:
                content = message["Contents"].strip()
                if not content or content.startswith("https://"):
                    continue  # skip empty messages or links
                self.sentences.append(content)

        return self
    
    def get_messages(self) -> list:
        return self.sentences
    

messages = Extraction(r"C:\path")
messages.loop_over_folders()

with open("discord_chunks.txt", "w", encoding="utf-8") as f:
    for chunk in messages.get_messages():
        f.write(chunk + "\n")
