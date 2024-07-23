from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Notice, HODmessage, BannerImage, Resource, Teacher, Images
from .forms import NoticeForm, HODmessageForm, BannerImageForm, ResourceForm, TeacherForm, ImageForm


# Create your views here.

# filter notice from date
def notice_filter(request, key):
    try:
        notices = Notice.objects.filter(title__contains=key).order_by('-id')
        return render(request, 'notice.html', {'notices': notices, 'request': request})
    except:
        messages.error(request, f"Error loading notice...")
        return render(request, 'notice.html', {'request': request})


# get hod message
def get_hod_message(request, id):
    try:
        hodmessage = HODmessage.objects.get(id=id)
        return render(request, 'message.html', {'hodmessage': hodmessage})
    except:
        messages.error(request, f"Error loading message...")
        return render(request, 'message.html', {'hodmessage': None})


def home(request):
    try:
        notices = None
        banner_image = None
        hodmessage = None
        try:
            banner_image = BannerImage.objects.all().order_by('-id')[0]
            hodmessage = HODmessage.objects.all().order_by('-id')[0]
            notices = Notice.objects.all().order_by('-id')[:3]
        except:
            notices = Notice.objects.all().order_by('-id')
        data = {
            'request': request,
            'notices': notices,
            'banner_image': banner_image,
            'hodmessage': hodmessage
        }
        return render(request, 'home.html', data)
    except:
        messages.error(request, f"Error loading home page...")
        return render(request, 'home.html', {'request': request})


# for notice
def notice(request):
    try:
        notices = None
        try:
            notices = Notice.objects.all().order_by('-id')[:20]
        except:
            notices = Notice.objects.all().order_by('-id')
        data = {
            'request': request,
            'notices': notices,
        }

        return render(request, 'notice.html', data)
    except:
        messages.error(request, f"Error loading home page...")
        return render(request, 'notice.html', {'request': request})



# for about
def about(request):
    data = {
        'teachers': Teacher.objects.all().order_by('id'),
        'request': request,
    }

    return render(request, 'about.html', data)

# search teacher
def search_teacher(request, key):
    try:
        teachers = Teacher.objects.filter(name__contains=key).order_by('id')
        return render(request, 'about.html', {'teachers': teachers, 'request': request})
    except:
        messages.error(request, f"Error loading teacher...")
        return render(request, 'about.html', {'request': request})


