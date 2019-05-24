from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Phone_Book
from .forms import AddNumber

# Create your views here.
def index(request):
    files = Phone_Book.objects.all()
    context = {
        'files': files
    }
    return render(request, 'blog/index.html', context)

class FileListView(ListView):
    model = Phone_Book
    template_name = 'blog/index.html'
    context_object_name = 'files'
    ordering = ['Author']

class FileDetailView(DetailView):
    model = Phone_Book

class FileCreateView(LoginRequiredMixin, CreateView):
    model = Phone_Book
    fields = ['Name', 'Number']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class FileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Phone_Book
    fields = ['Name', 'Number']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.Author:
            return True
        return False

class FileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Phone_Book
    success_url = '/'

    def test_func(self):
        file = self.get_object()
        if self.request.user == file.Author:
            return True
        return False

@login_required
def home(request):
    book = Phone_Book()
    if request.method == 'POST':
        form = AddNumber(request.POST)
        if form.is_valid():
            book.Name = form.cleaned_data['Name']
            book.Number = form.cleaned_data['Number']
            book.save()

            return redirect('blog-profile')
    else:
        form = AddNumber
    context = {
        'form': form,
        'book': book
    }

    return render(request, 'blog/home.html', context)

@login_required
def porfile(request):
    forms = Phone_Book.objects.filter(Author=request.user)
    context = {
        'forms': forms
    }
    return render(request, 'blog/profile.html', context)