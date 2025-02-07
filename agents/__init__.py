from .summarizeTools import SummarizeTool
from .writeArtical import WriteArticleTool
from .sanitizeData import SanitizeDataTool
from .summaryValidator import SummarizeValidatorAgent
from .writeArticleValidator import WriteArticleValidatorAgent
from .sanitizeDatavalidator import SanitizeDataValidatorAgent
from .refineAgent import RefinerAgent


class AgentManager:
  def __init__(self,max_retries=2,verbose=True):
    self.agents={
      'summarize':SummarizeTool(max_retries=max_retries,verbose=verbose),
      'write_article':WriteArticleTool(max_retries=max_retries,verbose=verbose),
      'sanitize_data':SanitizeDataTool(max_retries=max_retries,verbose=verbose),
      'summarize_validator':SummarizeValidatorAgent(max_retries=max_retries,verbose=verbose),
      'validator_agent':WriteArticleValidatorAgent(max_retries=max_retries,verbose=verbose),
      'sanitize_data_validator':SanitizeDataValidatorAgent(max_retries=max_retries,verbose=verbose),
      'refiner':RefinerAgent(max_retries=max_retries,verbose=verbose)
    }

  def get_agent(self,agent_name):
    agent=self.agents.get(agent_name)
    if not agent:
      raise ValueError(f"Agent '{agent_name}' not found")
    return agent
    