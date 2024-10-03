from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate,login,logout
from myapp.models import ck_table,Rep_id,adcourse,paydetails,qualifications,locations_add,source,User
from django.db.models import Q
from operator import itemgetter
import io,csv
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
from datetime import date,timedelta,datetime
from dateutil.relativedelta import relativedelta
from num2words import num2words
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
# from django.utils.dateformat import DateFormat
# from django.utils.formats import get_format
# from django.views.generic.base import View
# import datetime
# from ck_univ.utils import render_to_pdf
# from django.core.mail import send_mail
# from django.template import loader
# import json

# Create your views here.
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username = username, password = password)
        userData=User.objects.get(username=username)
        request.session['role']=userData.role
        request.session['username']=userData.username
        if user is not None:
            login(request,user)
            if userData.role == "Admin" and user.is_superuser:
                return redirect('index')
            elif not user.is_superuser and userData.role == "Internal Audit":
                return redirect('enroll')
        else:
            return redirect('/')

    return render(request,'auth/login.html')

def signout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='/')
def index(request):
    return render(request,'auth/index.html')

@login_required(login_url='/')
def e_form(request):
    quali=qualifications.objects.values('qualification')
    location=locations_add.objects.values('loc_name')
    sources=source.objects.values('source_name')
    coursename=adcourse.objects.values('cname','id')
    return render(request,'auth/enq_form.html',{'coursename':coursename,'quali':quali,'location':location,'sources':sources})

@login_required(login_url='/')
def add_course(request):
    return render(request,'auth/addcourse.html')

@login_required(login_url='/')
def sources(request):
    return render(request,'auth/source.html')

@login_required(login_url='/')
def addsource(request):
    if request.method == "POST":
        data=source.objects.filter(source_name=request.POST['sour_name']).count()
        if data == 0:
           obj=source.objects.create(source_name=request.POST['sour_name'],status="Active",created_at=date.today())
           return JsonResponse({'status':'Success'})
        else:
           return JsonResponse({'status':'exist'})
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def source_fetch(request):
    a=source.objects.filter(status="Active").values('source_name','status','id')
    return JsonResponse(list(a),safe=False)

@login_required(login_url='/')
def editsource(request):
    id1=request.POST.get('id')
    obj = source.objects.get(id=id1)
    user = {'id':obj.id,'source_name':obj.source_name}
    data={'user':user}
    return JsonResponse(data)

@login_required(login_url='/')
def updatesource(request):
    try:
        id = request.POST.get('ids')
        data=source.objects.get(id=id)
        data.source_name=request.POST['sour_name1']
        data.created_at=date.today()
        data.save()
        return JsonResponse({'status':'Success'})
    except:
        return JsonResponse({'status':'failed'})

@login_required(login_url='/')
def source_delete(request):
    id = request.POST.get('id')
    source.objects.get(id=id).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)


@login_required(login_url='/')
def addlocation(request):
    if request.method == "POST":
        data=locations_add.objects.filter(loc_name=request.POST['loc']).count()
        if data == 0:
           obj=locations_add.objects.create(loc_name=request.POST['loc'],status="Active",created_at=date.today())
           return JsonResponse({'status':'Success'})
        else:
           return JsonResponse({'status':'exist'})
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def loc_fetch(request):
    a=locations_add.objects.filter(status="Active").values('loc_name','status','id')
    return JsonResponse(list(a),safe=False)

@login_required(login_url='/')
def editlocation(request):
    id1=request.POST.get('id')
    obj = locations_add.objects.get(id=id1)
    user = {'id':obj.id,'loc_name':obj.loc_name}
    data={'user':user}
    return JsonResponse(data)

@login_required(login_url='/')
def updatelocation(request):
    try:
        id = request.POST.get('ids')
        data=locations_add.objects.get(id=id)
        data.loc_name=request.POST['loc1']
        data.created_at=date.today()
        data.save()
        return JsonResponse({'status':'Success'})
    except:
        return JsonResponse({'status':'failed'})

@login_required(login_url='/')
def loc_delete(request):
    id = request.POST.get('id')
    locations_add.objects.get(id=id).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)

@login_required(login_url='/')
def location(request):
    return render(request,'auth/location.html')


@login_required(login_url='/')
def qualification(request):
    return render(request,'auth/qualification.html')

@login_required(login_url='/')
def add_quali(request):
    return render(request,'auth/add_qualification.html')

@login_required(login_url='/')
def insert_quali(request):
    if request.method == "POST":
        data=qualifications.objects.filter(qualification=request.POST['quali']).count()
        if data == 0:
           obj=qualifications.objects.create(qualification=request.POST['quali'],remark=request.POST['remark'],created_at=date.today())
           return JsonResponse({'status':'Success'})
        else:
           return JsonResponse({'status':'exist'})
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def quali_fetch(request):
    a=qualifications.objects.all().values('qualification','remark','id')
    return JsonResponse(list(a),safe=False)

