
from django.shortcuts import render,redirect
from. models import Car,BuyedCar
from. forms import CommentForm
from django.contrib.auth.models import User
from django.views.generic import DetailView,UpdateView
from. forms import CreateUserForm,EditUserData
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg='id'
    template_name='car_details.html'
    def post(self, request, *args, **kwargs):
        comment_form=CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.car=post
            new_comment.save()
        return self.get(request, *args, **kwargs)    
    

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        car=self.object
        comments=car.comments.all()
        comment_form=CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context

@login_required
def copy_car(request,id):
    car=Car.objects.get(pk=id)
    car.car_quantity-=1
    if  car.car_quantity<1:
        messages.warning(request,'The Car is out of stock')
    else:
        buyed_car=BuyedCar(
            user=request.user,
            car_image=car.car_image,
            car_name=car.car_name,
            car_price=car.car_price,
            car_quantity=car.car_quantity,
            car_brand_name=car.car_brand_name
        )
        
        car.save()
        buyed_car.save()

    return redirect('profile')
    # return render(request,'profile.html')


def create_user(request):
    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        form=CreateUserForm()
    return render(request,'signup.html',{'form':form, 'type':'Signup'})


class login_user_view(LoginView):
    template_name='signup.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'You are logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'You enter wrong information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context

@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request,'You are logged out successfully')
        return reverse_lazy('login')

@login_required 
def profile(request):
    car=BuyedCar.objects.filter(user=request.user)
    return render(request, 'profile.html',{'car':car})
    
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model=User
    form_class=EditUserData
    template_name='signup.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')
    

    def form_valid(self, form):
        messages.success(self.request, 'Profile updeted successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='EditProfile'
        return context

def edit_profile(request):
    if request.method=='POST':
        form=EditUserData(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form=EditUserData(instance=request.user)
    return render(request, 'signup.html', {'form': form,'type': 'Edit_profile'})