# get teacher by id
def get_teacher(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        return render(request, 'teacher.html', {'teacher': teacher, 'request': request})
    except:
        messages.error(request, f"Error loading teacher...")
        return render(request, 'about.html', {'request': request})


# for resource
def resource(request):
    data = {
        'resources': Resource.objects.all().order_by('-id'),
        'request': request,
    }

    return render(request, 'resource.html', data)


# filter resource
def resource_filter(request, key):
    try:
        resources = Resource.objects.filter(title__contains=key).order_by('-id')
        return render(request, 'resource.html', {'resources': resources, 'request': request})
    except:
        messages.error(request, f"Error loading resource...")
        return render(request, 'resource.html', {'request': request})
    

#gallary
def gallary(request):
    try:
        data = {}
        try:
            data['images'] = Images.objects.all().order_by('-id')[31]
        except:
            data['images'] = Images.objects.all().order_by('-id')
            
        return render(request, 'gallary.html', data)
    except:
        return render(request, 'gallary.html')


# for contact
def contact(request):
    data = {
        'request': request,
    }

    return render(request, 'contact.html', data)


# for login
def login_user(request):
    data = {
        'request':request,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth = authenticate(request, username=username, password=password)

        if auth is not None:
            login(request, auth)
            return redirect('admin')
        else:
            messages.error(request, f"Invalid credencials...")

    return render(request, 'login.html', data)




########################for admin######################

@login_required(login_url='home')
def admin_home(request):
    data = {
        'request': request,
    }

    if request.method == 'POST':
        bannerimage_data = BannerImageForm(request.POST, request.FILES)
        if bannerimage_data.is_valid():
            bannerimage_data.save()
            messages.success(request, f"Banner image added successfully...")
            return redirect('admin')
        else:
            messages.error(request, f"Error uploading banner image...")

        HODmessage_data = HODmessageForm(request.POST, request.FILES)
        if HODmessage_data.is_valid():
            HODmessage_data.save()
            messages.success(request, f"HOD message added successfully...")
            return redirect('admin')
        else:
            messages.error(request, f"Error uploading HOD message...")


    try:
        data['hodmessage'] = HODmessage.objects.all().order_by('-id')[0]
    except:
        data['hodmessage_form'] = HODmessageForm()
    try:
        data['bannerimage'] = BannerImage.objects.all().order_by('-id')[0]
    except:
        data['bannerimage_form'] = BannerImageForm()

    return render(request, 'admin/admin_home.html', data)


# for admin_notice
@login_required(login_url='home')
def admin_notice(request):
    if request.method == 'POST':
        notice_data = NoticeForm(request.POST, request.FILES)
        if notice_data.is_valid():
            notice_data.save()
            messages.success(request, f"Notice added successfully...")
        else:
            messages.error(request, f"Error uploading notice...")

    data = {
        'request': request,
        'notices': Notice.objects.all().order_by('-id'),
        'notice_form': NoticeForm(),
    }

    return render(request, 'admin/admin_notice.html', data)


# for admin_about
@login_required(login_url='home')
def admin_about(request):
    data = {
        'teacher_form': TeacherForm(),
        'teachers': Teacher.objects.all().order_by('id'),
        'request': request,
    }

    if request.method == 'POST':
        teacher_data = TeacherForm(request.POST, request.FILES)
        if teacher_data.is_valid():
            teacher_data.save()
            messages.success(request, f"Teacher added successfully...")
        else:
            messages.error(request, f"Error uploading teacher...")

    return render(request, 'admin/admin_about.html', data)


# for admin_resource
@login_required(login_url='home')
def admin_resource(request):
    if request.method == 'POST':
        resource_data = ResourceForm(request.POST, request.FILES)
        if resource_data.is_valid():
            resource_data.save()
            messages.success(request, f"Resource added successfully...")
        else:
            messages.error(request, f"Error uploading resource...")

    data = {
        'resources': Resource.objects.all().order_by('-id'),
        'request': request,
        'resource_form': ResourceForm(),
    }

    return render(request, 'admin/admin_resource.html', data)


# for admin_contact
@login_required(login_url='home')
def admin_contact(request):
    data = {
        'request': request,
    }

    return render(request, 'admin/admin_contact.html', data)


@login_required(login_url='home')
def admin_notice_delete(request, id):
    try:
        notice = Notice.objects.get(id=id)
        notice.delete()
        messages.success(request, f"Notice deleted successfully...")

        return redirect('admin_notice')
    except:
        messages.error(request, f"Notice not found")

        return redirect('admin_notice')
    
# edit notice
@login_required(login_url='home')
def admin_notice_edit(request, id):
    try:
        notice = Notice.objects.get(id=id)
        if request.method == 'POST':
            notice_form = NoticeForm(request.POST, request.FILES, instance=notice)

            if notice_form.is_valid():
                notice_form.save()
                messages.success(request, f"Notice updated successfully...")

                return redirect('admin_notice')

        data = {
            'request': request,
            'notice_form_edit': NoticeForm(instance=notice),
            'notices': Notice.objects.all().order_by('-id'),
        }

        return render(request, 'admin/admin_notice.html', data)
    except:
        messages.error(request, f"Notice not found")

        return redirect('admin_notice')
    

# add HODmessage
@login_required(login_url='home')
def admin_HODmessage_update(request, id):
    try:
        hodmessage = HODmessage.objects.get(id=id)
        if request.method == 'POST':
            hodmessage_form = HODmessageForm(request.POST, request.FILES, instance=hodmessage)

            if hodmessage_form.is_valid():
                hodmessage_form.save()
                messages.success(request, f"HOD message updated successfully...")

                return redirect('admin')
        data = {
            'request': request,
            'hodmessage_form_edit': HODmessageForm(instance=hodmessage),
            'hodmessage': HODmessage.objects.all().order_by('-id')[0],
            'bannerimage': BannerImage.objects.all().order_by('-id')[0],
        }

        return render(request, 'admin/admin_home.html', data)
    except:
        messages.error(request, f"HOD message not found")

        return redirect('admin_home')
    

# admin_banner_image_update
@login_required(login_url='home')
def admin_banner_image_update(request, id):
    try:
        bannerimage = BannerImage.objects.get(id=id)
        if request.method == 'POST':
            bannerimage_form = BannerImageForm(request.POST, request.FILES, instance=bannerimage)

            if bannerimage_form.is_valid():
                bannerimage_form.save()
                messages.success(request, f"Banner image updated successfully...")

                return redirect('admin')
        data = {
            'request': request,
            'bannerimage_form_edit': BannerImageForm(instance=bannerimage),
            'bannerimage': BannerImage.objects.all().order_by('-id')[0],
            'hodmessage': HODmessage.objects.all().order_by('-id')[0],
        }

        return render(request, 'admin/admin_home.html', data)
    except:
        messages.error(request, f"Banner image not found")

        return redirect('admin')
    

# delete resources
@login_required(login_url='home')
def admin_resource_delete(request, id):
    try:
        resource = Resource.objects.get(id=id)
        resource.delete()
        messages.success(request, f"Resource deleted successfully...")

        return redirect('admin_resource')
    except:
        messages.error(request, f"Resource not found")

        return redirect('admin_resource')
    

#edit resources
@login_required(login_url='home')
def admin_resource_edit(request, id):
    try:
        resource = Resource.objects.get(id=id)
        if request.method == 'POST':
            resource_form = ResourceForm(request.POST, request.FILES, instance=resource)

            if resource_form.is_valid():
                resource_form.save()
                messages.success(request, f"Resource updated successfully...")

                return redirect('admin_resource')

        data = {
            'request': request,
            'resource_form_edit': ResourceForm(instance=resource),
            'resources': Resource.objects.all().order_by('-id'),
        }

        return render(request, 'admin/admin_resource.html', data)
    except:
        messages.error(request, f"Resource not found")

        return redirect('admin_resource')
    

# filter admin_notice
@login_required(login_url='home')
def admin_notice_filter(request, key):
    try:
        notices = Notice.objects.filter(title__contains=key).order_by('-id')

        data = {
            'notices': notices,
            'request': request,
            'key': key,
            'notice_form': NoticeForm(),
        }
        return render(request, 'admin/admin_notice.html', data)
    except:
        messages.error(request, f"Error loading notice...")
        return render(request, 'admin/admin_notice.html', {'request': request})
    

# for logout
@login_required(login_url='home')
def logout_user(request):
    logout(request)
    return redirect('home')


# delete teacher
@login_required(login_url='home')
def admin_teacher_delete(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        messages.success(request, f"Teacher deleted successfully...")

        return redirect('admin_about')
    except:
        messages.error(request, f"Teacher not found...")

        return redirect('admin_about')
    

#edit teacher
@login_required(login_url='home')
def admin_teacher_edit(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        if request.method == 'POST':
            teacher_form = TeacherForm(request.POST, request.FILES, instance=teacher)

            if teacher_form.is_valid():
                teacher_form.save()
                messages.success(request, f"Teacher updated successfully...")

                return redirect('admin_about')

        data = {
            'request': request,
            'teacher_form_edit': TeacherForm(instance=teacher),
            'teachers': Teacher.objects.all().order_by('id'),
        }

        return render(request, 'admin/admin_about.html', data)
    except:
        messages.error(request, f"Teacher not found")

        return redirect('admin_about')
    
    
# gallary
@login_required(login_url='home')
def admin_gallary(request):
    try:
        data = {
            'image_form':ImageForm,
            'images':Images.objects.all().order_by('-id')
        }
        
        if request.method == 'POST':
            image_data = ImageForm(request.POST, request.FILES)
            
            if(image_data.is_valid()):
                messages.success(request, f"Image uploaded successfully... {request.POST.get('image')}")
                image_data.save()
                
            
        return render(request, 'admin/admin_gallary.html', data)
    except:
        return render(request, 'admin/admin_gallary.html', {'image_form':ImageForm})
    

@login_required(login_url='home')
def admin_gallary_delete(request, id):
    try:
        image = Images.objects.get(id=id)
        image.delete()
        messages.error('Image deleted...')
        # return redirect('admin_gallaary')
    except:
        return redirect('admin_gallary')