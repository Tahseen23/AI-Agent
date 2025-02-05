from .agentsBase import Agent


class SummarizeTool(Agent):
  def __init__(self,max_retries=3,verbose=True):
    super().__init__(name='SummarizeTool',max_retries=max_retries,verbose=verbose)
  
  def execute(self, text):
     messages = [
            {"role": "system", "content": "You are an AI assistant that summarizes medical texts."},
            {
                "role": "user",
                "content": (
                    "Please provide a concise summary of the following medical text:\n\n"
                    f"{text}\n\nSummary:"
                )
            }
        ]
     summary=self.call_gemini(messages)
     return summary
     