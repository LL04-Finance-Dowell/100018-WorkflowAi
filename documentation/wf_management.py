import re
import json
from django.views import View
from django.http import JsonResponse
from django.contrib import messages

<<<<<<< HEAD
from .mongo_db_connection import save_wf, get_wf_object, get_document_object, update_document, get_document_list, save_uuid_hash, get_uuid_object
from .views import DocumentEditor

import uuid

from django.shortcuts import render, redirect
#from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
=======
from .mongo_db_connection import save_wf, get_wf_object, get_document_object, update_document, get_document_list
from .views import DocumentEditor



from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt

>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02

from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.models import Site

from .mail_format import formated_mail
#   from django.core.mail import EmailMultiAlternatives

from .mongo_db_connection import get_user_info_by_username


SESSION_ARGS = ["login","bangalore","login","login","login","6752828281","ABCDE"]
REGISTRATION_ARGS = ["login","bangalore","login","registration","registration","10004545","ABCDE"]


def send_notificationVia_mail(user_email, document_id, document_name, *args, **kwargs):
<<<<<<< HEAD
    uuid_hash = uuid.uuid4().hex
    route = reverse('documentation:verify-document', kwargs={"document_id": document_id, "uuid_hash": uuid_hash})

    uuid_status = save_uuid_hash(uuid_hash, user_email, document_id)
    print("Hash save response. ", uuid_status)

    link = Site.objects.get_current().domain + route
    html_content = formated_mail(user_email, link)
    send_mail(
        'Sign Document : ' + document_name,
        '', # You got document '+ instance.document_name +' to sign on DocEdit. Go at '+ link + ' to sign it ',
        '',
        [user_email,],
        fail_silently=False,
        html_message=html_content
    )
    return uuid_hash

=======
    try:
        email_to = user_email
        route = reverse('documentation:verify-document', kwargs={"document_id": document_id})
        link = Site.objects.get_current().domain + route
        html_content = formated_mail(email_to, link)
        send_mail(
            'Sign Document : ' + document_name,
            '', # You got document '+ instance.document_name +' to sign on DocEdit. Go at '+ link + ' to sign it ',
            '',
            [email_to,],
            fail_silently=False,
            html_message=html_content
        )
        return True
    except:
        return False
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02



def documentWorkFlowAddView(request, *args, **kwargs):
<<<<<<< HEAD
    if request.method == 'POST' and request.session['user_name'] :
        body = None
        print('Un the workflow request')
        #   try:
        body = json.loads(request.body)
        doc = get_document_object(body['file_id'])
        user = get_user_info_by_username(request.session['user_name'])
        new_step = ['Last', user['Email']]
        wf_obj = get_wf_object(doc['workflow_id'])
        new_wf = json.loads(save_wf('execute_wf', wf_obj['int_wf_string'], [*wf_obj['ext_wf_string'], new_step], request.session['user_name'], request.session['company_id']))
        dd = datetime.now()
        time = dd.strftime("%d:%m:%Y,%H:%M:%S")

        new_wf = get_wf_object(new_wf["inserted_id"])
        print("new Workflow:", new_wf)
        if new_wf['int_wf_string'] != [] :
            res = json.loads(update_document(
                body['file_id'],
                {
                    'workflow_id': new_wf['_id'],
                    #   'content': body['content'],
                    'int_wf_position': 1,
                    'int_wf_step': new_wf['int_wf_string'][0][0],
                    'update_time': time
                }
            ))
            if res["isSuccess"]:
                mail_status = send_notificationVia_mail(new_wf['int_wf_string'][0][1], body['file_id'], doc['document_name'])
                print('doc db updated', mail_status)
            else:
                print('doc db updated error')
        else:
            if new_wf['ext_wf_string'] != []:
                res = json.loads(update_document(
                    body['file_id'],
                    {
                        #   'content': body['content'],
                        'workflow_id': new_wf['_id'],
                        'ext_wf_position': 1,
                        'ext_wf_step': new_wf['ext_wf_string'][0][0],
                        'update_time': time
                    }
                ))
                if res["isSuccess"]:
                    mail_status = send_notificationVia_mail(new_wf['ext_wf_string'][0][1], body['file_id'], doc['document_name'])
                    print('doc db updated', mail_status)
                else:
                    print('doc db updated error')
        return JsonResponse({ 'status': 200, 'url': reverse('documentation:sign-docs') })
        #   except:           return JsonResponse({ 'status': 'ERROR' , 'message': 'Error placing document in workflow.'})
