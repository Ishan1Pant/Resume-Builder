from django.shortcuts import render,get_object_or_404
from .models import resume
from django.contrib import messages
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
config=pdfkit.configuration(wkhtmltopdf=r"D:/web dev/wkhtmltox/bin/wkhtmltopdf.exe")
# Create your views here.
def main(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        about=request.POST['about']
        degree=request.POST['degree']
        school=request.POST['school']
        university=request.POST['university']
        previous=request.POST['previous']
        skills=request.POST['skills']

        pdf=resume(name=name,email=email,phone=phone,about=about,degree=degree,school=school,university=university,previous=previous,skills=skills)
        pdf.save()
        messages.success(request,"Your details have been saved")

    return render(request,'resumeapp/accept.html')

def profile(request, id):
    pro=resume.objects.get(pk=id)
    template=loader.get_template('resumeapp/profile.html')
    html=template.render({'pro':pro})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,options,configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attactment'
    filename='resumebuilder.pdf'
    return response


def list_item(request):
    list_items=resume.objects.all()
    return render(request,'resumeapp/all.html',{'list_items':list_items})