@login_required(login_url='/')
def edit_quali(request):
    id1=request.POST.get('id')
    obj = qualifications.objects.get(id=id1)
    user = {'id':obj.id,'qualification':obj.qualification,'remark':obj.remark}
    data={'user':user}
    return JsonResponse(data)

@login_required(login_url='/')
def update_quali(request):
    try:
        id = request.POST.get('id')
        data=qualifications.objects.get(id=id)
        data.qualification=request.POST['quali']
        data.remark=request.POST['remark']
        data.created_at=date.today()
        data.save()
        return JsonResponse({'status':'Success'})
    except:
        return JsonResponse({'status':'failed'})

@login_required(login_url='/')
def delete_quali(request):
    id = request.POST.get('id')
    qualifications.objects.get(id=id).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)

@login_required(login_url='/')
def enroll(request):
    return render(request,'auth/enroll.html')

@login_required(login_url='/')
def enroll_form(request,id):
    a=ck_table.objects.select_related('acourse').filter(id=id).values('acourse_id__cduration','acourse_id__cprice','acourse_id__id','id','acourse_id__cname','Location','candid_name','email','education','comp_year','ph_num','al_ph_num','parent_name','dat','parent_ph_num','address','source')
    return render(request,'auth/enroll_form.html',{"a1":a})

@login_required(login_url='/')
def enq_fetch(request):
    a=ck_table.objects.select_related('acourse').filter(payment_type='').values('id','acourse_id__cname','Location','candid_name','education','comp_year','parent_name','ph_num','al_ph_num','parent_ph_num','email','address','source','dat')
    return JsonResponse(list(a),safe=False)

@login_required(login_url='/')
def enroll_fetch(request):
    chk_month= ck_table.objects.filter(payment_type='Monthly Payment')
    if chk_month :
        a=ck_table.objects.select_related('acourse').filter( ~Q(payment_type='' )).values('candid_no','id','acourse_id__cname','Location','candid_name','education','comp_year','parent_name','ph_num','al_ph_num','parent_ph_num','dat','email','address','source','payment_type','payment_mode','remark','nxt_month','status','blc_amnt')
        return JsonResponse(list(a),safe=False)
    else:
        return JsonResponse({'status':'no data'})

@login_required(login_url='/')
def enroll_fetch1(request):
    cour=request.POST.get('cour')
    quali=request.POST.get('quali')
    loc=request.POST.get('loc')
    chk_month= ck_table.objects.filter(payment_type='Monthly Payment')
    if chk_month :
        a=ck_table.objects.select_related('acourse').filter( ~Q(payment_type='' ),Q(acourse=cour ),Q(education=quali ),Q(Location=loc)).values('candid_no','id','acourse_id__cname','Location','candid_name','education','comp_year','parent_name','ph_num','al_ph_num','parent_ph_num','dat','email','address','source','payment_type','payment_mode','remark','nxt_month','status','blc_amnt')
        return JsonResponse(list(a),safe=False)
    else:
        return JsonResponse({'status':'no data'})

@login_required(login_url='/')
def getid(request):
    id1=request.POST.get('id1')
    obj = ck_table.objects.get(id=id1)
    user = {'id':obj.id,'amount':obj.amount}
    data={'user':user}
    return JsonResponse(data)

