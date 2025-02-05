import os
import logging
from abc import ABC, abstractmethod
import google.generativeai as genai


# Configure GenAI API
genai.configure(api_key=os.getenv('api'))
model = genai.GenerativeModel('gemini-pro')

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Agent(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_gemini(self, messages):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending message to Gemini")
                result = model.generate_content(messages)
                reply = result.text  
                print(reply)
                if self.verbose:
                    logger.info(f"[{self.name}] Received Response: {reply}")

                return reply

            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during Gemini call: {e}. Retry {retries}/{self.max_retries}")

        raise Exception(f"[{self.name}] Failed to get response from Gemini after {self.max_retries} retries.")