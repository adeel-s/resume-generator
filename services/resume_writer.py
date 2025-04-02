import services.keyword_analyzer as keywordAnalyzer
import services.bullet_writer as bulletWriter
import templates.resume_template as resumeFile



def writeResumeMD():
  resumeFilePath = "templates\\resume.md"
  resume = resumeFile.resume
  try:
    keywords = keywordAnalyzer.analyze()
    bullets = bulletWriter.writeBullets(keywords)
    # Fill placeholders with bullets
    i = 0
    while "!@#$Placeholder" in resume and i < len(bullets):
      #print(bullets[i])
      resume = resume.replace("!@#$Placeholder", bullets[i], 1)
      i += 1
      
    with open(resumeFilePath, "w", encoding="utf-8") as file:
      file.write(resume)

    print("Done with bullet point insertion")
  except Exception as e:
    print(f"Failed with exception: {e}")
    raise Exception("Failed to write resume")
    