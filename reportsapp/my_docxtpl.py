from docxtpl import DocxTemplate

doc = DocxTemplate("./docx_templates/example.docx")
context = { 'title' : "ワード" }
doc.render(context)
doc.save("generated_doc.docx")