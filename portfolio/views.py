from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse  # new

from .models import Post
from .models import Post,Contact
from .forms import ContactForm
from .bot import send_message

def home(request):
    posts=Post.objects.all()
    context={"posts":posts}

    if request.method == "GET":
        form  = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        # phone_number = form.cleaned_data["phone_number"]
        description = form.cleaned_data["description"]

        # send_message(name,email,description)

        
        form.save()
        form = ContactForm()
        return HttpResponseRedirect(reverse('home_page'))
    context = {"form":form}

    return render(request,'index.html',context=context)


    