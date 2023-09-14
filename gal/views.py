from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import UserImage

from django.shortcuts import get_object_or_404
from django.http import FileResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            UserImage.objects.create(user=request.user, image=image)
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


@login_required(login_url='login')
def image_list(request):
    user_images = UserImage.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'user_images': user_images})


@login_required(login_url='login')
def view_user_images(request, user_id):
    user = User.objects.get(pk=user_id)
    user_images = UserImage.objects.filter(user=user)
    return render(request, 'user_images.html', {'user_images': user_images, 'user': user})


@login_required(login_url='login')
def preview_image(request, image_id):
    user_image = get_object_or_404(UserImage, id=image_id)
    image_path = user_image.image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


@login_required(login_url='login')
def preview_imageip(request, image_id):
    user_image = get_object_or_404(UserImage, id=image_id, user=request.user)
    image_path = user_image.image.path

    # Provide the image for preview
    context = {'user_image': user_image}

    # Add the image path for download
    context['download_url'] = image_path

    return render(request, 'preview_image.html', context)


@login_required(login_url='login')
def delete_image(request, image_id):
    user_image = get_object_or_404(UserImage, id=image_id, user=request.user)

    if request.method == 'POST':
        user_image.image.delete()  # Delete the image file
        user_image.delete()  # Delete the database record
        return redirect('image_list')

    return render(request, 'delete_image.html', {'user_image': user_image})


@login_required(login_url='login')
def download_image(request, image_id):
    user_image = get_object_or_404(UserImage, id=image_id, user=request.user)
    image_file = user_image.image

    response = FileResponse(open(image_file.path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{image_file.name}"'
    return response


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirmpassword')

        if pass1 != pass2:
            return HttpResponse("Password didn't match!!")
        else:

            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            return redirect('login')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('userhome')
        else:
            return HttpResponse("Username or Password is incorrect!!")
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('index')
