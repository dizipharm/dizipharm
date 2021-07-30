from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from tablib import Dataset
from .resources import PersonResource
from .models import bulk_upload
from .models import bulkdata

import requests
from . forms import *
from . models import *
import json
# Create your views here.

# Dashboard for manufacturer result showing view

def dashboardview(request):
    result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
    # return render(request,'dashboard.html')
    return render(request,'dashboard.html',{'result':result, 'res_token':request.session['email'] or ''})

def base_admin_dashboardview(request):
    result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
    # return render(request,'dashboard.html')
    return render(request,'base_admin_dashboard.html',{ 'result':result, 'res_token':request.session['email'] or ''})

# def base_operator_dashboardview(request):
#     result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
#     # return render(request,'dashboard.html')
#     return render(request,'base_operator_dashboard.html',{ 'result':result, 'res_token':request.session['email'] or ''})

# Dashboard1 for operator view
# def dashboardoperatorview(request):
#     result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
#     return render(request,'operator_dashboard.html',{ 'result':result,'res_token':request.session['email'] or ''})

# Dashboard2 for manager view
# def dashboardmanagerview(request):
#     result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
#     # result = requests.get('http://3.237.20.101:8000/TpUsers/').json()
#     return render(request,'manager_dashboard.html',{ 'result':result,'res_token':request.session['email'] or ''})

# Dashboard3 for executive view
# def dashboardexecutiveview(request):
#     result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
#     # result = requests.get('http://3.237.20.101:8000/TpUsers/').json()
#     return render(request,'executive_dashboard.html',{ 'result':result,'res_token':request.session['email'] or ''})



def popupview(request):
    pass
    return render(request,'popup.html')

def transactionformview(request):
    pass
    return render(request,'transactionform.html')

def maps_view(request):
    result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
    return render(request,'map.html',{'result':result})

# User Profile view
def user_profileview(request):
    pass
    # return render(request, 'user_profile.html')
    return render(request,'user_profile.html',{'res_token':request.session['email'] or ''})
    # return render(request,'user_profile.html')

def operatordashboard(request):
    pass
    return render(request,'operatordashboard.html',{'res_token':request.session['email'] or ''})

# Accounts view
def accountsview(request):
    pass
    return render(request,'accounts.html')

# Roles view
def rolesview(request):
    pass
    return render(request,'roles.html')

# Permissions view
def permissionsview(request):
    pass
    return render(request,'permissions.html')

# Licence view
def licenceview(request):
    pass
    return render(request,'licence.html')


# Manufacturer details getting from manufacturer api view
def manufacturer_order_details_view(request):
    # import  pdb;pdb.set_trace()
    result_old=requests.get('http://18.207.255.94:8000/manufacturer_drug/').json()
    result=[]
    for row in result_old:
        if row['em_status']=='HandoffToLSP':
            result.append(row)

    return render(request,'manufacturer_order_details.html',{'result':result,'res_token':request.session['email'] or ''})

 # Manufacturer details Showing api view
def manufacturer_order_details_edit_view(request,id):
    result=requests.get('http://18.207.255.94:8000/manufacturer_drug/'+str(id)+'/').json()
    return render(request,'manufacturer_order_details_edit.html',{'result':result,'res_token':request.session['email'] or ''})

# Manufacturer details Submitting from manufacturer api to trace form api view

