# pylint: disable=E1101
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Mail
import os
from dotenv import load_dotenv

load_dotenv()


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

            message = Mail(
                from_email=From(os.environ["SG_RECEIVER_EMAIL"], name),
                to_emails=To(os.environ["SG_RECEIVER_EMAIL"], "Marceia"),
                subject="Contact Form",
                html_content=f"Sender: {sender}<br /> Message: {message}",
            )
            try:
                sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.to_dict)
            return redirect("portfolio:thanks")
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {"form": form})
