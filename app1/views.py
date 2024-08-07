from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .decorators import admin_required,user_required
from .models import Jobs,Profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Profile,JobApplications,Notifications,Messages
from django.db.models import Q
from datetime import datetime,timedelta

from django.http import JsonResponse
from django.contrib.auth.models import User

# admin
@login_required
@admin_required
def admin_home(request):
      jobs_count = len(Jobs.objects.all())
      candidates_count = len(Profile.objects.all())
      # Calculate the date 7 days ago from today
      seven_days_ago = datetime.now() - timedelta(days=7)
      # Filter notifications that are unread and from the last 7 days
      notifications = Notifications.objects.filter(read=False, date__gte=seven_days_ago)
      # notifications = Notifications.objects.filter(read=False)
      messages = Messages.objects.all()
      users = User.objects.all()
      context = {'jobs_count':jobs_count,'candidates_count':candidates_count,'notifications':notifications,'notification_count':len(notifications),'messages':messages,'message_count':len(messages)}
      return render(request,"admin/index.html",context)

def job_creation(request):
      if request.method=='POST':
            title = request.POST['title']
            location = request.POST['location']
            qualification = request.POST['qualification']
            experience = request.POST['experience']
            min_salary = request.POST['min_salary']
            max_salary = request.POST['max_salary']
            category = request.POST['job-category']
            min_age = request.POST['min-age']
            max_age = request.POST['max-age']
            job_type = request.POST['job-type']
            gender = request.POST['gender']
            skills = request.POST['skills']
            vacancies = request.POST['vacancy']
            new_job = Jobs(title=title,skills=skills,vacancy=vacancies,location=location,qualification=qualification,gender=gender,category=category,min_age=min_age,max_age=max_age,job_type=job_type,experience=experience,min_salary=min_salary,max_salary=max_salary)
            new_job.save()
            context = {"job_created":True,"title":title}
            return render(request,'admin/job_creation_form.html',context)
      else:
            return render(request,'admin/job_creation_form.html')
      
def jobs_list(request):
      jobs = Jobs.objects.all()
      context = {'jobs':jobs}
      return render(request,'admin/jobs_list.html',context)

def job_details_admin(request,pk):
      job = Jobs.objects.get(id=pk)
      applications = JobApplications.objects.filter(job=job)
      context = {'job':job,'applications':applications}
      return render(request,'admin/job_details.html',context)

def application_profile_admin(request,pk):
      user = User.objects.get(id=pk)
      global user_id
      user_id = user.id
      profile = Profile.objects.get(user=user)
      context = {"profile":profile}
      return render(request,'admin/user_profile_admin.html',context)

def edit_job(request,pk):
      global job
      job = Jobs.objects.get(id=pk)
      context = {'job':job}
      return render(request,'admin/edit_job.html',context)
      
def save_updated(request):
      job.title = request.POST['title']
      job.location = request.POST['location']
      job.qualification = request.POST['qualification']
      job.skills = request.POST['skills']
      job.experience = request.POST['experience']
      job.min_salary = request.POST['min_salary']
      job.max_salary = request.POST['max_salary']
      job.category = request.POST['job-category']
      job.job_type = request.POST['job-type']
      job.gender = request.POST['gender']
      job.min_salary = request.POST['min_salary']
      job.max_salary = request.POST['max_salary']
      job.min_age = request.POST['min_age']
      job.max_age = request.POST['max_age']
      job.vacancy = request.POST['vacancies']
      job.save()
      return redirect('jobs-admin')

def delete_job(request,pk):
      job=Jobs.objects.get(id=pk)
      title = job.title
      job_id = job.id
      job.delete()
      jobs = Jobs.objects.all()
      context = {"deleted":True,"title":title,"job_id":job_id,'jobs':jobs}
      return render(request,"admin/jobs_list.html",context)

def candidates(request):
      profiles = Profile.objects.all()
      context = {'profiles':profiles}
      return render(request,'admin/candidates.html',context)

# with temporary page , change it.
def admin_login(request):
      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            login(request,user)
            if (user is not None) and (user.is_staff):
                  return redirect("admin-home") 
            else:
                  return render(request,"admin/login.html")
      else:
            return render(request,"admin/login.html")

def user_logout(request):
      user = request.user
      if user.is_staff:
            logout(request)
            return redirect("admin_login")
      else:
            logout(request)
            return redirect("signin")


# user pages
def index(request):
      return render(request,'user/index.html')

def search_job(request):
      search_title = request.GET.get('title')
      search_location = request.GET.get('location')
      jobs = Jobs.objects.filter(
            Q(title__icontains=search_title) & Q(location__icontains=search_location)
      )
      context = {'jobs':jobs}
      return render(request,'user/jobs_listing.html',context)