@login_required(login_url='/')
def enqu(request):
    value = request.POST.get('j2')
    ph_num = request.POST.get('f2')
    al_ph_num = request.POST.get('g2')
    parent_ph_num = request.POST.get('i2')
    try:
        validate_email(value)
        email=ck_table.objects.filter(Q(email=value) | Q(ph_num=ph_num)).count()
        cgst=adcourse.objects.get(id=request.POST.get('a2'))
        if email == 0:
            obj=ck_table.objects.create(acourse_id=request.POST.get('a2'),Location=request.POST.get('b2'),candid_name=request.POST.get('c2'),education=request.POST.get('d2'),comp_year=request.POST.get('e2'),parent_name=request.POST.get('h2'),ph_num=ph_num,al_ph_num=al_ph_num,parent_ph_num=parent_ph_num,email=value,address=request.POST.get('k2'),source=request.POST.get('l2'),cgst=cgst.cgst)
            msg='success'
        else:
            msg="email"
        return JsonResponse({'status':msg})
    except ValidationError as e:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def enro(request):
    value = request.POST.get('j2')
    t_date=date.today()
    h1= t_date+ relativedelta(months=1)
    discount_value=request.POST.get('txtstock')
    dis_price_value=request.POST.get('disprice1')
    ph_num = request.POST.get('f2')
    al_ph_num = request.POST.get('g2')
    parent_ph_num = request.POST.get('i2')
    try:
        validate_email(value)
        if discount_value!='' and dis_price_value!='':
            obj=ck_table.objects.create(acourse_id=request.POST.get('a2'),Location=request.POST.get('b2'),candid_name=request.POST.get('c2'),education=request.POST.get('d2'),comp_year=request.POST.get('e2'),parent_name=request.POST.get('h2'),ph_num=ph_num,al_ph_num=al_ph_num,parent_ph_num=parent_ph_num,email=value,address=request.POST.get('k2'),source=request.POST.get('l2'),payment_type=request.POST.get('m2'),payment_mode=request.POST.get('n2'),remark=request.POST.get('p2'),amount=request.POST.get('o2'),blc_amnt=request.POST.get('r2'),price=request.POST.get('q2'),nxt_month=h1,status='Active',dis_price=request.POST.get('disprice1'),discount=request.POST.get('txtstock'),final_amount=request.POST.get('final_p'),gst_amount=request.POST.get('total_gst'),gst_p=request.POST.get('gst_m'),cgst=request.POST.get('cgst'),candid_no=request.POST.get('candid_no'))
            obj.save()
            date_det = date.today()
            details = ck_table.objects.latest('id')
            ckid=details.id
            data = paydetails.objects.create(candid_name=request.POST.get('c2'), amount= request.POST.get('o2'),dat= date_det,ckid=ckid,discount=request.POST.get('txtstock'),final_amount=request.POST.get('final_p'),gst_p=request.POST.get('gst_m'))
        else:
            obj=ck_table.objects.create(acourse_id=request.POST.get('a2'),Location=request.POST.get('b2'),candid_name=request.POST.get('c2'),education=request.POST.get('d2'),comp_year=request.POST.get('e2'),parent_name=request.POST.get('h2'),ph_num=ph_num,al_ph_num=al_ph_num,parent_ph_num=parent_ph_num,email=value,address=request.POST.get('k2'),source=request.POST.get('l2'),payment_type=request.POST.get('m2'),payment_mode=request.POST.get('n2'),remark=request.POST.get('p2'),amount=request.POST.get('o2'),blc_amnt=request.POST.get('r2'),price=request.POST.get('q2'),nxt_month=h1,status='Active',final_amount=request.POST.get('final_p'),gst_amount=request.POST.get('total_gst'),gst_p=request.POST.get('gst_m'),cgst=request.POST.get('cgst'),candid_no=request.POST.get('candid_no'))
            obj.save()
            date_det = date.today()
            details = ck_table.objects.latest('id')
            ckid=details.id
            data = paydetails.objects.create(candid_name=request.POST.get('c2'), amount= request.POST.get('o2'),dat= date_det,ckid=ckid,final_amount=request.POST.get('final_p'),gst_p=request.POST.get('gst_m'))
        id1=ck_table.objects.get(email=request.POST.get('j2'))
        c=request.POST.get('a2')
        items=ck_table.objects.get(id=id1.id)
        R_id=Rep_id.objects.get(id=1)
        today = date.today()
        if today==R_id.dat:
            bb=int(R_id.receipt_id)+1
            num=str(bb).zfill(4)
            R_id.receipt_id=int(R_id.receipt_id)+1
            R_id.dat=today
            R_id.save()
        else:
            R_id.receipt_id=0
            R_id.save()
            bb=int(R_id.receipt_id)+1
            num=str(bb).zfill(4)
            R_id.receipt_id=+1
            R_id.dat=today
            R_id.save()
        aa=today.strftime("%d%m%y")
        r_id=aa +''+ num
        items.receipt_id=r_id
        items.save()
        if items:
            cust_email= items.email
            items=ck_table.objects.get(id=id1.id)
            course=adcourse.objects.get(id=c)
            paid_amt=items.final_amount
            paid_amt1=num2words(paid_amt)
            if items.payment_type == 'Full Payment':
              a="Full Payment"
            else:
              a=paydetails.objects.filter(ckid=id1.id).count()
            if items.discount is None:
               grant_tot=float(items.price)+float(items.gst_amount)
               discount=items.discount
               dis_price="0.00"
            else:
              grant_tot=float(items.dis_price)+float(items.gst_amount)
              discount=items.discount
              dis_price=items.dis_price
            # print(grant_tot)
            gst_amt=float(items.gst_amount)/2
            price_dis=float(course.cprice)-float(dis_price)
            data = {
                'id':items.id,
                'course_name' :course.cname,
                'course_dur':course.cduration,
                'course_price' :course.cprice,
                'Location' :items.Location,
                'candid_name' :items.candid_name,
                'education' :items.education,
                'ph_num' :items.ph_num,
                'parent_ph_num' :items.parent_ph_num,
                'email' :items.email,
                'bal_amt':items.blc_amnt,
                'address' :items.address,
                'amount' :items.amount,
                'payment_type':items.payment_type,
                'receipt_id':items.receipt_id,
                'date':items.dat,
                'paid_amt':str(paid_amt1).title(),
                'GST':items.cgst,
                'final_price':items.final_amount,
                'gst_price':items.gst_p,
                'month':str(a),
                'dis_price':dis_price,
                'discount':discount,
                'grant_tot':grant_tot,
                'gst_amt':gst_amt,
                'price_dis':price_dis,
                'candid_no':items.candid_no

            }
            template=get_template('auth/receipt.html')
            html  = template.render(data)
            result = BytesIO()
            pdf1 = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            pdf = result.getvalue()
            if a==1:
                k=str(a)+'st'
            elif a==2:
                k=str(a)+'nd'
            elif a==3:
                k=str(a)+'rd'
            else:
                k=str(a)+'th'
            if(items.payment_type == 'Full Payment'):
              email = EmailMessage('Hello , Successfully Register your course and paid your full payment in HEPL', 'Here your Receipt', 'zevonstore4@gmail.com', [cust_email])
            else:
                email = EmailMessage('Hello , Successfully Register your course and '+k+' Month fees is Paid in HEPL', 'Here your Receipt', 'zevonstore4@gmail.com', [cust_email])
            email.attach('Receipt.pdf',pdf)
            email.send()
            msg="success"
        return JsonResponse({'status':msg})
    except ValidationError as e:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def enrollment_form(request):
    quali=qualifications.objects.all()
    coursename=adcourse.objects.all()
    location=locations_add.objects.all()
    sources=source.objects.all()
    return render(request,"auth/enrollment_form.html",{'coursename':coursename,'quali':quali,'location':location,'sources':sources})

