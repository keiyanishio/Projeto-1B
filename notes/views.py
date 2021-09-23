from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        #Note.objects.create(title=title, content=content)
        note = Note()
        note.title = title
        note.content = content 
        note.save() 
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def deletar(request, ide):
    note = Note()
    note.id = ide
    note.delete()
    return redirect('index')

def editar(request, ide):
    nota = Note.objects.filter(id=ide)
    print(nota)
    primeiro = nota[0]
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        editado=Note.objects.filter(id=ide).update(title=title, content=content) 
        return redirect('index')
    return render(request, 'notes/editar.html', {'nota': primeiro})
    
