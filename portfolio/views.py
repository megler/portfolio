from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    return render(request, "portfolio/index.html")


def twitter_about(request):
    return render(request, "portfolio/twitter-about.html")


def zillow_about(request):
    return render(request, "portfolio/zscraper-about.html")


def stocks_about(request):
    return render(request, "portfolio/stocks-about.html")


def movies_about(request):
    return render(request, "portfolio/movies-about.html")


def blog_about(request):
    return render(request, "portfolio/blog-about.html")


def auctions_about(request):
    return render(request, "portfolio/auctions-about.html")


def anf_about(request):
    return render(request, "portfolio/anf-about.html")


def thanks(request):
    return render(request, "portfolio/thanks.html")


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            subject = "Contact Form"
            name = form.cleaned_data["your_name"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            human = True
            recipients = ["marceia.egler@gmail.com"]
            send_mail(subject, message, sender, recipients)
            return redirect("thanks")
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {"form": form})
