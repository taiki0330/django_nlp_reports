from docx import Document

doc = Document('/Users/matsuzakidaiki/anaconda3/envs/django_nlp_env/reportsproject/reportsapp/docx_templates/ninsou.docx')
print(type(doc))

doc.save('ninsou2.docx')