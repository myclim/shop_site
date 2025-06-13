from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from user.forms import UserLoginForm, UserRegistrationForm, UpdateForm




class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        messages.success(self.request, 'Вошли в акаунт')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Login - page'
        return context
    

class UserRegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        messages.success(self.request, 'Профиль создан')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register - page'
        return context
    

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    form_class = UpdateForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Профиль обновлен')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Profile - page'
        context['avatar'] = self.request.user.image
        return context
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('main:index'))