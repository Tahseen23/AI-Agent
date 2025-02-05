from .agentsBase import Agent

class RefinerAgent(Agent):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an expert editor who refines and enhances research articles for clarity, coherence, and academic quality."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Please refine the following research article draft to improve its language, coherence, and overall quality:\n\n"
                            f"{draft}\n\nRefined Article:"
                        )
                    }
                ]
            }
        ]
        refined = self.call_gemini(messages)
        return refined