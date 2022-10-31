import json
import requests
from django import forms

from django.views import View
from django.shortcuts import render ,redirect, reverse
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import (
    xframe_options_exempt, xframe_options_deny, xframe_options_sameorigin,
)
from django.utils.decorators import method_decorator
from .dowellconnection import dowellconnection
from .mongo_db_connection import get_all_wf_list, save_wf, get_wf_list, get_user_list, get_template_list, save_template, get_template_object, update_template, save_document
from .mongo_db_connection import get_document_object, update_document, get_wf_object, get_user_info_by_username
from functools import wraps


from .forms import CreateTemplateForm, CreateDocumentForm


SESSION_ARGS = ["login","bangalore","login","login","login","6752828281","ABCDE"]
REGISTRATION_ARGS = ["login","bangalore","login","registration","registration","10004545","ABCDE"]


def redirect_to_login():
    return redirect("https://100014.pythonanywhere.com/register?redirect_url=https://100084.pythonanywhere.com")


@csrf_exempt
def main(request):
    session_id = request.GET.get('session_id', None)
    if session_id:
        field = { "SessionID" : session_id }
        response = dowellconnection(*SESSION_ARGS, "fetch",field,"nil")
        res = json.loads(response)
        if res['isSuccess']:
            request.session['session_id'] = res['data'][0]['SessionID']

        fields = { "Username" : res['data'][0]['Username'] }
        response = dowellconnection(*REGISTRATION_ARGS,"fetch",fields,"nil")
        usrdic = json.loads(response)
        if usrdic['isSuccess']:
            print("User Role :", usrdic["data"][0]["Role"])
            request.session["Role"] = usrdic["data"][0]["Role"]
            try:
                request.session["company_id"] = usrdic["data"][0]["company_id"]
            except:
                request.session["company_id"] = None
            request.session["user_name"]= usrdic["data"][0]["Username"]
            print("LoggedIn as : ", usrdic["data"][0])
            return redirect('documentation:home')   #   HttpResponse("hello")
        else:
            return redirect_to_login()   #   return redirect("https://100014.pythonanywhere.com/?code=100084")
    else:
        return redirect_to_login()


def logout(request):
    del request.session["user_name"]
    del request.session["company_id"]
    del request.session["Role"]
    return redirect("https://100014.pythonanywhere.com/logout")







def home(request, *args, **kwargs):
    if request.session.get("user_name"):
        return render(request, 'home.html', {"obj":request.session.items()})    #HttpResponse(context)
    else:
        return redirect_to_login()


class EmailWorkflow(View):

    def get(self, request, *args, **kwargs):
        wf_list = get_wf_list(request.session['company_id'])
        wfs_to_display = []
        for wf in wf_list:
            wf["id"] = wf["_id"]
            print("workflow_list :", wf)
            if wf.get('workflow_title') and (wf.get('workflow_title') != 'execute_wf') :
                wfs_to_display.append(wf)
        return render(request, 'manage_workflow.html', context={'wf_list': wfs_to_display, 'workflow':['internal', 'external']})


    def post(self, request, *args, **kwargs):
        body = None
        try:
            body = json.loads(request.body)
        except:
            body = None
        if not body or not body['title'] :
            context = {
                'object': 'Error: Title required.'
            }
            return JsonResponse(context)

        int_wf_string = []
        ext_wf_string = []

        if len(body['internal']) :
            for step in body['internal']:
                int_wf_string.append([step['name'], step['emailID']])

        if len(body['external']) :
            for step in body['external']:
                ext_wf_string.append([step['name'], step['emailID']])

        obj = save_wf(wf_name=body['title'], int_wf_string=int_wf_string, ext_wf_string=ext_wf_string, user=request.session['user_name'], company_id=request.session['company_id'])

        return JsonResponse({"status": 200, "message": "workflow added.", 'obj': obj})




