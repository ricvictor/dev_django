from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.


def list_username(request):
    users = User.objects.all()
    return render(request, 'GCacc/users.html', {'users': users})


def new_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('GCacc:users')

    return render(request, 'GCacc/new_user.html', {'form': form})


def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('GCacc:users')

    return render(request, 'GCacc/new_user.html', {'form': form, 'user': user})


def delete_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('GCacc:users')

    return render(request, 'GCacc/user_delete_confirm.html', {'user': user})