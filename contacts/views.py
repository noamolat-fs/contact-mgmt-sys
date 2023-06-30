import typing
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from contacts.models import Contact

# Create your views here.
def index(request: HttpRequest):
    query = request.GET.get("query", "")
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    context = dict(
        query=query,
        contacts=contacts,
    )
    return render(request, "contacts/index.html", context)

def create(request: HttpRequest):
    if request.method == "GET":
        return render(request, "contacts/create.html")
    elif request.method == "POST":
        post = request.POST
        kwargs = dict(
            name=post["name"],
            address=post["address"],
            email=post["email"],
            mobile=post["mobile"],
        )
        Contact(**kwargs).save()
        return HttpResponseRedirect(reverse("contacts:index"))

def read(request: HttpRequest, uid: int):
    contact = get_object_or_404(Contact, pk=uid)
    if request.method == "GET": return view(request, contact)
    elif request.method == "POST": return delete(request, contact)

def view(request: HttpRequest, contact: Contact):
    context = dict(
        contact=contact,
    )
    return render(request, "contacts/read.html", context)

def update(request: HttpRequest, uid: int):
    contact = get_object_or_404(Contact, pk=uid)
    if request.method == "GET":
        return render(request, "contacts/update.html", dict(contact=contact))
    elif request.method == "POST":
        post = request.POST
        kwargs = dict(
            name=post["name"],
            address=post["address"],
            email=post["email"],
            mobile=post["mobile"],
        )
        Contact(id=contact.id, **kwargs).save()
        return HttpResponseRedirect(reverse("contacts:index"))

def delete(request: HttpRequest, contact: Contact):
    contact.delete()
    return HttpResponseRedirect(reverse("contacts:index"))