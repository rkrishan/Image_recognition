# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from my_imagesearch.colordescriptor import ColorDescriptor
from my_imagesearch.searcher import Searcher
import csv
import cv2
import PIL
from Image_recognition.search1 import Solution
from Image_recognition.models import Document
from Image_recognition.forms import DocumentForm
from Image_recognition.performRecognition import DigitRecognizer
from Image_recognition.facerecog import FaceRecognition



def index(request):
    return render(request,'home.html')
	

def list(request):
	# Handle file upload
	RESULTS_ARRAY=[]
	form = DocumentForm()
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():

			newdoc = Document(docfile=request.FILES['docfile'])
			newdoc.save()
			obj=Solution()
			ac = obj.perform(newdoc.docfile.path)
			url = newdoc.docfile.url

			for (score,resultID) in ac:
				RESULTS_ARRAY.append(resultID)
		# return the RESULT_ARRAY to static page list.html in Template Folder
		return render(request, 'image_recognition.html',{'form': form,"imgS" : RESULTS_ARRAY,"image_path" : url})


	else:
		form = DocumentForm()  # A empty, unbound form

	# Load documents for the list page
	documents = Document.objects.all()

    # Render list page with the documents and the form
	return render_to_response(
        'image_recognition.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def digit_recognize(request):
	form = DocumentForm()
	if request.method == 'POST':
		form = DocumentForm(request.POST,request.FILES)
		if form.is_valid():

			digit_docfile = Document(docfile=request.FILES['docfile'])
			digit_docfile.save()

			objct = DigitRecognizer()
			mylist = []
			digit_list = objct.perform(digit_docfile.docfile.path)

			digit_image_url = digit_docfile.docfile.url
			for value in digit_list:
				mylist.append(int(value))
			return render(request,'digit.html',{'form':form,'image_path' : digit_image_url,'digit_value':mylist})
			# return HttpResponse(digit_list)

	else:
		form = DocumentForm()  # A empty, unbound form

	# # Load documents for the list page
	documents = Document.objects.all()

 #    # Render list page with the documents and the form
	return render_to_response(
        'digit.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )



def face_recognize(request):
	form = DocumentForm()
	if request.method == 'POST':
		form = DocumentForm(request.POST,request.FILES)
		if form.is_valid():

			face_docfile = Document(docfile=request.FILES['docfile'])
			face_docfile.save()
			face_image_url = face_docfile.docfile.url

			faceobj = FaceRecognition()

			num,conf=faceobj.perform_recognition(face_docfile.docfile.path)


			return render(request,'face.html',{'form':form, "count":conf, "image_path" :face_image_url ,"number":num})

			# return HttpResponse(conf)

	else:
		form = DocumentForm()  # A empty, unbound form

	# # Load documents for the list page
	documents = Document.objects.all()

 #    # Render list page with the documents and the form
	return render_to_response(
        'face.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
