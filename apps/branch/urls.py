from django.urls import path
from . import views


urlpatterns=[
    path("branch/create/", view=views.BranchCreateView.as_view(), name="branch_create"),
    path("branch/list/", view=views.BranchListView.as_view(), name="branch_list"),
    path("branch/update/<uuid:id>/", view=views.BranchUpdateView.as_view(), name="branch_update"),
    path("branch/delete/<uuid:id>/", view=views.BranchDestroyView.as_view(), name="branch_delete"),
    path("branch/retrieve/<uuid:id>/", view=views.BranchRetrieveView.as_view(), name="branch_retrieve"),
]