from django.shortcuts import render


def test(request):
    return render(request, 'user/test.html')