=======
    if request.session['user_name'] :
        body = None
        try:
            body = json.loads(request.body)
            doc = get_document_object(body['file_id'])

            user = get_user_info_by_username(request.session['user_name'])

            new_step = ['Last', user['Email']]
            wf_obj = get_wf_object(doc['workflow_id'])
            new_wf = save_wf('execute_wf', wf_obj['int_wf_string'], [*wf_obj['ext_wf_string'], new_step], request.session['user_name'], request.session['company_id'])

            from datetime import datetime
            dd = datetime.now()
            time = dd.strftime("%d:%m:%Y,%H:%M:%S")
            #   first_int_wf_step = ''
            #   first_ext_wf_step = ''

            if new_wf['int_wf_string'] != [] :
                #   x = re.findall("\w*\-\w*\*", doc['int_wf_string'])
                #   first_int_wf_step = re.split('\-', x[0])[0]
                doc = update_document(
                    body['file_id'],
                    {
                        'content': body['data'],
                        'workflow_id': new_wf['_id'],
                        'auth_user_list': [],
                        'int_wf_position': 1,
                        'int_wf_step': new_wf['int_wf_string'][0][0],
                        'update_time': time
                    }
                )
            else:
                if new_wf['ext_wf_string'] != []:
                    #   x = re.findall("\w*\-\w*\*", doc['ext_wf_string'])
                    #   first_ext_wf_step = re.split('\-', x[0])[0]
                    doc = update_document(
                        body['file_id'],
                        {
                            'content': body['data'],
                            'workflow_id': new_wf['_id'],
                            'auth_user_list': [],
                            'ext_wf_position': 1,
                            'ext_wf_step': new_wf['ext_wf_string'][0][0],
                            'update_time': time
                        }
                    )

            return JsonResponse({ 'status': 200, 'url': reverse('documentation:sign-docs') })
        except:
            return JsonResponse({ 'status': 'ERROR' , 'message': 'Error placing document in workflow.'})
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
    else:
        return JsonResponse({ 'status': 'ERROR' , 'message': 'A User must be related with company'})





def execute_wf(request, document_id, document_name, status, wf):
    step_name = ''
    status += 1
<<<<<<< HEAD
    if status > len(wf) :
=======
    if status == len(wf) :
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
        step_name = 'complete'
        messages.success(request, document_name.title() + ' document Signed at all stages.')
    else:
        step_name = wf[status - 1][0]           #   step_user = get_user(re.split('-', wf[status - 1])[1][:-1])
        mail_status = send_notificationVia_mail(wf[status - 1][1], document_id, document_name)
        if mail_status:
            print("mail_sent")
        else:
            print("mail_not_sent")
        messages.info(request, document_name.title() + ' document Signed at :'+ re.split('-', wf[status - 1])[0] + '.')
<<<<<<< HEAD
=======

>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
    return status, step_name



def workflowVerification(request, doc):
    status = 0
    step_name = ''
<<<<<<< HEAD
    res = None
=======
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
    wf = get_wf_object(doc['workflow_id'])
    int_wf_steps = wf['int_wf_string']   # int_wf_steps = re.findall("\w*\-\w*\*", wf['int_wf_string'])
    ext_wf_steps = wf['ext_wf_string']   # ext_wf_steps = re.findall("\w*\-\w*\*", wf['ext_wf_string'])