def signin(request):
      if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                  login(request,user)
                  return redirect("home")
            else:
                  context = {'login_failed':True}
                  return render(request,'user/login.html',context)
      else:
            return render(request,'user/login.html')

# checking whether username exists or not.
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})


def signup(request):
      if request.method=='POST':
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = User.objects.create_user(username=email,password=password1)
            user.save()
            context = {'registered':'success'}
            return render(request,'user/login.html',context)
      else:
            return render(request,'user/register.html')

def about(request):
      return render(request,'user/about.html')

def contact(request):
      if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            email = request.user.username
            context = {'full_name':(profile.first_name+profile.last_name),'email':email}
      else:
            context = None
      return render(request,'user/contact.html',context)

@login_required(login_url='signin')
def job_listing(request):
      jobs = Jobs.objects.all()
      context = {'jobs':jobs}  
      return render(request,'user/jobs_listing.html',context)

def job_details(request,pk):
      global job
      job = Jobs.objects.get(id=pk)
      context = {'job':job}
      return render(request,'user/job_details.html',context)

@login_required(login_url='signin')
def user_profile(request):
      current_user = request.user
      try:
            profile = Profile.objects.get(user=current_user)
            job_applications = JobApplications.objects.filter(user=current_user)
            context = {"profile":profile,"jobs":job_applications}
            return render(request,'user/profile.html',context)
      except:
            return redirect('edit-profile')

def edit_profile(request):
      if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            phone1 = request.POST['phone1']
            phone2 = request.POST['phone2']
            age = request.POST['age']
            employed = request.POST['employment']
            if employed == 'yes':
                  employed = True
            else:
                  employed = False
            skills = request.POST['skills']
            qualifications = request.POST['qualification']
            certifications = request.POST['certifications']
            resume = request.FILES.get("resume")
            about = request.POST["about"]
            profile = Profile(
                  first_name = first_name,
                  last_name = last_name,
                  address = address,
                  phone1 = phone1,
                  phone2 = phone2,
                  age = age,
                  employed = employed,
                  skills = skills,
                  qualification = qualifications,
                  certifications = certifications,
                  resume = resume,
                  about = about,
                  user = request.user
            )
            profile.save()
            print("profile updated")
            return redirect("user-profile")
      else:
            return render(request,'user/edit_profile.html')

def download_resume(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    file_path = profile.resume.path
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename={profile.resume.name}'
        return response
  
def download_resume_admin(request):
    profile = get_object_or_404(Profile, user_id=user_id)
    file_path = profile.resume.path
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = f'attachment; filename={profile.resume.name}'
        return response
  
def notifications_page(request):
      notifications = Notifications.objects.all()
      context = {'notifications':notifications}
      return render(request,'admin/notifications.html',context)

def messages_page(request):
      messages = Messages.objects.all()
      context = {'messages':messages}
      return render(request,'admin/messages.html',context)

def update_profile(request):
      if request.method != 'POST':
            global profile
            profile = Profile.objects.get(user=request.user)
            context = {'profile':profile}
            return render(request,'user/update_profile.html',context)
      else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            phone1 = request.POST['phone1']
            phone2 = request.POST['phone2']
            age = request.POST['age']
            employed = request.POST['employment']
            if employed == 'yes':
                  employed = True
            else:
                  employed = False
            skills = request.POST['skills']
            qualifications = request.POST['qualification']
            certifications = request.POST['certifications']
            resume = request.FILES.get("resume")
            about = request.POST["about"]

            profile.first_name = first_name
            profile.last_name = last_name
            profile.address = address
            profile.phone1 = phone1
            profile.phone2 = phone2
            profile.age = age
            profile.employed = employed
            profile.skills = skills
            profile.qualification = qualifications
            profile.certifications = certifications
            if resume is not None:
                  profile.resume = resume
            profile.about = about
            profile.user = request.user
            
            profile.save()
            print("profile updated")
            return redirect("user-profile")

def apply_job(request):
      user = request.user
      if not JobApplications.objects.filter(Q(user=user) & Q(job=job)):
            new_application = JobApplications(user=user,job=job)
            new_application.save()
            profile = Profile.objects.get(user=user)
            fullname = profile.first_name + profile.last_name
            notification = Notifications(msg='job application',description=fullname+' applied for the job '+job.title)
            notification.save()
            return redirect('job-listing')
      else:
            context = {"job":job,"msg":"You have already applied for this job...."}
            return render(request,'user/job_details.html',context)
      
def about(request):
      return render(request,'user/about.html')

def send_message(request):
      message = request.POST['message']
      name = request.POST['name']
      email = request.POST['email']
      subject = request.POST['subject']
      new_msg = Messages(message=message,full_name=name,email=email,subject=subject)
      new_msg.save()
      return redirect('contact')