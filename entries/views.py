from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Entry

class LockedView(LoginRequiredMixin):
     login_url = "admin:login"

class EntryListView(LockedView, ListView):
	model = Entry
	queryset = Entry.objects.all().order_by("-date_created") # returns all entries ordered by primary key ordered by newest to oldest


class EntryDetailView(LockedView, DetailView):
	model = Entry

class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "New entry made."

class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "New update to an entry made."

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk} # refers to entry update instance, not diary entry, so not self.entry.id
        )

class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Entry deleted."
    def delete(self, request, *args, **kwards):
         messages.success(self.request, self.success_message)
         return super().delete(request, *args, **kwards) # call entry delete within delete.
'''
self refers to the object (def delete) and super(). finds the parent class
"EntryDeleteView" in this case.

*args allows the function to collect any extra positional 
args(which are collected into tuple inside function)
while kwargs allows it to accept any number of extra
keyword arguements, collected into a dict.

tl;dr: 
keyword args: nameAge(name="Cohen", age=19)
posit args: nameAge("Cohen", 19)

'''