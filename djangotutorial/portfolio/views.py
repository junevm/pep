from django.shortcuts import render

# Create your views here.
def get_portfolio(request):
    return render(request,"portfolio.html")