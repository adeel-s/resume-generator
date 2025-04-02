import services.resume_writer as writer, services.MDtoPDF_converter as converter

resumeTemplate = "templates\\resume.md"
resumeOutput = "resume.pdf"

writer.writeResumeMD()

converter.MDtoPDF(resumeTemplate, resumeOutput)



