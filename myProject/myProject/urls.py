from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
    path('',loginPage,name='loginPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('createResumePage/',createResumePage,name="createResumePage"),
    path('profilePage/',profilePage,name="profilePage"),
    path('addSkillPage/',addSkillPage,name="addSkillPage"),
    path('addEducation/',addEducation,name="addEducation"),
    path('addLanugage/',addLanugage,name="addLanugage"),
    path('LanguageListbyUser/',LanguageListbyUser,name="LanguageListbyUser"),
    path('LanguageEditbyUser/<str:myid>',LanguageEditbyUser,name="LanguageEditbyUser"),
    path('addSkillPage/',addSkillPage,name="addSkillPage"),
    path('skillListByUser/',skillListByUser,name="skillListByUser"),
    path('skillEditByUser/<str:myid>',skillEditByUser,name="skillEditByUser"),
    path('deleteSkillByUser/<str:myid>',deleteSkillByUser,name="deleteSkillByUser"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)