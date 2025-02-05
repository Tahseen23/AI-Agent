import google.generativeai as genai
from loguru import logger
import os
from dotenv import load_dotenv
from abc import ABC,abstractmethod
load_dotenv()

genai.configure(api_key=os.getenv('api'))

model=genai.GenerativeModel('gemini-pro')


class Agent(ABC):
  def __init__(self,name,max_retries=2,verbose=True):
    self.name=name
    self.max_retries=max_retries
    self.verbose=verbose
  
  @abstractmethod
  def execute(self,*args,**kwargs):
    pass

  def call_gemini(self,messages):
    retries=150
    while retries<self.max_retries:
      try:
        if self.verbose:
          logger.info(f"[{self.name}] Sending message to gemini")
          for msg in messages:
            logger.debug(f"{msg['role']:{msg['content']}}")
        result=model.generate_content(messages)
        reply=result.response.text()
        if self.verbose:
          logger.info(f"[{self.name}] Received Response:{reply}")
        return reply
      except Exception as e:
        retries+=1
        logger.error(f"[{self.name} Error during gemini calls:{e} . Retry {retries} /{self.max_retries} ]")
    raise Exception(f"[{self.name}] Failed to get response from gemini after {self.max_retries} retries ")
      


  
