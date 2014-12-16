import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/student/$',ajaxHandeler.ajax_Student),
    (r'^api/student/(?P<id>\d+)/$',ajaxHandeler.ajax_Student),
    #(r'^student/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/parent/$',ajaxHandeler.ajax_Student_Parent),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/class/$',ajaxHandeler.ajax_Student_Class),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/student/mv/$',ajaxHandeler.ajax_Student_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/employee/$',ajaxHandeler.ajax_Employee),
    (r'^api/employee/(?P<id>\d+)/$',ajaxHandeler.ajax_Employee),
    #(r'^employee/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/employee/(?P<id>\d+)/class/$',ajaxHandeler.ajax_Employee_Class),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/employee/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_Employee_Subject),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/employee/mv/$',ajaxHandeler.ajax_Employee_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/parent/$',ajaxHandeler.ajax_Parent),
    (r'^api/parent/(?P<id>\d+)/$',ajaxHandeler.ajax_Parent),
    #(r'^parent/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/parent/mv/$',ajaxHandeler.ajax_Parent_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/class/$',ajaxHandeler.ajax_Class),
    (r'^api/class/(?P<id>\d+)/$',ajaxHandeler.ajax_Class),
    #(r'^class/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/class/(?P<id>\d+)/employee/$',ajaxHandeler.ajax_Class_Employee),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/class/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_Class_Subject),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/class/mv/$',ajaxHandeler.ajax_Class_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/subject/$',ajaxHandeler.ajax_Subject),
    (r'^api/subject/(?P<id>\d+)/$',ajaxHandeler.ajax_Subject),
    #(r'^subject/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/subject/(?P<id>\d+)/employee/$',ajaxHandeler.ajax_Subject_Employee),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/subject/mv/$',ajaxHandeler.ajax_Subject_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/mark/$',ajaxHandeler.ajax_Mark),
    (r'^api/mark/(?P<id>\d+)/$',ajaxHandeler.ajax_Mark),
    #(r'^mark/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/mark/mv/$',ajaxHandeler.ajax_Mark_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/result/$',ajaxHandeler.ajax_Result),
    (r'^api/result/(?P<id>\d+)/$',ajaxHandeler.ajax_Result),
    #(r'^result/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/result/mv/$',ajaxHandeler.ajax_Result_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/exam/$',ajaxHandeler.ajax_Exam),
    (r'^api/exam/(?P<id>\d+)/$',ajaxHandeler.ajax_Exam),
    #(r'^exam/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/exam/mv/$',ajaxHandeler.ajax_Exam_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/attendance/$',ajaxHandeler.ajax_Attendance),
    (r'^api/attendance/(?P<id>\d+)/$',ajaxHandeler.ajax_Attendance),
    #(r'^attendance/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/attendance/mv/$',ajaxHandeler.ajax_Attendance_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/fees/$',ajaxHandeler.ajax_Fees),
    (r'^api/fees/(?P<id>\d+)/$',ajaxHandeler.ajax_Fees),
    #(r'^fees/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/fees/mv/$',ajaxHandeler.ajax_Fees_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/fund/$',ajaxHandeler.ajax_Fund),
    (r'^api/fund/(?P<id>\d+)/$',ajaxHandeler.ajax_Fund),
    #(r'^fund/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/fund/mv/$',ajaxHandeler.ajax_Fund_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/libbook/$',ajaxHandeler.ajax_LibBook),
    (r'^api/libbook/(?P<id>\d+)/$',ajaxHandeler.ajax_LibBook),
    #(r'^libbook/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/libbook/mv/$',ajaxHandeler.ajax_LibBook_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/leaves/$',ajaxHandeler.ajax_Leaves),
    (r'^api/leaves/(?P<id>\d+)/$',ajaxHandeler.ajax_Leaves),
    #(r'^leaves/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/leaves/mv/$',ajaxHandeler.ajax_Leaves_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/payroll/$',ajaxHandeler.ajax_PayRoll),
    (r'^api/payroll/(?P<id>\d+)/$',ajaxHandeler.ajax_PayRoll),
    #(r'^payroll/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/payroll/mv/$',ajaxHandeler.ajax_PayRoll_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/sport/$',ajaxHandeler.ajax_Sport),
    (r'^api/sport/(?P<id>\d+)/$',ajaxHandeler.ajax_Sport),
    #(r'^sport/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/sport/mv/$',ajaxHandeler.ajax_Sport_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/event/$',ajaxHandeler.ajax_Event),
    (r'^api/event/(?P<id>\d+)/$',ajaxHandeler.ajax_Event),
    #(r'^event/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/event/mv/$',ajaxHandeler.ajax_Event_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/discipline/$',ajaxHandeler.ajax_Discipline),
    (r'^api/discipline/(?P<id>\d+)/$',ajaxHandeler.ajax_Discipline),
    #(r'^discipline/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/discipline/mv/$',ajaxHandeler.ajax_Discipline_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/notice/$',ajaxHandeler.ajax_Notice),
    (r'^api/notice/(?P<id>\d+)/$',ajaxHandeler.ajax_Notice),
    #(r'^notice/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/notice/mv/$',ajaxHandeler.ajax_Notice_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/account/$',ajaxHandeler.ajax_Account),
    (r'^api/account/(?P<id>\d+)/$',ajaxHandeler.ajax_Account),
    #(r'^account/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/account/mv/$',ajaxHandeler.ajax_Account_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/instrument/$',ajaxHandeler.ajax_Instrument),
    (r'^api/instrument/(?P<id>\d+)/$',ajaxHandeler.ajax_Instrument),
    #(r'^instrument/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/instrument/mv/$',ajaxHandeler.ajax_Instrument_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/setting/$',ajaxHandeler.ajax_Setting),
    (r'^api/setting/(?P<id>\d+)/$',ajaxHandeler.ajax_Setting),
    #(r'^setting/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/setting/mv/$',ajaxHandeler.ajax_Setting_min_view),
)

