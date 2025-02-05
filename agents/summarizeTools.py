from .agentsBase import Agent
class SummarizeTool(Agent):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name='SummarizeTool', max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        
        messages = [
            {"role": "user", "parts": [{"text": "You are an AI assistant that summarizes medical texts."}]},
            {"role": "user", "parts": [{"text": f"Please provide a concise summary of the following medical text:\n\n{text}\n\nSummary:"}]}
        ]

        summary = self.call_gemini(messages)
        return summary