# def manufacturer_order_update(request):
#     # import pdb; pdb.set_trace()
#     if request.method=="POST":
#         # serial_number=request.POST.get('serial_number')
#         # brand_name=request.POST.get('brand_name')
#         # product_name=request.POST.get('product_name')
#         # mfg_date=request.POST.get('mfg_date')
#         # manufacturer_name=request.POST.get('manufacturer_name')
#         # expiry_date=request.POST.get('expiry_date')
#         # manufacturer_gln=request.POST.get('manufacturer_gln')
#         # product_description=request.POST.get('product_description')
#         # strength=request.POST.get('strength')
#         # batch_number=request.POST.get('batch_number')
#         # patient_instruction=request.POST.get('patient_instruction')
#         # product_code_gtin=request.POST.get('product_code_gtin')
#         # serial_number=request.POST.get('serial_number')
#         # product_ndc=request.POST.get('product_ndc')
#         # product_code_type=request.POST.get('product_code_type')
#         # user_id=request.POST.get('user_id')
#         import pdb; pdb.set_trace()
#         sscc=request.POST.get('sscc')
#         package_name=request.POST.get('package_name')
#         inner_content=request.POST.get('inner_content')
#         pallet_no=request.POST.get('pallet_no')
#         package_level=request.POST.get('package_level')
#         packaging_dimensions=request.POST.get('packaging_dimensions')
#
#         # data1={'product_name': product_name,'mfg_date': mfg_date,'serial_number':serial_number,'manufacturer_gln':manufacturer_gln,'manufacturer_name':manufacturer_name,'expiry_date': expiry_date,'product_description':product_description,'strength':strength,'batch_number':batch_number,'patient_instruction':patient_instruction,'product_code_gtin':product_code_gtin,'product_ndc':product_ndc,'product_code_type':product_code_type,'user':'http://3.237.20.101:8000/addusers/'+str(user_id)+'/'}
#         # result=requests.post('http://3.237.20.101:8000/product/',data1).json()
#
#         # data2={'sscc': sscc,'inner_content':inner_content,'pallet_no':pallet_no,'package_level':package_level,'package_name':package_name,'packaging_dimensions':packaging_dimensions,'product':result['url']}
#         data2={'sscc': sscc,'inner_content':inner_content,'pallet_no':pallet_no,'package_level':package_level,'package_name':package_name,'packaging_dimensions':packaging_dimensions}
#         result1=requests.post('http://3.237.20.101:8000/packaging/',data2)
#         return redirect("/manufacturer_order_details")
#     else:
#         return render(request,'manufacturer_order_details.html')


def manufacturer_order_update(request):
    # import pdb; pdb.set_trace()
    if request.method=="POST":
        # serial_number=request.POST.get('serial_number')
        # brand_name=request.POST.get('brand_name')
        #product elements
        product_name=request.POST.get('product_name')
        mfg_date=request.POST.get('mfg_date')
        expiry_date=request.POST.get('expiry_date')
        product_description=request.POST.get('product_description')
        strength=request.POST.get('strength')
        batch_number=request.POST.get('batch_number')
        patient_instruction=request.POST.get('patient_instruction')
        product_code_gtin=request.POST.get('product_code_gtin')
        product_ndc=request.POST.get('product_ndc')
        product_code_type=request.POST.get('product_code_type')

        #product dispatch elements
        packaging_time=request.POST.get('packaging_time')
        package_type=request.POST.get('package_type')
        package_dimentions=request.POST.get('package_dimentions')

        #package pallet elements
        package_pallet_sn=request.POST.get('package_pallet_sn')
        inner_package_count=request.POST.get('inner_package_count')

        #case  elements
        for value in range(1,6):
            package_case_sn = request.POST.get('package_case_sn'+str(value))
            parent_pallet_package_id=request.POST.get('parent_pallet_package_id'+str(value))
            package_type=request.POST.get('package_type'+str(value))




        #unit  elements
        package_sn=request.POST.get('package_sn')
        inner_package_count=request.POST.get('inner_package_count')

        # import pdb; pdb.set_trace()
        productdata={'product_name': product_name,'mfg_date': mfg_date,'expiry_date': expiry_date,'product_description':product_description,'strength':strength,'batch_number':batch_number,'patient_instruction':patient_instruction,'product_code_gtin':product_code_gtin,'product_ndc':product_ndc,'product_code_type':product_code_type}
        result=requests.post('http://3.239.56.34:8000/product/',productdata).json()

        productdispatch={'packaging_time': packaging_time,'package_type':package_type,'package_dimentions':package_dimentions,'product':result['url']}
        result1=requests.post('http://3.239.56.34:8000/product_dispatch/',productdispatch).json()

        packagepallet={'package_pallet_sn': package_pallet_sn,'inner_package_count':inner_package_count,'product':result['url'],'product_disp':result1['url']}
        result2=requests.post('http://3.239.56.34:8000/package_Pallet/',packagepallet).json()

        casedata={'package_case_sn': package_case_sn,'parent_pallet_package_id':parent_pallet_package_id,'package_type':package_type,'parent_pallet_package':result2['url']}
        result3=requests.post('http://3.239.56.34:8000/package_cases/',casedata).json()

        unitdata={'package_sn': package_sn,'inner_package_count':inner_package_count,'parent_package_case':result3['url']}
        result4=requests.post('http://3.239.56.34:8000/package_units/',unitdata).json()

        return redirect("/manufacturer_order_details")
    else:
        return render(request,'manufacturer_order_details.html')


