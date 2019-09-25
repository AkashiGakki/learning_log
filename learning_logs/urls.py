from django.urls import path, include

import learning_logs.views

app_name = 'note'
urlpatterns = [
    path('index', learning_logs.views.get_index_page, name='index'),
    path('topics', learning_logs.views.get_topics_page, name='topics'),
    path('topics/<int:topic_id>', learning_logs.views.get_entry_page, name='topics'),
    path('new_topic', learning_logs.views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', learning_logs.views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', learning_logs.views.edit_entry, name='edit_entry')
]
