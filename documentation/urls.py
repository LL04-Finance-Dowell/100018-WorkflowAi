from django.urls import path
from .views import main, home, logout, EmailWorkflow, Template, add_members
from .views import previous_template, TemplateEditor, CreateDocument, DocumentEditor, DocumentViewer, UserAuthenticate

from .wf_management import DocumentVerificationView, documentRejectionRequest, DocumentExecutionListView, documentWorkFlowAddView, DocumentCreatedListView, RejectedDocumentListView
from .wf_management import DocumentCreatedInExecutionListView

app_name = "documentation"

urlpatterns = [
    path('', main, name='main'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('manage_workflow', EmailWorkflow.as_view(), name='manage-workflow'),
    path('create-template', Template.as_view(), name='create-template'),
    path('prevs-template', previous_template, name='prevs-template'),
    path('create-docs', CreateDocument.as_view(), name='create-docs'),

    path('template/<str:template_id>', TemplateEditor.as_view(), name='template-editor'),
    path('document/<str:document_id>', DocumentEditor.as_view(), name='document-editor'),
    path('add-to-wf', documentWorkFlowAddView, name="add-to-wf"),
    path('sign-document/<str:document_id>/<str:uuid_hash>', DocumentVerificationView.as_view(), name="verify-document"),
    path('reject-document-request', documentRejectionRequest, name="reject-document"),

    path('view-document/<str:document_id>', DocumentViewer.as_view(), name='view-document'),
    path('user-authorization/<str:document_id>', UserAuthenticate.as_view(), name='user-authentication'),

    path('sign-docs', DocumentExecutionListView.as_view(), name='sign-docs'),
    path('reject-list', RejectedDocumentListView.as_view(), name='reject-list'),
    path('prev-docs', DocumentCreatedListView.as_view(), name='prev-docs'),
    path('add-members', add_members, name='add-members'),
    #   path('manage_document', Document.as_view(), name='manage-document'),
    path('requested-documents', DocumentCreatedInExecutionListView.as_view(), name='requested-documents'),


]