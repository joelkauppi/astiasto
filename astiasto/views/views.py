from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from astiasto.forms import OrderForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from astiasto.models import Item, Genre

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def rent(request):
    items = Item.objects.all()
    genres = Genre.objects.all()
    form_class = OrderForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'name'
            , '')
            contact_email = request.POST.get(
                'email'
            , '')
            form_content = request.POST.get('message', '')
            amount = request.POST.get('amount', '')
            place = request.POST.get('place', '')
            phone = request.POST.get('phone','')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,


            }
            for i in Item.objects.all():
                v = i.name
                context[v] = request.POST.get(v, '')
            #for i in Item.objects.all():
            #    context = {
            #        context,


            #    }

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['astiasto@jalostajat.fi'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('valmis/')

    return render(request, 'main/rent.html', {
        'form': form_class, 'items':items, 'genres':genres
    })
def ordersent(request):
    form = {}
    return render(request, 'main/thanks.html', {'form': form})

def terms(request):
    #temp = get_template('terms.txt')
    #context = {'terms': temp}
    return render(request, 'main/terms.html')

def calendar(request):
    #temp = get_template('terms.txt')
    #context = {'terms': temp}
    return render(request, 'main/calendar.html')
