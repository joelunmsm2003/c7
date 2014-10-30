from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext

from django.core import serializers
import simplejson

from diloo_mtv.models import Chat,Colas,OriLlamadas,OriAcd,OriLlamadas261013
import socket



# Create your views here.


def sobre(request):
	html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
	return HttpResponse(html)

def pregunta(request):

	preguntas = Question.objects.all()
	print preguntas[0]
	return render_to_response('base.html',{'preguntas':preguntas})

def main(request):
	return render_to_response('ajaxexample.html', context_instance=RequestContext(request))


def post(request):

	x = request.POST['client_response']              
	y = socket.gethostbyname(x)                           
	#response_dict = {}                                          
	#response_dict.update({'server_response': y })  
                                                               
	return HttpResponse(simplejson.dumps(y), mimetype='application/javascript') 


def monitoreo(request):

	return render_to_response('monitoreo.html',context_instance=RequestContext(request))

def push(request):

	x = request.POST['id_ori_llamadas']   
	
	return HttpResponse(simplejson.dumps(x), mimetype='application/javascript') 


def ori(request):
   
	x = request.POST['nori']


	numori = OriLlamadas261013.objects.count()


	data = serializers.serialize("json", OriLlamadas261013.objects.filter(id_ori_llamadas=2835071))

	print data

	return HttpResponse(data) 



def orillamadas(request):

	orillamadas = OriLlamadas261013.objects.all().order_by('-id_ori_llamadas')[:50]
	
	
	
	#return render_to_response('orillamadas.html',{'orillamadas':orillamadas})
	return render_to_response('orillamadas.html',context_instance=RequestContext(request))