@login_required(login_url='/')
def update_enroll(request):
    discount_value=request.POST.get('txtstock')
    dis_price_value=request.POST.get('disprice1')
    if discount_value!='' and dis_price_value!='':
        t_date=date.today()
        h1= t_date+ relativedelta(months=1)
        id1=request.POST.get('id')
        obj=ck_table.objects.get(id=id1)
        obj.payment_type=request.POST.get('m2')
        obj.payment_mode=request.POST.get('n2')
        obj.remark=request.POST.get('p2')
        obj.amount=request.POST.get('o2')
        obj.blc_amnt=request.POST.get('r2')
        obj.price=request.POST.get('q2')
        obj.dis_price=request.POST.get('disprice1')
        obj.discount=request.POST.get('txtstock')
        obj.final_amount=request.POST.get('final_p')
        obj.gst_amount=request.POST.get('total_gst')
        obj.gst_p=request.POST.get('gst_amt')
        obj.nxt_month=h1
        obj.candid_no=request.POST.get('candid_no')
        obj.status='Active'
        obj.save()
        date_det = date.today()
        data = paydetails.objects.create(candid_name=obj.candid_name, amount= request.POST['o2'],dat= date_det,ckid=obj.id,discount=request.POST.get('txtstock'),final_amount=request.POST.get('final_p'),gst_p=request.POST.get('gst_amt'))
    else:
        t_date=date.today()
        h1= t_date+ relativedelta(months=1)
        id1=request.POST.get('id')
        obj=ck_table.objects.get(id=id1)
        obj.payment_type=request.POST.get('m2')
        obj.payment_mode=request.POST.get('n2')
        obj.remark=request.POST.get('p2')
        obj.amount=request.POST.get('o2')
        obj.blc_amnt=request.POST.get('r2')
        obj.price=request.POST.get('q2')
        obj.final_amount=request.POST.get('final_p')
        obj.gst_amount=request.POST.get('total_gst')
        obj.gst_p=request.POST.get('gst_amt')
        obj.nxt_month=h1
        obj.candid_no=request.POST.get('candid_no')
        obj.status='Active'
        obj.save()
        date_det = date.today()
        data = paydetails.objects.create(candid_name=obj.candid_name,amount= request.POST['o2'],dat= date_det,ckid=obj.id,final_amount=request.POST.get('final_p'),gst_p=request.POST.get('gst_amt'))
    items=ck_table.objects.get(id=id1)
    c=items.acourse_id
    R_id=Rep_id.objects.get(id=1)
    today = date.today()
    if today==R_id.dat:
        bb=int(R_id.receipt_id)+1
        num=str(bb).zfill(4)
        R_id.receipt_id=int(R_id.receipt_id)+1
        R_id.dat=today
        R_id.save()
    else:
        R_id.receipt_id=0
        R_id.save()
        bb=int(R_id.receipt_id)+1
        num=str(bb).zfill(4)
        R_id.receipt_id=+1
        R_id.dat=today
        R_id.save()
    aa=today.strftime("%d%m%y")
    r_id=aa +''+ num
    items.receipt_id=r_id
    items.save()
    if items:
            cust_email= items.email
            items=ck_table.objects.get(id=id1)
            paid_amt=items.final_amount
            paid_amt1=num2words(paid_amt)
            course=adcourse.objects.get(id=c)
            if items.payment_type == 'Full Payment':
              a="Full Payment"
            else:
              a=paydetails.objects.filter(ckid=id1).count()
            if items.discount is None:
               grant_tot=float(items.price)+float(items.gst_amount)
               discount=items.discount
               dis_price="0.00"
            else:
              grant_tot=float(items.dis_price)+float(items.gst_amount)
              discount=items.discount
              dis_price=items.dis_price
            # print(grant_tot)
            gst_amt=float(items.gst_amount)/2
            price_dis=float(course.cprice)-float(dis_price)
            data = {
                'id':items.id,
                'course_name' :course.cname,
                'course_dur':course.cduration,
                'course_price' :course.cprice,
                'Location' :items.Location,
                'candid_name' :items.candid_name,
                'education' :items.education,
                'ph_num' :items.ph_num,
                'parent_ph_num' :items.parent_ph_num,
                'email' :items.email,
                'address' :items.address,
                'amount' :items.amount,
                'payment_type':items.payment_type,
                'receipt_id':items.receipt_id,
                'date':items.dat,
                'paid_amt':str(paid_amt1).title(),
                'bal_amt':items.blc_amnt,
                'GST':items.cgst,
                'final_price':items.final_amount,
                'gst_price':items.gst_p,
                'month':str(a),
                'dis_price':dis_price,
                'discount':discount,
                'grant_tot':grant_tot,
                'gst_amt':gst_amt,
                'price_dis':price_dis,
                'candid_no':items.candid_no

            }
            template=get_template('auth/receipt.html')
            html  = template.render(data)
            result = BytesIO()
            pdf1 = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            pdf = result.getvalue()
            pay=request.POST.get('m2')
            if a==1:
                k=str(a)+'st'
            elif a==2:
                k=str(a)+'nd'
            elif a==3:
                k=str(a)+'rd'
            else:
                k=str(a)+'th'
            if(pay == 'Full Payment'):
               email = EmailMessage('Hello , Successfully Register your course and paid your full payment in HEPL', 'Here your Receipt', 'zevonstore4@gmail.com', [cust_email])
            else:
               email = EmailMessage('Hello , Successfully Register your course and '+k+' Month fees is Paid in HEPL', 'Here your Receipt','zevonstore4@gmail.com', [cust_email])
            email.attach('Receipt.pdf',pdf)
            email.send()
    return JsonResponse({'status':'Success'})

