faylname = "report.pdf"

if faylname.endswith(".pdf"):
    file_type ="pdf"
elif faylname.endswith(".docx"):
    file_type = "docx"
elif faylname.endswith(".txt"):
    file_type = "txt"

else:
    file_type = "nomalum"

print(f"fayl turi:{file_type}")