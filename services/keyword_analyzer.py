import services.LLM_generator as LLM
import resources.job_description, resources.keywords, resources.llm_prompts

jobDescription = resources.job_description.jobDescription
keywords = resources.keywords.keywords
prompt = resources.llm_prompts.keywordPrompt

prompt += "\nHere is the job description:\n\n" + jobDescription
prompt += "\nHere is the list of keywords: \n\n" + keywords

def analyze():
  return LLM.generate(prompt)