from django.shortcuts import render,redirect
from .forms import UserForm, UserFilterForm  
from .models import User

def index(request):
  form = UserFilterForm(request.GET or None)
  users = User.objects.all()


  if form.is_valid():  # Verifica se o formulário é válido
      if form.cleaned_data['nome']:
          users = users.filter(nome__icontains=form.cleaned_data['nome'])
      if form.cleaned_data['email']:
          users = users.filter(email__icontains=form.cleaned_data['email'])
      if form.cleaned_data == None:
        users = User.objects.all()
  context = {
    'users': users,
    'filter_form': form

  }

  return render(request, 'index.html',context)

def create(request):

  if request.method == 'GET':
    form = UserForm()

    context = {
      'form': form,
    }

    return render(request, 'criar.html',context=context)
  else:
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(index)


def refresh(request,user_id):

  user = User.objects.get(pk=user_id)

  if request.method == 'POST':
    form = UserForm(data=request.POST,instance=user)

    if form.is_valid():
      form.save()
      return redirect(index)
  else:
    form = UserForm(instance=user)

    context = {'form': form}

    return render(request,'criar.html',context=context)

def delete(request,user_id):
  user = User.objects.get(pk=user_id)
  user.delete()

  return redirect(index)