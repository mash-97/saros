from django.db.models import query
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

def test(request):
    return render(request, 'user/test.html')

class UserProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['username', 'email']
    template_name = 'users/profile.html'

    def get_queryset(self):
        queryset = super(UserProfile, self).get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return  queryset 