class Template(View):
    def get(self, request, *args, **kwargs):
        if request.session['user_name']:
            template_list = []
            template_list = [(0, '--Template Name(None)--')]
            try:
                for i in get_template_list(request.session['company_id']):
                    template_list.append((i['_id'], i['template_name']))
            except:
                pass

            wf_list = []
            wf_list = [(0, '--Workflow (None)--')]
            try:
                for i in get_wf_list(request.session['company_id']):
                    wf_list.append((i['_id'], i['workflow_title']))
            except:
                pass

            form = CreateTemplateForm()
            CreateTemplateForm.base_fields['workflow'] = forms.ChoiceField(choices=wf_list)
            CreateTemplateForm.base_fields['copy_template'] = forms.ChoiceField(choices=template_list, required=False)

            CreateTemplateForm.base_fields['workflow'].widget.attrs.update({'class': 'form-control selectpicker','data-style':"btn-custom"})
            CreateTemplateForm.base_fields['copy_template'].widget.attrs.update({'class': 'form-control selectpicker','data-style':"btn-custom"})
            form = CreateTemplateForm()
            return render(request, 'create_template.html', {'form': form})
        else:
            return redirect_to_login()


    def post(self, request, *args, **kwargs):
        data = ''
        old_template = None
        form = CreateTemplateForm(request.POST)
        company_id = request.session["company_id"]
        created_by = request.session['user_name']
        if form.is_valid():
            if 'name' in form.cleaned_data.keys() and 'workflow' in form.cleaned_data.keys():
                if form.cleaned_data['copy_template'] :
                    try:
                        old_template = get_template_object(form.cleaned_data['copy_template'])
                        data = old_template['content']
                    except:
                        pass

                resObj = json.loads(save_template(form.cleaned_data['name'], form.cleaned_data['workflow'], data, created_by, company_id))
                print('This is a response from Report server', resObj)
                if resObj['isSuccess'] :
                    return redirect('documentation:template-editor', template_id=resObj['inserted_id'])
            return JsonResponse({"status": 300, "Error": "Name and workflow required."})
        return JsonResponse({"status": 420, "Error": "invalid form"})


class TemplateEditor(View):
    def get(self, request, *args, **kwargs):
        if request.session['user_name']:
            template_obj = get_template_object(template_id=kwargs["template_id"])
            workflow_obj = get_wf_object(template_obj['workflow_id'])
            user = get_user_info_by_username(request.session['user_name'])

            user_list = []
            for step in workflow_obj['int_wf_string']:
                user_list.append(step[1])
            for step in workflow_obj['ext_wf_string']:
                user_list.append(step[1])

            print("Template object in Template Editor", template_obj)
            ctx = {
                'id': template_obj['_id'],
                'name': template_obj['template_name'],
                'created_by': template_obj['created_by'],
                'auth_user_list': [str(user['Email']), *user_list],
                'file': template_obj['content'],
                'verify': False,
                'template': True,
                'doc_viewer': False,
                'company_id': template_obj['company_id'],
                'user_email': user['Email'],
            }

            return render(request, 'editor.html', context={'document': ctx})
        else:
            return redirect_to_login()


    def post(self, request,*args, **kwargs):
        if request.session['user_name']:
            body = json.loads(request.body)
            template_id = body["file_id"]
            data = body["content"]
            resObj = update_template(template_id, json.dumps(data))
            print('body : ', body, '\nThis is a response from Report server', resObj)
            try:
                if resObj['isSuccess'] :
                    return JsonResponse({"status": "200", "message": "Template saved!"})    #   redirect('documentation:document-editor', template_id=resObj['inserted_id'])
            except:
                return JsonResponse({"status": "340", "Error": "Unable to save on database"})
        else:
            return JsonResponse({"status": "420", "message": "invalid data"})



class CreateDocument(View):
    def get(self, request, *args, **kwargs):
        if request.session['user_name']:
            form = CreateDocumentForm()
            template_list = [(0, '__Template Name__')]
            for i in get_template_list(company_id=request.session["company_id"]):
                template_list.append((i['_id'], i['template_name']))
            CreateDocumentForm.base_fields['copy_template'] = forms.ChoiceField(choices=template_list)
            CreateDocumentForm.base_fields['copy_template'].widget.attrs.update({'class': 'form-control selectpicker','data-style':"btn-custom"})

            form = CreateDocumentForm()
            return render(request, 'create_document.html', {'form': form})
        else:
            return redirect_to_login()


    def post(self, request, *args, **kwargs):
        data = ''
        form = CreateDocumentForm(request.POST)
        if request.session['user_name']:
            company_id = request.session["company_id"]
            created_by = request.session['user_name']
            if form.is_valid():
                template_id = form.cleaned_data['copy_template']
                name = form.cleaned_data['name']
                resObj = json.loads(save_document(name, template_id, data, created_by, company_id))
                print('This is a response from Report server', resObj)
                if resObj['isSuccess'] :
                    return redirect('documentation:document-editor', document_id=resObj['inserted_id'])
                return JsonResponse({"status": 400, "message": "Unable to save on database"})
            return JsonResponse({"status": 420, "message": "invalid form"})
        else:
            return redirect_to_login()


