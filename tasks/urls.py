from django.urls import path

from tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    path(
        'task/<int:pk>/edit/',
        views.TaskUpdateView.as_view(),
        name='task-edit'
    ),
    path(
        'task/<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='task-delete'
    ),
    path(
        'task/<int:pk>/toggle/',
        views.ToggleTaskStatusView.as_view(),
        name='task-toggle'
    ),

    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/add/', views.TagCreateView.as_view(), name='tag-add'),
    path(
        'tags/<int:pk>/edit/',
        views.TagUpdateView.as_view(),
        name='tag-edit'
    ),
    path(
        'tags/<int:pk>/delete/',
        views.TagDeleteView.as_view(),
        name='tag-delete'
    ),
]