<<<<<<< HEAD
    if ((wf['int_wf_string'] != []) and (doc['int_wf_step'] != 'complete')) and (doc['int_wf_position'] <= len(int_wf_steps)):    #   if ((wf['int_wf_string'] != '') or (wf['int_wf_step'] != 'complete')) and (doc['int_wf_position'] <= len(int_wf_steps)):
        status, step_name = execute_wf(request, doc['_id'], doc['document_name'], doc['int_wf_position'], int_wf_steps)
        if status and status != doc['int_wf_position'] :
            res = json.loads(update_document(doc['_id'], {
                'int_wf_position': status,
                'int_wf_step': step_name,
                }
            ))

            doc = get_document_object(doc['_id'])

            if (doc['int_wf_step'] == 'complete') and (wf['ext_wf_string'] != []):
                res = json.loads(update_document(doc['_id'], {
                    'ex_wf_position': 1,
                    'ex_wf_step': step_name,
                    }
                ))
=======
    if ((wf['int_wf_string'] != []) or (doc['internal_wf_step'] != 'complete')) and (doc['int_wf_position'] <= len(int_wf_steps)):    #   if ((wf['int_wf_string'] != '') or (wf['int_wf_step'] != 'complete')) and (doc['int_wf_position'] <= len(int_wf_steps)):
        status, step_name = execute_wf(request, doc['_id'], doc['document_name'], doc['int_wf_position'], int_wf_steps)
        if status and status != doc['int_wf_position'] :
            doc = update_document(doc['_id'], {
                'int_wf_position': status,
                'int_wf_step': step_name,
                }
            )

            if (doc['internal_wf_step'] == 'complete') and (wf['ext_wf_string'] != []):
                doc = update_document(doc['_id'], {
                    'ex_wf_position': 1,
                    'ex_wf_step': step_name,
                    }
                )
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02

    elif ((wf['ext_wf_string'] != []) or (doc['ext_wf_step'] != 'complete')) and (doc['ext_wf_position'] <= len(ext_wf_steps)):
        status, step_name = execute_wf(request, doc['_id'], doc['document_name'], doc['ext_wf_position'], ext_wf_steps)
        if status and status != doc['ext_wf_position'] :
<<<<<<< HEAD
            res = json.loads(update_document(
=======
            doc = update_document(
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                doc['_id'], {
                    'ext_wf_position': status,
                    'ext_wf_step': step_name,
                }
<<<<<<< HEAD
            ))

            doc = get_document_object(doc['_id'])
            if doc['ext_wf_position'] == 'complete' :
                messages.info(request, 'Document completed External WorkFlow.')
    else:
        messages.error(request, 'No WorkFlow Available')
    print("Update response :", res)
=======
            )

    elif doc['ext_wf_position'] == 'complete' :
        messages.info(request, 'Document completed External WorkFlow.')
    else:
        messages.error(request, 'No WorkFlow Available')
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
    return doc, status, step_name



class DocumentVerificationView(DocumentEditor):
<<<<<<< HEAD
    verify = True
    is_template = False
    doc_viewer = False

    def get(self, request, *args, **kwargs):
        if kwargs.get('uuid_hash', None):
            uuid_obj = get_uuid_object(uuid_hash=kwargs["uuid_hash"])
            print("UUID object in Editor", uuid_obj['email'])
            document_obj = get_document_object(document_id=kwargs["document_id"])
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
                'user_email': uuid_obj['email'],
            }
            return render(request, 'editor.html', context={'document': ctx})
        else:
            return redirect("https://100014.pythonanywhere.com/logout")

    def post(self, request, **kwargs):
        doc = get_document_object(request.POST['document_id'])
        print("Document in wf: ", doc['int_wf_step'], doc['ext_wf_step'], doc['int_wf_position'], doc['ext_wf_position'])
        doc, status, step_name = workflowVerification(request, doc)
        if status != 0 and step_name != '' :
            data = json.loads(request.POST['documentData'])
            doc = json.loads(update_document(request.POST['document_id'], {'content': json.dumps(data) }))
            print("Document after updating step :", doc)
            return JsonResponse({"status": 200, "message": f"Document updated! - {doc}"})    # return redirect('editor:documents-in-workflow', company_id=kwargs['company_id'])
        else:
            print("Unauthorize access to document 403")
            return JsonResponse({'status': 403, 'url': '/', 'error': 'Unauthorize access to document.' })


