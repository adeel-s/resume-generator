import services.LLM_generator as LLM
import resources.job_description, resources.work_experience, resources.llm_prompts

jobDescription = resources.job_description.jobDescription
workExperience = resources.work_experience.workExperience
prompt = resources.llm_prompts.experienceBulletsPrompt
prompt += "\nHere is the job description:\n\n" + jobDescription
prompt += "\nHere is the work experience:\n\n" + workExperience

def writeBullets(keywords):
  global prompt
  prompt += "\nHere is the list of keywords:\n\n" + keywords
  bullets = LLM.generate(prompt)
  print(bullets)
  return parse(bullets)

def parse(bullets):
  return bullets.split('!@#$')