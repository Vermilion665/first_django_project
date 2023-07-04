from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from myapp.views import menu

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user, 'menu': menu})
        else:
            user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'user_form': user_form, 'menu': menu})