=======
	verify = True
	is_template = False
	doc_viewer = False

	def post(self, request, **kwargs):
		doc = get_document_object(request.POST['document_id'])
		doc, status, step_name = workflowVerification(request, doc)
		if status != 0 and step_name != '' :
		    data = json.loads(request.POST['documentData'])
		    doc = update_document(request.POST['id'], {'content': json.dumps(data) })
		    return JsonResponse({"status": 200, "message": "Document updated!"})    # return redirect('editor:documents-in-workflow', company_id=kwargs['company_id'])
		else:
		    print("Unauthorize access to document 403")
		    return JsonResponse({'status': 403, 'url': '/', 'error': 'Unauthorize access to document.' })
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02

def user_in_wf(user, wf):
    status = False
    for step in wf:
        if user['Email'] == step[1]:
            status = True
    return status


def documentRejectionRequest(request, *args, **kwargs):
    if request.method == 'POST' and request.session['user_name']:
        body = json.loads(request.body)
        doc = get_document_object(body['file_id'])
        wf = get_wf_object(doc['workflow_id'])
        int_wf_steps = wf['int_wf_string']  #   re.findall("\w*\-\w*\*", wf['int_wf_string'])
        ext_wf_steps = wf['ext_wf_string']  #   re.findall("\w*\-\w*\*", wf['ext_wf_string'])

        user = get_user_info_by_username(request.session['user_name'])

        if user_in_wf(user, wf['int_wf_string']) or user_in_wf(user, wf['ext_wf_string']) :
            if wf['int_wf_string'] != [] and doc['int_wf_step'] != 'complete':
                if doc['int_wf_position'] > 0:
<<<<<<< HEAD
                    doc = json.loads(update_document(doc['_id'], {
=======
                    doc = update_document(doc['_id'], {
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                        'int_wf_position': doc['int_wf_position'] - 1,
                        'int_wf_step': int_wf_steps[doc['int_wf_position'] - 1][0],
                        'reject_message': body['reason'],
                        'rejected_by': request.session['user_name']
<<<<<<< HEAD
                    }))
                else:
                    doc = json.loads(update_document(doc['_id'], {
=======
                    })
                else:
                    doc = update_document(doc['_id'], {
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                        'int_wf_position': 0,
                        'int_wf_step': '',
                        'reject_message': body['reason'],
                        'rejected_by': request.session['user_name']
<<<<<<< HEAD
                    }))
            elif wf['ext_wf_string'] != '' and doc['ext_wf_step'] != 'complete':
                if doc['ext_wf_position'] > 0:
                    doc = json.loads(update_document(doc['_id'], {
=======
                    })
            elif wf['ext_wf_string'] != '' and doc['ext_wf_step'] != 'complete':
                if doc['ext_wf_position'] > 0:
                    doc = update_document(doc['_id'], {
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                        'ext_wf_position': doc['ext_wf_position'] - 1,
                        'ext_wf_step': ext_wf_steps[doc['ext_wf_position'] - 1][0],
                        'reject_message': body['reason'],
                        'rejected_by': request.session['user_name']
<<<<<<< HEAD
                    }))
=======
                    })
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
            else:
                return JsonResponse({'status': 300, 'url': 'Unable to reject.' })
            return JsonResponse({'status': 200, 'url': reverse('documentation:sign-docs') })
        else:
            return JsonResponse({'status': 302, 'url': 'Only wf authority requests are accepted.' })
    else:
        return JsonResponse({'status': 500, 'url': 'Only POST requests are accepted.' })




class DocumentCreatedListView(View):
    executed = False
    def get(self, request, *args, **kwargs):
        documents = get_document_list(request.session['company_id'])
        print("Documents :", documents)
        filtered_list = []
<<<<<<< HEAD
        try:
            for doc in documents:
                doc['document_id'] = doc['_id']
                if doc['created_by'] == request.session['user_name']:
                    if self.executed:
                        if doc['int_wf_position'] > 0 or doc['ext_wf_position'] > 0:
                            filtered_list.append(doc)
                    else:
                        filtered_list.append(doc)
        except:
            pass
=======
        for doc in documents:
            doc['document_id'] = doc['_id']
            if doc['created_by'] == request.session['user_name']:
                if self.executed:
                    if doc['int_wf_position'] > 0 or doc['ext_wf_position'] > 0:
                        filtered_list.append(doc)
                else:
                    filtered_list.append(doc)