# Logistic details getting from manufacturer api view
def logistics_order_details_view(request):
    # import  pdb;pdb.set_trace()
    result_old=requests.get('http://18.207.255.94:8000/manufacturer_drug/').json()
    result=[]
    for row in result_old:
        if row['em_status']=='HandoffToRetailer':
            result.append(row)

    return render(request,'logistics_order_details.html',{'result':result})

# Logistics details Showing api view
def logistics_order_details_edit_view(request,id):
    result=requests.get('http://18.207.255.94:8000/manufacturer_drug/'+str(id)+'/').json()
    return render(request,'logistics_order_details_edit.html',{'result':result})

# Logistics details Submitting from manufacturer api to trace form api view
def logistics_order_update(request):

    result_old=requests.get('http://18.207.255.94:8000/tracepharm/').json()
    result=[]
    for row in result_old:
        #import pdb; pdb.set_trace()
        if row['em_sscc']==request.GET.get('em_sscc'):

            # import pdb; pdb.set_trace()
            em_sscc=request.GET.get('em_sscc')
            em_truck_no=request.GET.get('em_truck_no')
            # import pdb; pdb.set_trace()
            em_gtin=request.GET.get('em_gtin')
            em_pallet_no=request.GET.get('em_pallet_no')
            em_mfg_date=request.GET.get('em_mfg_date')
            em_expiry_date=request.GET.get('em_expiry_date')
            em_gln=request.GET.get('em_gln')
            em_drug_name=request.GET.get('em_drug_name')
            em_batch_no=request.GET.get('em_batch_no')
            em_drug_type=request.GET.get('em_drug_type')
            em_status=request.GET.get('em_status')
            em_ndc=request.GET.get('em_ndc')
            em_strength=request.GET.get('em_strength')
            em_product_description=request.GET.get('em_product_description')
            em_patient_instruction=request.GET.get('em_patient_instruction')
            em_destination=request.GET.get('em_destination')
            em_mfg_name=request.GET.get('em_mfg_name')
            em_packing_level=request.GET.get('em_packing_level')
            em_container_size=request.GET.get('em_container_size')
            em_inner_content=request.GET.get('em_inner_content')
            # em_mfg_name=request.POST.get('em_mfg_name')
            em_destination=request.GET.get('em_destination')
            em_transporter=request.GET.get('em_transporter')
            em_retailer_name=request.GET.get('em_retailer_name')
            em_order_no=request.GET.get('em_order_no')
            em_last_updated1=request.GET.get('em_last_updated1')
            em_current_owner=request.GET.get('em_current_owner')
            em_previous_owner=request.GET.get('em_previous_owner')

            # import pdb;pdb.set_trace()

            result=requests.put(row['url'],data={'em_sscc': em_sscc,
            'em_gtin': em_gtin,
            'em_mfg_date': em_mfg_date,
            'em_expiry_date': em_expiry_date,
            'em_gln':em_gln,
            'em_batch_no':em_batch_no,
            'em_pallet_no':em_pallet_no,
            'em_drug_name':em_drug_name,
            'em_drug_type':em_drug_type,
            'em_status':em_status,
            'em_ndc':em_ndc,
            'em_strength':em_strength,
            'em_product_description':em_product_description,
            'em_patient_instruction':em_patient_instruction,
            'em_destination':em_destination,
            'em_mfg_name':em_mfg_name,
            'em_packing_level':em_packing_level,
            'em_container_size':em_container_size,
            'em_inner_content':em_inner_content,
            # 'em_mfg_name':em_mfg_name,
            'em_destination':em_destination,
            'em_transporter':em_transporter,
            'em_retailer_name':em_retailer_name,
            'em_order_no':em_order_no,
            'em_last_updated1':em_last_updated1,
            'em_current_owner':em_current_owner,
            'em_previous_owner':em_previous_owner})

    return redirect("/logistics_order_details")




def retailer_order_details_view(request):
    # import  pdb;pdb.set_trace()
    result_old=requests.get('http://18.207.255.94:8000/manufacturer_drug/').json()
    result=[]
    for row in result_old:
        if row['em_status']=='HandoffToRetailer':
            result.append(row)

    return render(request,'retailer_order_details.html',{'result':result})

