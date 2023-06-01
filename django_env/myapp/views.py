from django.shortcuts import render, HttpResponse
from django.template import loader

from myapp.models import Person, Pet

# Create your views here.
template_name_list = 'myapp/lists.html'

def index(request):
    persons = Person.objects.all()
    list_person = []

    for person in persons:
        name_person = "{} {}".format(person.first_name, person.last_name)
        list_person.append(name_person)

    list_person = ['---']
    texto_respuesta = """
        <h1>Hola mundo</h1>
        {}
    """.format(list_person)
    return HttpResponse(texto_respuesta)

def index_2(request):
    template = 'myapp/index.html'
    return render(request, template)
    # return HttpResponse(template.render())

def lists_persons(request):
    persons = Person.objects.all()

    list_persons = []
    for p in persons:
        name_person = "{} {}".format(p.first_name, p.last_name)
        list_persons.append(name_person)
    
    context = {
        "list_name": "Personas",
        "list": list_persons
    }

    return render(request, template_name_list, context)

def lists_pets(request):
    pets = Pet.objects.all()

    lists_pets = []
    for p in pets:
        lists_pets.append([p.name, p.age, p.person, p.specie])

    context = {
        "list_name": "Mascotas",
        "list": lists_pets
    }

    return render(request, template_name_list, context)
