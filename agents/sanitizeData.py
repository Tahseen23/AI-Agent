from .agentsBase import Agent

class SanitizeDataTool(Agent):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
            {"role": "user", "parts": [{"text":"You are an AI assistant that sanitizes medical data by removing Protected Health Information (PHI)."}]},
            {"role": "user", "parts": [{"text": "Remove all PHI from the following data  and give only informaion How patient was treated and what are the problems patient was facing :\n\n"
                    f"{medical_data}\n\nSanitized Data:"}]}
        ]
        sanitized_data = self.call_gemini(messages)
        return sanitized_data