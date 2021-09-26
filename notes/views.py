from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_texto = request.POST.get('tag')
        lista = Tag.objects.filter(texto=tag_texto)

        note = Note()
        tag = Tag()

        if tag_texto == "":
            note.title = title
            note.content = content
            note.save()
            Tag.objects.filter(texto=tag_texto).delete()



        elif len(lista) > 0:
            tag = lista[0]
            note.title = title
            note.content = content
            note.tags = tag
            note.save()
        else:
            tag.texto = tag_texto
            tag.save()
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
    Tag.objects.filter(note__id=ide).delete()
    note.delete()
    return redirect('index')

def editar(request, ide):
    nota = Note.objects.filter(id=ide)
    primeiro = nota[0]
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        editado=Note.objects.filter(id=ide).update(title=title, content=content) 
        return redirect('index')
    return render(request, 'notes/editar.html', {'nota': primeiro})
    
def listatags(request):
    tag = Tag()
    all_tag = Tag.objects.all()
    return render(request, 'notes/listatags.html', {'notes': all_tag})



#Note.objects.create(title=title, content=content)