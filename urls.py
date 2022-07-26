from django.conf.urls import url
from django.contrib import admin
from Cyber_Admins import views as admin_view
from Cyber_Users import views as user_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', user_view.Login, name='Login'),
    url(r'^Register/$', user_view.SignUp, name='Register'),
    url(r'^AddData/$', user_view.AddData, name='AddData'),
    url(r'^DataAnalysis/$', user_view.DataAnalysis, name='DataAnalysis'),
    url(r'^MalwareDataAnalysis/$', user_view.MalwareDataAnalysis,
        name='MalwareDataAnalysis'),
    url(r'^UnMalwareDataAnalysis/$', user_view.UnMalwareDataAnalysis,
        name='UnMalwareDataAnalysis'),
    url(r'^BreachAnalysis/$', user_view.BreachAnalysis,
        name='BreachAnalysis'),
    url(r'GUIDataAnalysis/(?P<chart_type>\w+)',
        user_view.GUIDataAnalysis, name="GUIDataAnalysis"),

    url(r'^AdminLogin/$', admin_view.AdminLogin, name='AdminLogin'),
    url(r'^UserDetails/$', admin_view.UserDetails, name='UserDetails'),
    url(r'^Analysis/$', admin_view.Analysis, name='Analysis'),
]
