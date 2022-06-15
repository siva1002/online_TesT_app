from io import BytesIO
from django.template.loader import get_template
from 
from django.conf import settings
import uuid

def render_to_pdf(params:dict):
    template = get_template('ques.html')
    html = template.render(params)
    result = BytesIO()
    filename= uuid.uuid4()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    try:
        with open(str(settings.BASE_DIR)+f'/media/chapter_files/{filename}.pdf','wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),output)
    except Exception as e:
        print(e)
    if pdf.err:
        return '',False
    return filename,True