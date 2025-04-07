import services.resume_writer as writer, services.MDtoPDF_converter as converter
import services.experience_optimizer
resumeTemplate = "templates\\resume.md"
resumeOutput = "resume.pdf"

services.experience_optimizer.optimizeWorkExperience()

writer.writeResumeMD()

converter.MDtoPDF(resumeTemplate, resumeOutput)



