from io import BytesIOfrom reportlab.pdfgen 
import canvasfrom django.http 
import HttpResponsefrom reportlab.lib.pagesizes 
import letter, landscapefrom reportlab.lib.pagesizes 
import A4


class Utilities():
    def generatePdf(request):
        buffer = ByteIO()
        pdf = canvas.canvas(buffer,pagesize=A4)