from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView 
from aps.models import APS 
from django.urls import reverse_lazy

class APSS(TemplateView):
    def get(self, request, **kwargs):
        context = {'apss': APS.objects.all().order_by('id')}
        return render(request, 'aps/list.html', context)

    def post(self, request):
        aps = APS.objects.get(id=request.POST.get('aps_id'))
        aps.active = not aps.active 
        
        aps.save()
        return redirect("aps:list")


class CreateAPS(CreateView):
    model = APS 
    fields = ["name", "description"]
    success_url = reverse_lazy('aps:list')