@login_required(login_url='/')
def enq_delete(request):
        id = request.POST.get('id')
        ck_table.objects.get(id=id).delete()
        data = {
            'deleted': True

        }
        return JsonResponse(data)

@login_required(login_url='/')
def edit_enroll(request):
    id1=request.POST.get('id')
    obj = ck_table.objects.get(id=id1)
    data=obj.acourse_id
    acourse = adcourse.objects.get(id=data)
    coursename = adcourse.objects.values('cname','id')
    list_val=list(map(itemgetter('cname'),coursename))
    list_id=list(map(itemgetter('id'),coursename))
    user = {'id':obj.id,'course_name':acourse.cname,'course_id':acourse.id,'Location':obj.Location,'education':obj.education,'comp_year':obj.comp_year,'parent_name':obj.parent_name,'ph_num':obj.ph_num,'al_ph_num':obj.al_ph_num,'parent_ph_num':obj.parent_ph_num,'email':obj.email,'address':obj.address,'source':obj.source,'payment_type':obj.payment_type,'payment_mode':obj.payment_mode,'amount':obj.amount,'remark':obj.remark,'candid_name':obj.candid_name,'candid_no':obj.candid_no}
    quali=qualifications.objects.values('qualification')
    list_quali=list(map(itemgetter('qualification'),quali))
    location=locations_add.objects.values('loc_name')
    list_loc=list(map(itemgetter('loc_name'),location))
    sources=source.objects.values('source_name')
    list_sources=list(map(itemgetter('source_name'),sources))
    data={'user':user,'list_val':list_val,'list_id':list_id,'list_quali':list_quali,'list_loc':list_loc,'list_sources':list_sources}
    return JsonResponse(data)

@login_required(login_url='/')
def update_enrollform(request):
    try:
        id = request.POST['id']
        data=ck_table.objects.get(id=id)
        data.course_name=request.POST['a2']
        data.Location=request.POST['b2']
        data.education=request.POST['d2']
        data.comp_year=request.POST['e2']
        data.parent_name=request.POST['h2']
        data.ph_num=request.POST['f2']
        data.al_ph_num=request.POST['g2']
        data.parent_ph_num=request.POST['i2']
        data.email=request.POST['j2']
        data.address=request.POST['k2']
        data.source=request.POST['l2']
        data.payment_type=request.POST['m2']
        data.payment_mode=request.POST['n2']
        data.remark=request.POST['p2']
        data.amount=request.POST['o2']
        data.candid_name=request.POST['c2']
        data.candid_no=request.POST['candid_no']
        data.save()
        return JsonResponse({'status':'Success', 'msg': 'save successfully'})
    except:
        return JsonResponse({'status':'failed', 'msg': 'save successfully'})

