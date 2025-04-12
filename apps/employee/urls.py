from django.urls import path
from . import views


urlpatterns=[
    path("employee/create/", view=views.EmployeeCreateView.as_view(), name="employee_create"),
    path("employee/list/", view=views.EmployeeListView.as_view(), name="employee_list"),
    path("employee/update/<uuid:id>/", view=views.EmployeeUpdateView.as_view(), name="employee_update"),
    path("employee/delete/<uuid:id>/", view=views.EmployeeDestroyView.as_view(), name="employee_delete"),
    path("employee/retrieve/<uuid:id>/", view=views.EmployeeRetrieveView.as_view(), name="employee_retrieve"),
    path("employee/personal/update/<uuid:id>/", view=views.EmployeePersonalInfoUpdateAPIView.as_view(), name="employee_update_personal"),
    path("employee/personal/retrieve/<uuid:id>/", view=views.EmployeePersonalInfoRetriveAPIView.as_view(), name="employee_retrieve_personal"),

    path("employee-attachments/employee/create/", view=views.AttachmentsCreateView.as_view(), name="attachment_create"),
    path("employee-attachments/employee/list/", view=views.AttachmentsListView.as_view(), name="attachment_list"),
    path("employee-attachments/employee/update/<uuid:id>/", view=views.AttachmentsUpdateView.as_view(), name="attachment_update"),
    path("employee-attachments/employee/delete/<uuid:id>/", view=views.AttachmentsDestroyView.as_view(), name="attachment_delete"),
    path("employee-attachments/employee/retrieve/<uuid:id>/", view=views.AttachmentsRetrieveView.as_view(), name="attachment_retrieve"),

]