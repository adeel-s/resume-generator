import services.LLM_generator as LLM
import resources.work_experience_temp, resources.llm_prompts
import resources.work_experience_list, resources.keywords

rawWorkExperience = resources.work_experience_temp.workExperience
prompt = resources.llm_prompts.experienceOptimizerPrompt
workExperienceList = resources.work_experience_list.workExperience
keywords = resources.keywords.keywords

def optimizeWorkExperience():
  optimizedWorkExperience = ""
  for exp in workExperienceList:
    fullPrompt = prompt + "\nHere is the work experience:\n\n" + exp
    fullPrompt += "\nHere is the list of keywords:\n\n" + keywords
    response = LLM.generate(fullPrompt)
    print(response)
    optimizedWorkExperience += response + "\n\n"
  with open('resources\\work_experience.txt', 'w') as file:
    file.write(optimizedWorkExperience)
    
