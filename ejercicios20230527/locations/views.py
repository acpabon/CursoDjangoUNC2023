from django.shortcuts import render
from locations.models import Department, City, District

from rest_framework import viewsets, permissions
from .serializers import DepartmentSerializer, CitySerializer, DistrictSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]

def all(request):
    #data = District.objects.select_related('city_id')
    # data = District.objects.select_related('city').all()
    # data = Department.objects.select_related('city_id').all()

    data = []
    departments = Department.objects.all()
    
    for d in departments:
        cities = City.objects.filter(department_id = d.id).all()
        
        for c in cities:
            districts = District.objects.filter(city_id = c.id).all()

            for di in districts:
                data.append([d.name, c.name, di.name])

    # print(data)
    context = {
        "data": data
    }

    template_name = 'locations/todo.html'

    return render(request, template_name, context)

def departamentos(request):
    departments = Department.objects.all()

    if departments:
        context = {
            "departments": departments
        }

    template_name = 'locations/departamentos.html'

    return render(request, template_name, context)

def ciudades(request, name_department):
    name_d  = Department.objects.filter(name__iexact = name_department).first()

    if name_d:
        ciudades = City.objects.filter(department_id = name_d).all()
    
        context = {
            "display": True,
            "department": name_d,
            "cities": ciudades
        }
    else:
        context = {
            "display": False
        }

    template_name = 'locations/ciudades.html'
    return render(request, template_name, context)

def barrios(request, name_department, name_city):
    name_d  = Department.objects.filter(name__iexact = name_department).first()

    if name_d:
        name_c = City.objects.filter(name__iexact = name_city, department_id = name_d).first()

        if name_c:
            districs = District.objects.filter(city_id = name_c).all()

            context = {
                "display": True, 
                "city": name_c.name + ", " + name_d.name, 
                "distrits": districs
            }
        else:
            context = {
                "display": False
            }

    else:
        context = {
            "display": False
        }
    
    template_name = 'locations/barrios.html'
    return render(request, template_name, context)