@login_required(login_url='/')
def update_enqform(request):
    try:
        id=request.POST['id']
        data=ck_table.objects.get(id=id)
        data.acourse_id=request.POST['a2']
        data.Location=request.POST['b2']
        data.education=request.POST['d2']
        data.comp_year=request.POST['e2']
        data.parent_name=request.POST['h2']
        data.ph_num=request.POST['f2']
        data.al_ph_num=request.POST['g2']
        data.parent_ph_num=request.POST['i2']
        data.email=request.POST['j2']
        data.address=request.POST['k2']
        data.source=request.POST['l2']
        data.candid_name=request.POST['c2']
        data.save()
        return JsonResponse({'status':'Success', 'msg': 'save successfully'})
    except:
        return JsonResponse({'status':'failed', 'msg': 'save successfully'})

@login_required(login_url='/')
def addcourse_page(request):
    return render(request,'auth/addcourse_page.html')

@login_required(login_url='/')
def addcour(request):
    if request.method == "POST":
        obj=adcourse.objects.create(cname=request.POST['c2'],cdetails=request.POST['d2'],cduration=request.POST['e2'],cprice=request.POST['f2'],cgst=request.POST['g2'])
        return JsonResponse({'status':'Success'})
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def addcour_fetch(request):
    a=adcourse.objects.all().values('cname','cduration','cprice','cdetails','id','cgst')
    return JsonResponse(list(a),safe=False)

@login_required(login_url='/')
def edit_addcourse(request):
    id1=request.POST.get('id')
    obj = adcourse.objects.get(id=id1)
    coursename = adcourse.objects.values('cduration','id')
    list_val=list(map(itemgetter('cduration'),coursename))
    list_id=list(map(itemgetter('id'),coursename))
    user = {'id':obj.id,'course_name':obj.cname,'cdetails':obj.cdetails,'cduration':obj.cduration,'cprice':obj.cprice,'cgst':obj.cgst}
    data={'user':user,'list_val':list_val,'list_id':list_id}
    return JsonResponse(data)

@login_required(login_url='/')
def update_addcourse(request):
    try:
        id = request.POST.get('id')
        data=adcourse.objects.get(id=id)
        data.cname=request.POST['a2']
        data.cdetails=request.POST['b2']
        data.cprice=request.POST['c2']
        data.cduration=request.POST['d2']
        data.cgst=request.POST['g2']
        data.save()
        return JsonResponse({'status':'Success', 'msg': 'save successfully'})
    except:
        return JsonResponse({'status':'failed', 'msg': 'save successfully'})

@login_required(login_url='/')
def delete_course(request):
        id = request.POST.get('id')
        adcourse.objects.get(id=id).delete()
        data = {
            'deleted': True

        }
        return JsonResponse(data)

@login_required(login_url='/')
def price(request):
    if request.method == "POST":
        id1=request.POST.get('id')
        a=adcourse.objects.get(id=id1)
        user = {'cprice':a.cprice,'cduration':a.cduration,'cgst':a.cgst}
        data={'user':user}
        return JsonResponse(data)
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def pendding_page(request,id):
    a=ck_table.objects.get(id=id)
    if a.discount is None:
       amt=str(a.price)
    else:
       amt=str(a.dis_price)
    gst=str(a.gst_amount)
    if isinstance(amt,str):
      if '.' in amt:
          amt1=float(amt)
      else:
          amt1=int(amt)
    if isinstance(gst,str):
      if '.' in gst:
          gst1=float(gst)
      else:
          gst1=int(gst)
    total=amt1+gst1
    cor=a.acourse_id
    duration=adcourse.objects.get(id=cor)
    duration_month=duration.cduration
    return render(request,'auth/pending.html',{"a1":a,"a2":duration_month,'total':total,'gst_p':gst1,"dur":duration})

