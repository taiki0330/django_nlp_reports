from docxtpl import DocxTemplate

doc = DocxTemplate("/Users/matsuzakidaiki/anaconda3/envs/django_nlp_env/reportsproject/reportsapp/docx_templates/Paragraph_usage_List2JP.docx")
context = { 
           'create_date' : "令和６年３月４日",
           'title': '被疑者の人相着衣',
           'crime_date': '令和６年３月３日',
           'crime_name': '暴行',
           'photograph_date': '令和６年３月４日',
           'photograph_place': '福岡県東警察署',
           'suspect_honseki': '福岡市中央区大名一丁目１番地',
           'suspect_address': ''
           }
doc.render(context)
doc.save("generated_doc.docx")