from .agentsBase import Agent

class WriteArticleTool(Agent):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic,outline=None):
        systemMessage='You are an  expert academic writter'
        userContent=f"Write a research article on the following topic:\nTopic:{topic}\n\n"
        if outline:
            userContent+=f"Outline:\n{outline}\n\n"
        userContent+=f"Article:\n"
        messages = [
            {"role": "system", "content": systemMessage},
            {"role": "user", "content": userContent}
        ]
        article = self.call_gemini(messages)
        return article