@login_required(login_url='/')
def pendding(request):
    t_date=date.today()
    h1= t_date+ relativedelta(months=1)
    id1=request.POST.get('id')
    obj=ck_table.objects.get(id=id1)
    obj.payment_type=request.POST.get('m2')
    obj.payment_mode=request.POST.get('n2')
    obj.amount=request.POST.get('o2')
    obj.blc_amnt=request.POST.get('r2')
    obj.gst_p=request.POST.get('gst_amt')
    obj.final_amount=request.POST.get('final_p')
    obj.nxt_month=h1
    obj.save()
    name = obj.candid_name
    amt = obj.amount
    ckid = id1
    date_det = date.today()
    paydetails.objects.create(candid_name=name,amount=amt,dat= date_det,ckid=ckid,gst_p=request.POST.get('gst_amt'),final_amount=request.POST.get('final_p'))
    items=ck_table.objects.get(id=id1)
    R_id=Rep_id.objects.get(id=1)
    today = date.today()
    if today==R_id.dat:
        bb=int(R_id.receipt_id)+1
        num=str(bb).zfill(4)
        R_id.receipt_id=int(R_id.receipt_id)+1
        R_id.dat=today
        R_id.save()
    else:
        R_id.receipt_id=0
        R_id.save()
        bb=int(R_id.receipt_id)+1
        num=str(bb).zfill(4)
        R_id.receipt_id=+1
        R_id.dat=today
        R_id.save()
    aa=today.strftime("%d%m%y")
    r_id=aa +''+ num
    items.receipt_id=r_id
    items.save()
    if items:
            cust_email= items.email
            items=ck_table.objects.get(id=id1)
            course=adcourse.objects.get(id=items.acourse_id)
            paid_amt=items.final_amount
            paid_amt1=num2words(paid_amt)
            if items.payment_type == 'Full Payment':
              a="Full Payment"
            else:
              a=paydetails.objects.filter(ckid=id1).count()
            if items.discount is None:
               grant_tot=float(items.price)+float(items.gst_amount)
               discount=items.discount
               dis_price="0.00"
            else:
              grant_tot=float(items.dis_price)+float(items.gst_amount)
              discount=items.discount
              dis_price=items.dis_price
            # print(grant_tot)
            gst_amt=float(items.gst_amount)/2
            price_dis=float(course.cprice)-float(dis_price)
            data = {
                'id':items.id,
                'course_name':course.cname,
                'course_dur':course.cduration,
                'course_price' :course.cprice,
                'Location' :items.Location,
                'candid_name' :items.candid_name,
                'education' :items.education,
                'ph_num' :items.ph_num,
                'parent_ph_num' :items.parent_ph_num,
                'email' :items.email,
                'address' :items.address,
                'amount' :items.amount,
                'payment_type':items.payment_type,
                'receipt_id':items.receipt_id,
                'date':date.today(),
                'paid_amt':str(paid_amt1).title(),
                'GST':items.cgst,
                'final_price':items.final_amount,
                'gst_price':items.gst_p,
                'bal_amt':items.blc_amnt,
                'month':str(a),
                'dis_price':dis_price,
                'discount':discount,
                'grant_tot':grant_tot,
                'gst_amt':gst_amt,
                'price_dis':price_dis,
                'candid_no':items.candid_no

                }
            template=get_template('auth/receipt.html')
            html  = template.render(data)
            result = BytesIO()
            pdf1 = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            pdf = result.getvalue()
            if a==1:
                k=str(a)+'st'
            elif a==2:
                k=str(a)+'nd'
            elif a==3:
                k=str(a)+'rd'
            else:
                k=str(a)+'th'
            if(items.payment_type == 'Full Payment'):
              email = EmailMessage('Hello , Successfully  paid your full payment in HEPL', 'Here your Receipt', 'zevonstore4@gmail.com', [cust_email])
            else:
                email = EmailMessage('Hello , Successfully  paid your '+k+' Month fees  in HEPL', 'Here your Receipt', 'zevonstore4@gmail.com', [cust_email])
            email.attach('Receipt.pdf',pdf)
            email.send()
            return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'fail'})

@login_required(login_url='/')
def paydetail(request):
    return render(request,'auth/paydetails.html')

@login_required(login_url='/')
def enr_frm1(request,id):
   data=paydetails.objects.filter(ckid=id)
   return render(request,'auth/paydetails.html',{'val':data})

@login_required(login_url='/')
def History_enroll(request):
    id1=request.POST.get('id')
    data1=paydetails.objects.filter(ckid=id1).count()
    if data1 !=0 :
        obj=ck_table.objects.get(id=id1)
        obj1=paydetails.objects.filter(ckid=id1).values('final_amount','dat')
        user = {'id':obj.id,'candid_name':obj.candid_name,'blc_amnt':obj.blc_amnt,'dis_price':obj.dis_price,'discount':obj.discount }
        table=""
        i=1
        for pay in obj1:
            j=str(i)
            table+='''<tr>\
                     <td id="paid">'''+j+'''</td>\
                     <td id="paid">'''+pay['final_amount']+'''</td>\
                     <td id="date">'''+str(pay['dat'])+'''</td>\
                    </tr>'''
            k=int(i)
            i=k+1
        user1 = {'pay':table}
        if obj.discount:
            msg='valid'
        else:
            msg='invalid'
        msg1='success'
    else:
        user=''
        user1=''
        msg=''
        msg1='failed'
    data={'user':user,'user1':user1,'msg':msg,'msg1':msg1}
    return JsonResponse(data)

@login_required(login_url='/')
def receipt(request):
    return render(request,'auth/receipt.html')

@login_required(login_url='/')
def chng_inactive(request):
    today=date.today()
    ids=request.POST.get('id')
    set_status=ck_table.objects.get(id=ids)
    set_status.status='Inactive'
    set_status.inactive_dat=today
    set_status.save()
    return JsonResponse({'status':'success'})

@login_required(login_url='/')
def chng_active(request):
    today=date.today()
    ids=request.POST.get('id')
    set_status=ck_table.objects.get(id=ids)
    set_status.status='Active'
    set_status.save()
    return JsonResponse({'status':'success'})

