import file_generation_service as fileGen


resumeTemplate = "templates\\resume.md"
resumeOutput = "resume.pdf"

# print("Enter the name for the output PDF: ")
# outputFilename = input()

fileGen.MDtoPDF(resumeTemplate, resumeOutput)