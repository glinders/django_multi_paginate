from django.urls import path

from . import views

# register our namespace
app_name = 'mpag'


urlpatterns = [
    # home page
    path(
        '',
        views.index,
        name='index'
    ),
    # room detail view
    path(
        'room/<int:room_id>/',
        views.MpagDetailView.as_view(
            extra_context={
                'title': 'MPag Detail'
            },
        ),
        name='detail',
    ),
]