def retailer_order_details_edit_view(request,id):
    result=requests.get('http://18.207.255.94:8000/manufacturer_drug/'+str(id)+'/').json()
    return render(request,'retailer_order_details_edit.html',{'result':result})

def retailer_order_update(request):
    # import pdb; pdb.set_trace()
    if request.method=="POST":
        em_sscc=request.POST.get('em_sscc')
        em_gtin=request.POST.get('em_gtin')
        em_mfg_date=request.POST.get('em_mfg_date')
        em_expiry_date=request.POST.get('em_expiry_date')
        result=requests.post('http://18.207.255.94:8000/tracepharm/',data={'em_sscc': em_sscc,
            'em_gtin': em_gtin,
            'em_mfg_date': em_mfg_date,
            'em_expiry_date': em_expiry_date})
        return redirect("/retailer_order_details")
    else:
        return render(request,'retailer_order_details.html')

# for base page view
def base_view(request):
    result=requests.get('http://18.207.255.94:8000/tracepharm/').json()
    return render(request,'base.html',{ 'result':result, 'username':request.session['username'] or ''})

# for registration form 1 drop down bounding




#mobile app aplication view
def homeview(request):
    try:
        # import pdb; pdb.set_trace()
        result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
        return render(request, 'home.html', {'result': result, 'username':request.session['username'] or ''})
    except:
        return render(request,'home.html')



#  mobile app application showing result view
def detailsview(request):
    result = requests.get('http://18.207.255.94:8000/tracepharm/').json()
    final_resut = []
    for res in result:
        if request.GET.get('details') in res['em_serial_no']:
            final_resut.append(res)
        if request.GET.get('details') in res['em_ndc']:
            final_resut.append(res)


    return render(request, 'details.html', {'result': final_resut})

#manufacturer search view
def search(request):
    result=requests.get('http://3.239.56.34:8000/package_pallet_info/').json()
    final_resut=[]
    for res in result:
        #import pdb; pdb.set_trace()
        if request.GET.get('search') in res['product_disp']['sscc_no']:
            final_resut.append(res)
        if request.GET.get('search') in str(res['package_pallet_sn']):
            final_resut.append(res)
        # if request.GET.get('search') in str(res['package_case']['package_case_sn']):
        #     final_resut.append(res)

    return render(request,'search.html',{'result':final_resut,'res_token':request.session['email'] or ''})


def trace_identification(request):
    result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
    final_resut=[]
    for res in result:
        #import pdb; pdb.set_trace()
        if request.GET.get('trace_identification') in res['disptch']['sscc_no']:
            final_resut.append(res)
        if request.GET.get('trace_identification') in res['package_case']['package_case_serial_number']:
            final_resut.append(res)
        if request.GET.get('trace_identification') in res['package_unit']['package_sn']:
            final_resut.append(res)

    return render(request,'trace_identification.html',{'result':final_resut,'res_token':request.session['email'] or ''})


def lsp_identification(request):
    result=requests.get('http://3.239.56.34:8000/package_pallet_info/').json()
    final_resut=[]
    for res in result:

        if request.GET.get('lsp_identification') in res['product_disp']['sscc_no']:
            final_resut.append(res)
        if request.GET.get('lsp_identification') in str(res['package_pallet_sn']):
            final_resut.append(res)
    return render(request,'lsp_identification.html',{'result':final_resut,'res_token':request.session['email'] or ''})

def distributor_identification(request):
    result=requests.get('http://3.239.56.34:8000/package_case_info/').json()
    final_resut=[]
    for res in result:
        if request.GET.get('distributor_identification') in res['parent_pallet_package']['product_disp']['sscc_no']:
            final_resut.append(res)
        if request.GET.get('distributor_identification') in str(res['package_case_sn']):
            final_resut.append(res)
        if request.GET.get('distributor_identification') in str(res['parent_pallet_package']['package_pallet_sn']):
            final_resut.append(res)
    return render(request,'distributor_identification.html',{'result':final_resut,'res_token':request.session['email'] or ''})

def retailer_identification(request):
    result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
    final_resut=[]
    for res in result:
        if request.GET.get('retailer_identification') in res['package_unit']['package_sn']:
            final_resut.append(res)
        if request.GET.get('retailer_identification') in res['package_case']['package_case_serial_number']:
            final_resut.append(res)
        # if request.GET.get('retailer_identification') in res['package_pallet']['package_pallet_sn']:
        #     final_resut.append(res)

    return render(request,'retailer_identification.html',{'result':final_resut,'res_token':request.session['email'] or ''})