class UserAuthenticate(View):
    redirect_url = ''
    def get(self, request, *args, **kwargs):
        self.redirect_url = reverse('document:verify', kwargs={'document_id': kwargs['document_id']})
        return render(request, 'link_based_authenticate.html')

    def post(self, request):
        post_obj = {
            "Username": request.POST['user'],
            "OS": request.POST['osver'],
            "Device": request.POST['device'],
            "Browser": request.POST['brow'],
            "Location": request.POST['loc'],
            "Time": request.POST['ltime'],
            "Connection": request.POST['mobconn'],
            "IP": request.POST['ipuser']
        }

        res_obj = requests.post('https://100014.pythonanywhere.com/api/linkbased', payload=post_obj)

        request.session['user_name'] = res_obj['data'][0]['Username']
        return redirect(self.redirect_url)


class DocumentEditor(View):
    verify = False
    template = False
    doc_viewer = False

    def get(self, request, *args, **kwargs):
        if request.session['user_name']:
            document_obj = get_document_object(document_id=kwargs["document_id"])
            user = get_user_info_by_username(request.session['user_name'])
            print("Document object in Editor", document_obj['int_wf_step'])
            ctx = {
                'id': document_obj['_id'],
                'name': document_obj['document_name'],
                'created_by': document_obj['created_by'],
                'auth_user_list': document_obj['auth_user_list'],
                'file': document_obj['content'],
                'verify': self.verify,
                'template': self.template,
                'doc_viewer': self.doc_viewer,
                'company_id': document_obj['company_id'],
                'user_email': user['Email'],
            }
            return render(request, 'editor.html', context={'document': ctx})
        else:
            if self.verify :
                return redirect("documentation:user-authentication", document_id=kwargs["document_id"])
            return redirect("https://100014.pythonanywhere.com/logout")


    def post(self, request,*args, **kwargs):
        if request.session['user_name']:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print("Document Post:", body['file_id'], str(body['content']))
            res = update_document(body["file_id"], {'content': json.dumps(body["content"])})
            #   print("res  : ", res)
            res_obj = json.loads(res)
            print('This is a response from Report server', res)
            if res_obj["isSuccess"]:
                return JsonResponse({"status": 200, "res"  : res })   #   "url": reverse('documentation:document-editor', kwargs={'document_id': body['file_id']})
            else:
                return JsonResponse({"status": 400, "message": "Unable to save on database"})
            '''
            Uncomment this when document update is corrected.
            if resObj['isSuccess'] :
                return JsonResponse({"status": 200, "url": reverse('documentation:document-editor', kwargs={'document_id':document_id'})  #redirect('documentation:document-editor', template_id=resObj['inserted_id'])

            '''
        else:
            return JsonResponse({"status": 420, "message": "invalid data"})



class DocumentViewer(DocumentEditor):
    verify = False
    template = False
    doc_viewer = True

    def post(self, request, *args, **kwargs):
        pass



def previous_template(request):
    template_list = get_template_list(company_id=request.session["company_id"])
    for item in template_list:
        item['template_id'] = item['_id']
    return render(request, 'prev_temp.html', context={'template_list': template_list})


class Document(View):
    pass


def add_members(request):
    reject_list = []
    return render(request, 'reject_list.html', context={'reject_list': reject_list})


def requested_documents(request):
    reject_list = []
    return render(request, 'reject_list.html', context={'reject_list': reject_list})