>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
        return render(request, 'requested_documents.html', {'filtered_list': filtered_list})


class DocumentCreatedInExecutionListView(DocumentCreatedListView):
    executed = True



class DocumentExecutionListView(View):
    rejected = False
    template_name = 'requested_documents.html'

    def get(self, request, *args,**kwargs):
        filtered_list = []
        documents = get_document_list(request.session['company_id'])
<<<<<<< HEAD
        user = get_user_info_by_username(request.session['user_name'])

        # user['Email']

=======
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
        print('documents in List view', documents)
        for doc in documents:
            doc['document_id'] = doc['_id']
            try:
                wf = get_wf_object(doc['workflow_id'])
<<<<<<< HEAD
                int_wf_steps = wf['int_wf_string']
                ext_wf_steps = wf['ext_wf_string']
                if doc['workflow_id']:
                    if wf['int_wf_string'] != '' and doc['int_wf_step'] != 'complete':
                        for step in int_wf_steps:
                            if (step[0] == doc['int_wf_step']) and (step[1] == user['Email']):
=======
                int_wf_steps = re.findall("\w*\-\w*\*", wf['int_wf_string'])
                ext_wf_steps = re.findall("\w*\-\w*\*", wf['ext_wf_string'])
                if doc['workflow_id']:
                    if wf['int_wf_string'] != '' and doc['int_wf_step'] != 'complete':
                        for step in int_wf_steps:
                            if (re.split('-', step)[0] == doc['int_wf_step']) and (re.split('-', step)[1][:-1] == request.session['user_name']):
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                                if not self.rejected:
                                    if doc['rejected_by'] == '' :
                                        filtered_list.append(doc)
                                else:
                                    if doc['rejected_by'] != '' :
                                        filtered_list.append(doc)


<<<<<<< HEAD
                    elif wf['ext_wf_string'] != [] and (doc['ext_wf_step'] != 'complete'):
                        for step in ext_wf_steps:
                            if (step[0] == doc['ext_wf_step']) and (step[1] == user['Email']):
=======
                    elif wf['ext_wf_string'] != '' and (doc['ext_wf_step'] != 'complete'):
                        for step in ext_wf_steps:
                            if (re.split('-', step)[0] == doc['ext_wf_step']) and (re.split('-', step)[1][:-1] == request.session['user_name']):
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                                if not self.rejected:
                                    if doc['rejected_by'] == '' :
                                        filtered_list.append(doc)
                                else:
                                    if doc['rejected_by'] != '' :
                                        filtered_list.append(doc)
            except:
                pass

        return render(request, self.template_name, {'filtered_list': filtered_list, 'rejected': self.rejected})


class RejectedDocumentListView(DocumentExecutionListView):
    rejected = True
    template_name = 'reject_list.html'





'''
class RejectedDocumentListView(DocumentExecutionListView):
    def get(self, *args, **kwargs):
        filtered_list = []
        documents = get_document_list(request.session['company_id'])

        for doc in documents:
            wf = get_wf_object(doc['workflow_id'])
            int_wf_steps = re.findall("\w*\-\w*\*", wf['int_wf_string'])
            ext_wf_steps = re.findall("\w*\-\w*\*", wf['ext_wf_string'])

            if wf['int_wf_string'] != '' and doc['int_wf_step'] != 'complete'):
                for step in int_wf_steps:
                    if (re.split('-', step)[0] == doc['int_wf_step']) and (re.split('-', step)[1][:-1] == request.session['user_name']):
                        if doc['rejected_by'] != '' :
                            filtered_list.append(doc)

            elif wf['ext_wf_string'] != '' and (doc['ext_wf_step'] != 'complete'):
                for step in ext_wf_steps:
                    if (re.split('-', step)[0] == doc['ext_wf_step']) and (re.split('-', step)[1][:-1] == request.session['user_name']):
                        if doc['rejected_by'] != '' :
                            filtered_list.append(doc)


        return render(request, 'document_list.html', {'object_list': filtered_list})

<<<<<<< HEAD
'''



=======
'''
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