def show(request):
    try:
        # import pdb; pdb.set_trace()
        result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
        # return render(request,'show.html',{'result':result,'res_token':request.session['email'] or ''})
        # result = requests.get('http://tracepharm.us-e2.cloudhub.io/api/v1/packages/dispatch_products').json()
        return render(request,'show.html',{'result':result, 'res_token':request.session['email'] or ''})
    except:
        return redirect("/show")

# def verification(request):
#     import pdb; pdb.set_trace()
#     api_1 = requests.get('http://54.209.190.184:8080/api/getHistoryByPhAssetId/1').json()
#     api_2 = requests.get('http://54.209.190.184:8080/api/getHistoryByPhAssetId/1').json()
#     final_resut=[]
#     for key in api_1:
#         if key in api_2:
#             if request.GET.get('verification') in res['SerialNo']:
#                 final_resut.append(key)
#             else:
#                 print("not verified")
#         else:
#             print("not verified")
#
#     result = (key(api_1) == key(api_2))           #comapring two json

    return render(request,'verification.html',{'result':result, 'res_token':request.session['email'] or ''})

def verification(request):
    try:
        if request.method == 'POST':
            # import pdb; pdb.set_trace()
            input_value = request.POST.get("input")
            root_url = 'http://54.196.204.11:8081/api/v1/package_verify/{}'.format(input_value)
            root_url1 = 'http://54.196.204.11:8081/api/v1/product_verify/{}'.format(input_value)
            root_url2 = 'http://54.196.204.11:8081/api/v1/owner_verify/{}'.format(input_value)
            root_url3 = 'http://54.196.204.11:8081/api/v1/location_verify/{}'.format(input_value)
            print(root_url)
            response2 = requests.get(root_url).json()
            response1 = requests.get(root_url1).json()
            response3 = requests.get(root_url2).json()
            response4 = requests.get(root_url3).json()
            response2.update(response1)
            response2.update(response3)
            response2.update(response4)
            # result=requests.post('http://ec2-54-196-204 -11.compute-1.amazonaws.com:8081/location_verfication').json()
            # return render(request,'verification.html',{'response2':response2, 'res_token':request.session['email'] or ''})
            return render(request,'verification.html',{'response2':response2,'res_token':request.session['email'] or ''})
        else:
            return render(request,'verification.html')
    except:
        return redirect("/error1")

def trace(request):
    try:
        # import pdb; pdb.set_trace()
        result=requests.get('http://54.209.190.184:8080/api/getHistoryByPhAssetId/1').json()
        # result=requests.get('http://identification.us-e2.cloudhub.io/exp_identification/').json()
        # return render(request,'show.html',{'result':result,'res_token':request.session['email'] or ''})
        # result = requests.get('http://tracepharm.us-e2.cloudhub.io/api/v1/packages/dispatch_products').json()
        return render(request,'trace.html',{'result':result, 'res_token':request.session['email'] or ''})
    except:
        return redirect("/trace")

def lsp_identify(request):
    try:
        # import pdb; pdb.set_trace()
        # return render(request,'show.html',{'result':result,'res_token':request.session['email'] or ''})
        result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
        # result = requests.get('http://tracepharm.us-e2.cloudhub.io/api/v1/packages/dispatch_products').json()
        return render(request,'lsp_identify.html',{'result':result, 'res_token':request.session['email'] or ''})
    except:
        return redirect("/lsp_identify")

def distributor_identify(request):
    try:
        # import pdb; pdb.set_trace()
        result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
        # return render(request,'show.html',{'result':result,'res_token':request.session['email'] or ''})
        # result = requests.get('http://tracepharm.us-e2.cloudhub.io/api/v1/packages/dispatch_products').json()
        return render(request,'distributor_identify.html',{'result':result, 'res_token':request.session['email'] or ''})
    except:
        return redirect("/distributor_identify")

def retailer_identify(request):
    try:
        # import pdb; pdb.set_trace()
        result=requests.get('http://identificationv2.us-e2.cloudhub.io/exp_identification/').json()
        # return render(request,'show.html',{'result':result,'res_token':request.session['email'] or ''})
        # result = requests.get('http://tracepharm.us-e2.cloudhub.io/api/v1/packages/dispatch_products').json()
        return render(request,'retailer_identify.html',{'result':result, 'res_token':request.session['email'] or ''})
    except:
        return redirect("/retailer_identify")


