from django.shortcuts import render, HttpResponse
from django.template import loader

from myapp.models import Person

# Create your views here.
def index(request):
    persons = Person.objects.all()
    list_person = []

    for person in persons:
        name_person = "{} {}".format(person.first_name, person.last_name)
        list_person.append(name_person)

    texto_respuesta = """
        <h1>Hola mundo</h1>
        {}
    """.format(list_person)
    return HttpResponse(texto_respuesta)

def index_2(request):
    template = 'myapp/index.html'
    return render(request, template)
    # return HttpResponse(template.render())