'''
from django.contrib.auth import REDIRECT_FIELD_NAME


def user_passes_test(test_func, login_url='', redirect_field_name=REDIRECT_FIELD_NAME):
    def decorator(view_func):
        @wraps(view_func)
        def rt_wrapper(request, *args, **kwargs):
            session_id = request.GET.get('session_id', None)
            user_name = request.session.get("user_name", None)

            if test_func(request.session["user_name"]):
                return view_func(request, *args, **kwargs)

            if session_id :
                role = ''
                field={"SessionID":session_id}
                sessions=dowellconnection("login","bangalore","login","login","login","6752828281","ABCDE","fetch",field,"nil")
                session=json.loads(sessions)
                username=''
                for i in session["data"]:
                    username=i["Username"]
                    print("first OutPut :", sessions)


                fields={"Username":username}
                usr=dowellconnection("login","bangalore","login","registration","registration","10004545","ABCDE","fetch",fields,"nil")
                usrdic=json.loads(usr)
                for i in usrdic["data"]:
                    print("User Role :", usrdic["data"][0]["Role"])
                    request.session["Role"] = usrdic["data"][0]["Role"]
                    request.session["company_id"] = usrdic["data"][0]["company_id"]
                    request.session["user_name"]= usrdic["data"][0]["Username"]

                if test_func(request.session["user_name"]):
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect("https://100014.pythonanywhere.com/?code=100084")
            else:
                return redirect("https://100014.pythonanywhere.com/?code=100084")

        return rt_wrapper
    return decorator


def dowell_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    actual_decorator = user_passes_test(
        lambda user_name: user_name,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def class_user_passes_test(test_func, login_url='', redirect_field_name=REDIRECT_FIELD_NAME):
    def decorator(view_func):
        @wraps(view_func)
        def rt_wrapper(self, request, *args, **kwargs):
            session_id = request.GET.get('session_id', None)
            user_name = request.session.get("user_name", None)

            if test_func(request.session["user_name"]):
                return view_func(self, request, *args, **kwargs)

            if session_id :
                role = ''
                field={"SessionID":session_id}
                sessions=dowellconnection("login","bangalore","login","login","login","6752828281","ABCDE","fetch",field,"nil")
                session=json.loads(sessions)
                username=''
                for i in session["data"]:
                    username=i["Username"]
                    print("first OutPut :", sessions)


                fields={"Username":username}
                usr=dowellconnection("login","bangalore","login","registration","registration","10004545","ABCDE","fetch",fields,"nil")
                usrdic=json.loads(usr)
                for i in usrdic["data"]:
                    print("User Role :", usrdic["data"][0]["Role"])
                    request.session["Role"] = usrdic["data"][0]["Role"]
                    request.session["company_id"] = usrdic["data"][0]["company_id"]
                    request.session["user_name"]= usrdic["data"][0]["Username"]

                if test_func(request.session["user_name"]):
                    return view_func(self, request, *args, **kwargs)
                else:
                    return redirect("https://100014.pythonanywhere.com/?code=100084")
            else:
                return redirect("https://100014.pythonanywhere.com/?code=100084")
        return rt_wrapper
    return decorator


def dowell_class_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    actual_decorator = class_user_passes_test(
        lambda u: u,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator



def workflow_list(request, *args, **kwargs):
    if request.session.get("user_name"):
        wf_list = get_wf_list(company_id=request.session["company_id"])
        #   user_list = get_user_list(company_id=request.session["company_id"])
        return render(request, 'manage_workflow.html', context={'wf_list': wf_list, 'workflow':['internal', 'external']})
    else:
        return redirect("https://100014.pythonanywhere.com/?code=100084")



class Workflow(View):

    def get(self, request, *args, **kwargs):
        wf_list = get_wf_list(company_id=request.session["company_id"])
        user_list = get_user_list(company_id=request.session["company_id"])
        return render(request, 'manage_workflow.html', context={'wf_list': wf_list, 'user_list': user_list, 'workflow':['internal', 'external']})


    def post(self, request, *args, **kwargs):
        body = None
        try:
            body = json.loads(request.body)
        except:
            body = None
        if not body or not body['title'] :
            context = {
                'object': 'Error: Title required.'
            }
            return JsonResponse(context)

        int_wf_string = ''
        ext_wf_string = ''

        if len(body['internal']) :
            for step in body['internal']:
                if  ('-' in step['name']) or ('*' in step['name']):
                    return JsonResponse({"status": "325", "message": "Step name must not contain '-', '*'.", 'obj': step['name']})
                int_wf_string += step['name'] + '-' + step['authority'] + '*'

        if len(body['external']) :
            for step in body['external']:
                if ('-' in step['name']) or ('*' in step['name']):
                    return JsonResponse({"status": "325", "message": "Step name cannot contain '-'.", 'obj': step['name']})
                ext_wf_string += step['name'] + '-' + step['authority'] + '*'

        obj = save_wf(wf_name=body['title'], int_wf_string=int_wf_string, ext_wf_string=ext_wf_string, user=request.session['user_name'], company_id=request.session['company_id'])

        return JsonResponse({"status": 200, "message": "workflow added.", 'obj': obj})


'''






