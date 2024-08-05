from django.urls import path
from .import views

urlpatterns=[
      path('',views.index,name='home'),
      path('signin',views.signin,name='signin'),
      path('signup',views.signup,name='signup'),
      path('about',views.about,name='about'),
      path('contact',views.contact,name='contact'),
      path('user-profile',views.user_profile,name='user-profile'),
      path('edit-profile',views.edit_profile,name='edit-profile'),
      path('update-profile',views.update_profile,name='update-profile'),
      # admin
      path("admin_login",views.admin_login,name="admin_login"),
      path("admin_home",views.admin_home,name="admin-home"),
      path("logout",views.user_logout,name="logout"),
      path("create-job",views.job_creation,name="create-job"),
      path("jobs",views.jobs_list,name='jobs-admin'),
      path("candidates",views.candidates,name='candidates'),
      path("edit-job/<int:pk>",views.edit_job,name="edit_job"),
      path("save-updated",views.save_updated,name="save-updated"),
      path("delete-job/<int:pk>",views.delete_job,name="delete-job"),
      path("job-details-admin/<int:pk>",views.job_details_admin,name="job-details-admin"),
      path("application-profile-admin/<int:pk>",views.application_profile_admin,name="application-profile-admin"),
      path('download_resume_admin/', views.download_resume_admin, name='download_resume_admin'),
      path('notifications-page',views.notifications_page,name='notifications-page'),
      path('messages-page',views.messages_page,name='messages-page'),
      
      path("job-listing",views.job_listing,name='job-listing'),
      path("job-details/<int:pk>",views.job_details,name="job-details"),
      path('profile/<int:user_id>/download/', views.download_resume, name='download_resume'),
      path('apply-job',views.apply_job,name='apply-job'),
      path('about',views.about,name='about'),
      path('contact',views.contact,name='contact'),
      path('send_message',views.send_message,name="send_message"),
      path('ajax/check_username',views.check_username,name='check_username'),
      
      path('search_job',views.search_job,name='search_job')
]

# change the urls - include admin in each url.
