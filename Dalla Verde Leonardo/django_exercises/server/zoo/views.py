from django.shortcuts import render
from zoo.models import animals
import json
from django.http import HttpResponse
from django.views..decorators.csrf import csrf_extempt

# Create your views here.

def home(request):
	if request.method == 'POST':
		body = request.body
		content = json.loads(body)
		animal = animals(nome=content['nome'])
		animal.save()
		return HttpResponse(status=200)
	elif request.method == 'GET':
		animal = animals.objects.all()
		list_animal = [{'nome':x.nome} for x in animal] #lista dizionari python
		resp = json.dumps(list_animal)

		return HttpResponse(resp, content_type='application/json')