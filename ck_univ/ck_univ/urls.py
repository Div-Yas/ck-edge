"""ck_univ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('e_form',views.e_form,name='e_form'),
    path('enq_fetch',views.enq_fetch,name='enq_fetch'),
    path('enroll',views.enroll,name='enroll'),
    path('enroll_form/<int:id>',views.enroll_form,name='enroll_form'),
    path('enroll_fetch',views.enroll_fetch,name='enroll_fetch'),
    path('getid',views.getid,name='getid'),
    path('enqu',views.enqu,name='enqu'),
    path('enro',views.enro,name='enro'),
    path('update_enroll',views.update_enroll,name='update_enroll'),
    path('',views.user_login,name='user_login'),
    path('signout',views.signout,name='signout'),
    path('enrollment_form',views.enrollment_form,name='enrollment_form'),
    path('enq_delete',views.enq_delete,name='enq_delete'),
    path('edit_enroll',views.edit_enroll,name='edit_enroll'),
    path('update_enrollform',views.update_enrollform,name='update_enrollform'),
    path('update_enqform',views.update_enqform,name='update_enqform'),
    path('add_course',views.add_course,name='add_course'),
    path('addcour',views.addcour,name='addcour'),
    path('pendding',views.pendding,name='pendding'),
    path('price',views.price,name='price'),
    path('pendding_page/<int:id>',views.pendding_page ,name='pendding_page'),
    path('paydetail',views.paydetail ,name='paydetail'),
    path('enr_frm1/<int:id>',views.enr_frm1 ,name='enr_frm1'),
    path('History_enroll',views.History_enroll ,name='History_enroll'),
    path('receipt',views.receipt ,name='receipt'),
    path('chng_inactive',views.chng_inactive ,name='chng_inactive'),
    path('chng_active',views.chng_active ,name='chng_active'),
    path('status_fetch',views.status_fetch ,name='status_fetch'),
    path('addcourse_page',views.addcourse_page ,name='addcourse_page'),
    path('addcour_fetch',views.addcour_fetch ,name='addcour_fetch'),
    path('edit_addcourse',views.edit_addcourse ,name='edit_addcourse'),
    path('update_addcourse',views.update_addcourse ,name='update_addcourse'),
    path('delete_course',views.delete_course ,name='delete_course'),
    path('paydetailss',views.paydetailss ,name='paydetailss'),
    path('payying',views.payying ,name='payying'),
    path('qualification',views.qualification ,name='qualification'),
    path('add_quali',views.add_quali ,name='add_quali'),
    path('insert_quali',views.insert_quali ,name='insert_quali'),
    path('quali_fetch',views.quali_fetch ,name='quali_fetch'),
    path('edit_quali',views.edit_quali ,name='edit_quali'),
    path('delete_quali',views.delete_quali ,name='delete_quali'),
    path('update_quali',views.update_quali ,name='update_quali'),
    path('cal_month',views.cal_month ,name='cal_month'),
    #ghg
    path('fetch_course',views.fetch_course ,name='fetch_course'),
    path('fetch_qualification',views.fetch_qualification ,name='fetch_qualification'),
    path('fetch_location',views.fetch_location ,name='fetch_location'),
    path('enroll_fetch1',views.enroll_fetch1,name='enroll_fetch1'),
    path('demo',views.demo,name='demo'),
    path('file_upload',views.file_upload,name='file_upload'),

    #source
    path('source',views.sources,name='source'),
    path('addsource',views.addsource,name='addsource'),
    path('source_fetch',views.source_fetch,name='source_fetch'),
    path('editsource',views.editsource,name='editsource'),
    path('updatesource',views.updatesource,name='updatesource'),
    path('source_delete',views.source_delete,name='source_delete'),

    #location
    path('location',views.location,name='location'),
    path('addlocation',views.addlocation,name='addlocation'),
    path('loc_fetch',views.loc_fetch,name='loc_fetch'),
    path('editlocation',views.editlocation,name='editlocation'),
    path('updatelocation',views.updatelocation,name='updatelocation'),
    path('loc_delete',views.loc_delete,name='loc_delete'),


]