@login_required(login_url='/')
def status_fetch(request):
    ids=request.POST.get('id')
    obj=ck_table.objects.get(id=ids)
    user = {'id':obj.id,'candid_name':obj.candid_name,'inactive_dat':obj.inactive_dat}
    data={'user':user}
    return JsonResponse(data)

@login_required(login_url='/')
def paydetailss(request):
    ids=request.POST.get('id')
    x1=request.POST.get('x')
    y1=request.POST.get('y')
    a=ck_table.objects.get(id=ids)
    gst_val=adcourse.objects.get(id=a.acourse_id)
    a1=a.cgst
    user = {'x1':x1,"y1":y1,"gst_val":a1,"amt":gst_val.cprice,"dur":gst_val.cduration}
    data={'user':user}
    return JsonResponse(data,safe=False)

@login_required(login_url='/')
def payying(request):
    x1=request.POST.get('x')
    y1=request.POST.get('y')
    g=request.POST.get('ids1')
    gst_val=adcourse.objects.get(id=g)
    a=gst_val.cgst
    user = {'x1':x1,"y1":y1,"gst_val":a,"amt":gst_val.cprice}
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    email=ck_table.objects.filter(Q(email=email) | Q(ph_num=phno)).count()
    if email == 0 :
        msg="success"
    else:
        msg="email"
    data={'user':user,'status':msg}
    return JsonResponse(data)

@login_required(login_url='/')
def cal_month(request):
    ids=request.POST.get('id')
    a=paydetails.objects.filter(ckid=ids).count()+1
    data={'a':a}
    return JsonResponse(data)

@login_required(login_url='/')
def fetch_course(request):
    data=ck_table.objects.values('acourse')
    course=adcourse.objects.filter(id__in=data).values('cname','id')
    res=list(map(itemgetter('cname'),course))
    res1=list(map(itemgetter('id'),course))
    value=set(res)
    value1=set(res1)
    user={'value':list(value),'value1':list(value1)}
    return JsonResponse(user,safe=False)

@login_required(login_url='/')
def fetch_qualification(request):
    cour=request.POST.get('cour')
    data=ck_table.objects.filter(~Q(payment_type=''),Q(acourse=cour)).values('education')
    res=list(map(itemgetter('education'),data))
    value=set(res)
    return JsonResponse(list(value),safe=False)

@login_required(login_url='/')
def fetch_location(request):
    cour=request.POST.get('cour')
    quali=request.POST.get('quali')
    data=ck_table.objects.filter(~Q(payment_type=''),acourse=cour,education=quali).values('Location')
    res=list(map(itemgetter('Location'),data))
    value=set(res)
    return JsonResponse(list(value),safe=False)

@login_required(login_url='/')
def demo(request):
    return render(request,'auth/demo.html')

@login_required(login_url='/')
def file_upload(request):
    paramFile = io.TextIOWrapper(request.FILES['file1'].file)
    portfolio1 = csv.DictReader(paramFile)
    list_of_dict = list(portfolio1)
    dict_from_csv = dict(list_of_dict[0])
    list_of_column_names = list(dict_from_csv.keys())
    print("List of column names : ",
          list_of_column_names)
    arr=[]
    for row in list_of_dict:
        cname=row['candid_name']
        loc=row['Location']
        education=row['education']
        phone_number=row['ph_num']
        email=row['email']
        course=row['course']
        comp_year=row['comp_year']
        email1=ck_table.objects.filter(Q(email=row['email']) | Q(ph_num=row['ph_num'])).count()
        if phone_number == 'null' or len(phone_number) != 10 or phone_number == '':
           returnmsg = "Phone Number"
        elif loc == 'null' or loc == '':
           returnmsg = "location"
        elif education == 'null' or education == '':
           returnmsg = "Gender"
        elif cname =='null' or cname == '':
           returnmsg = "Name"
        elif '@' not in email or '.' not in email or email == 'null' or email == '':
           returnmsg = "Email"
        elif course == 'null' or course == '':
           returnmsg = "Course"
        elif comp_year == 'null' or comp_year == '':
           returnmsg = "Compeleted_year"
        elif email1 !=0:
           returnmsg = "Exist_Email_or_Phone"
        else:
           returnmsg = "Success"
        arr.append(returnmsg)
    val=set(arr)
    try:
        array=list(val)
        b=array.remove("Success")
        if not b:
            for row in list_of_dict:
                cgst=adcourse.objects.get(cname=row['course'])
                obj=ck_table.objects.create(acourse_id=cgst.id,Location=row['Location'],candid_name=row['candid_name'],education=row['education'],comp_year=row['comp_year'],parent_name=row['parent_name'],ph_num=row['ph_num'],al_ph_num=row['al_ph_num'],parent_ph_num=row['parent_ph_num'],email=row['email'],address=row['address'],source=row['source'],cgst=cgst.cgst)
            val=set(arr)
        else:
            val=set(arr)
        return JsonResponse({"Status":list(val)})
    except:
        return JsonResponse({"Status":list(val)})