from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('automated_testing',views.automated_testing,name="automated_testing"),
    path('getuserfeedbackform',views.getuserfeedbackform,name="getuserfeedbackform"),
    path('deleteTime',views.deleteTime,name="deleteTime"),
    path('addRecord',views.addRecord,name="addRecord"),
    path('ticketinfo',views.ticketinfo,name="ticketinfo"),
    path('showallrecords',views.showallrecords,name="showallrecords"),
    path('deleteticket',views.deleteticket,name="deleteticket"),
    path('listall',views.listall,name="listall"),
    path('timeinfo',views.timeinfo,name="timeinfo"),
    path('updatetime',views.updatetime,name="updatetime"),
    path('searchRec',views.searchRec,name="searchRec"),
    path('saveuserfeedbackform',views.saveuserfeedbackform,name="saveuserfeedbackform"),
    path('search',views.search,name="search"),
    path('result',views.result,name='result'),
    path('geturlhistory',views.geturlhistory,name="geturlhistory"),
    path('discuss',views.discuss,name="discuss"),
    path('reply/<int:replyid>',views.replyform,name="reply"),
    path('savereply',views.savereply,name="reply"),
    path('searchdiscuss',views.searchdiscuss,name="searchdiscuss")

]