# login view for users
def loginview(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            data={'email':email,'password':password}
            # import pdb; pdb.set_trace()
            result=requests.post('http://3.239.56.34:8000/api/auth/login',data)
            res_token=eval(result.text)
            # import pdb; pdb.set_trace()
            try:
                if res_token['access']:
                    # print(res_token['role'])
                    request.session['email'] = res_token,
                    # if res_token['role']=='7':
                    return redirect('/dashboard',{'res_token':res_token})
                    # elif res_token['role']=='2':

                else:
                    messages.info(request,'user password not matching')
                    return redirect('login')
            except:
                messages.info(request,'Please enter correct username and password')
                return redirect('login')
        else:
            return render(request, 'Login.html')
    except:
        # messages.info(request,'Please enter correct username and password')
        return redirect('error')

#  registration part
def registerview(request):
    # import pdb; pdb.set_trace()
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        alternate_email=request.POST.get('alternate_email')
        designation=request.POST.get('designation')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        alternate_contact_number=request.POST.get('alternate_contact_number')
        contact_number=request.POST.get('contact_number')
        organization_category=request.POST.get('organization_category')

        data2={'organization_category':organization_category}
        result_category=requests.post('http://3.239.56.34:8000/organization_category/',data2).json()
        data={'username':username,'email':email,'alternate_email':alternate_email,'password':password,'designation':designation,'first_name':first_name,'last_name':last_name,'alternate_contact_number':alternate_contact_number,'contact_number':contact_number,'organization':organization_category}
        result=requests.post('http://3.239.56.34:8000/api/auth/register',data).json()
        return redirect('/')
    else:
        return render(request,'register.html')


# def add_userview(request):
#     # import pdb; pdb.set_trace()
#     if request.method=="POST":
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         role=request.POST.get('role')
#         alternate_email=request.POST.get('alternate_email')
#         password=request.POST.get('password')
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         contact_number=request.POST.get('contact_number')
#         user_id=request.POST.get('user_id')
#         # organization_category=request.POST.get('organization_category')
#         #
#         # data2={'organization_category':organization_category}
#         # result_category=requests.post('http://3.239.56.34:8000/organization_category/',data2).json()
#         # data={'username':username,'email':email,'role':role,'alternate_email':alternate_email,'password':password,'first_name':first_name,'last_name':last_name,'contact_number':contact_number,'add_user':'http://3.237.20.101:8000/addusers/'+str(user_id)+'/','organization':'http://3.239.56.34:8000/organization_category/'+str(organization_category)+'/'}
#         data={'username':username,'email':email,'role':role,'alternate_email':alternate_email,'password':password,'first_name':first_name,'last_name':last_name,'contact_number':contact_number,'add_user':'http://3.239.56.34:8000/api/auth/adduser'+str(user_id)+'/'}
#         result=requests.post('http://3.239.56.34:8000/api/auth/adduser',data)
#         return redirect('/dashboard')
#     else:
#         return render(request,'add_user.html')

def add_userview(request):
    # import pdb; pdb.set_trace()
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        role=request.POST.get('role')
        alternate_email=request.POST.get('alternate_email')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        contact_number=request.POST.get('contact_number')
        user_id=request.POST.get('user_id')
        organization_category=request.POST.get('organization_category')

        data2={'organization_category':organization_category}
        result_category=requests.post('http://3.239.56.34:8000/organization_category/',data2).json()
        data={'username':username,'email':email,'role':role,'alternate_email':alternate_email,'password':password,'first_name':first_name,'last_name':last_name,'contact_number':contact_number,'organization':'http://3.239.56.34:8000/organization_category/'+str(result_category['organization_category'])+'/','add_user':'http://3.237.20.101:8000/addusers/'+str(user_id)+'/'}
        result=requests.post('http://3.239.56.34:8000/api/auth/adduser',data)
        return redirect('/dashboard')
    else:
        return render(request,'add_user.html')

def add_user_emailview(request):
    pass
    return render(request,'add_user.html',{'res_token':request.session['email'] or ''})
# def create_userview(request):
#     pass
#     return render(request,'create_user.html',{'res_token':request.session['email'] or ''})

def reset_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        data={'old_password':old_password,'new_password':new_password}
        result=requests.post('http://18.207.255.94:8000/api/login/',data)
        res_token=eval(result.text)


        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

#  logout view
def logoutview(request):
    # session.pop('email', None)
	# return redirect('/')
    auth.logout(request)
    return redirect('/')

def error_view(request):
    pass
    return render(request,'error.html')

def error1_view(request):
    pass
    return render(request,'error1.html')

def resetpasswordview(request):
    pass
    return render(request,'Reset-password.html')

def forgotpasswordview(request):
    pass
    return render(request,'Forgot-password.html')


def registerform1view(request):
    if request.method=="POST":
        # import pdb; pdb.set_trace()
        company_category=request.POST.get('company_category')
        company_name=request.POST.get('company_name')
        registration_no=request.POST.get('registration_no')
        telephone=request.POST.get('telephone')
        taxcode=request.POST.get('taxcode')
        contact_role=request.POST.get('contact_role')

        street_address1=request.POST.get('street_address1')
        street_address2=request.POST.get('street_address2')
        city=request.POST.get('city')
        postal_code=request.POST.get('postal_code')
        country_code=request.POST.get('country_code')

        user_id=request.POST.get('user_id')
        data1={'street_address1':street_address1,'street_address2':street_address2,'city':city,'postal_code':postal_code,'country_code':country_code}
        result_reg_adress=requests.post('http://3.239.56.34:8000/company_registration_address/',data1).json()
        data2={'company_category':company_category}
        result_category=requests.post('http://3.239.56.34:8000/company_category/',data2).json()
        data={'company_name':company_name,'registration_no':registration_no,
        'telephone':telephone,'taxcode':taxcode,'contact_role':contact_role,'gs1_address':result_reg_adress['url'],'company_category':company_category,
        'api_user':'http://3.239.56.34:8000/addusers/'+str(user_id)+'/'}
# remove company category from this view check when necessary
        result=requests.post('http://3.239.56.34:8000/company_registration/',data)
        return redirect('/registerform_1')
    else:
        return render(request,'Register-form-1.html')

def registerform_idview(request):
    pass
    return render(request,'Register-form-1.html',{'res_token':request.session['email'] or ''})

# registring personal details page2 view
def registerform2view(request):
    # import pdb; pdb.set_trace()
    if request.method=="POST":
        em_product_name=request.POST.get('em_product_name')
        em_product_description=request.POST.get('em_product_description')
        em_brand=request.POST.get('em_brand')
        em_sub_classification=request.POST.get('em_sub_classification')
        em_dosage=request.POST.get('em_dosage')
        em_additional_information=request.POST.get('em_additional_information')
        em_full_name=request.POST.get('em_full_name')
        em_designation=request.POST.get('em_designation')
        em_contact_number=request.POST.get('em_contact_number')
        em_alternate_number=request.POST.get('em_alternate_number')
        em_email_address=request.POST.get('em_email_address')
        em_alternate_email_address=request.POST.get('em_alternate_email_address')
        em_department=request.POST.get('em_department')
        # em_department=request.POST.get('em_department')


        data={'em_product_name':em_product_name,'em_product_description':em_product_description,'em_brand':em_brand,'em_sub_classification':em_sub_classification,'em_full_name':em_full_name,'em_designation':em_designation,'em_contact_number':em_contact_number,'em_alternate_number':em_alternate_number,'em_email_address':em_email_address,'em_alternate_email_address':em_alternate_email_address,'em_department':em_department}
        result=requests.post('http://18.207.255.94:8000/product_details/',data)
        return redirect('/')
    else:
        return render(request,'Registration-form-2.html')




# bulk upload view
# def simple_upload(request):
#     try:
#         if request.method == 'POST':
#             person_resource = PersonResource()
#             dataset = Dataset()
#             new_persons = request.FILES['myfile']
#
#             imported_data = dataset.load(new_persons.read(),format='xlsx')
#             #print(imported_data)
#             for data in imported_data:
#             	print(data[1])
#             	value = bulkdata(
#             		data[0],
#             		data[1],
#             		 data[2],
#             		 data[3],
#                      data[4],
#                      data[5],
#                      data[6],
#                      data[7],
#                      data[8],
#                      data[9],
#                      data[10],
#                      data[11]
#             		)
#             	value.save()
#
#             messages.info(request,'file uploaded successfully')
#         return render(request, 'bulk_insert.html')
#         messages.info(request,'file uploaded successfully')
#     except:
#         messages.info(request,'file uploaded successfully')
