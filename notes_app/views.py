from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

from django.urls import path
from . import views


def index(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes_app/index.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes_app/add_note.html', {'form': form})


def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('index')
    return render(request, 'notes_app/edit_note.html', {'note': note})


def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes_app/view_note.html', {'note': note})