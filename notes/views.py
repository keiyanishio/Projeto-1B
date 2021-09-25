from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_texto = request.POST.get('tag')
        lista = Tag.objects.filter(texto=tag_texto)

        print(title, content, tag_texto)
        if len(lista) > 0:
            tag = lista[0]
        else:
            tag = Tag()
            tag.texto = tag_texto
            tag.save()
                
        #Note.objects.create(title=title, content=content)


        note = Note()
        note.title = title
        note.content = content 
        note.tags = tag
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
    
def listatags(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/listatags.html', {'notes': all_notes})
