from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(response):
    return render(response, 'main/home.html')

class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'main/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateNoteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'main/update.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self): 
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/'

    # def test_func(self): 
    #     note = self.get_object()
    #     if self.request.user == note.user:
    #         return True
    #     return False