import pdb
from django.conf.urls import patterns, include, url
import os
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
from . import ajaxHandeler
urlpatterns = patterns('',)
TEMPLATE_DIRS =('',here('templates'),)

urlpatterns += patterns('',
    # Read Operation
    (r'^api/parent/$',ajaxHandeler.ajax_Parent),
    (r'^api/parent/(?P<id>\d+)/$',ajaxHandeler.ajax_Parent),
    #(r'^parent/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/parent/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Parent_Student),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/parent/aq/$',ajaxHandeler.ajax_Parent_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/parent/mv/$',ajaxHandeler.ajax_Parent_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/employee/$',ajaxHandeler.ajax_Employee),
    (r'^api/employee/(?P<id>\d+)/$',ajaxHandeler.ajax_Employee),
    #(r'^employee/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/employee/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_Employee_Subject),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/employee/(?P<id>\d+)/myclass/$',ajaxHandeler.ajax_Employee_MyClass),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/employee/(?P<id>\d+)/exam/$',ajaxHandeler.ajax_Employee_Exam),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/employee/aq/$',ajaxHandeler.ajax_Employee_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/employee/mv/$',ajaxHandeler.ajax_Employee_min_view),
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
    # Many2 many key Operations
    (r'^api/subject/(?P<id>\d+)/myclass/$',ajaxHandeler.ajax_Subject_MyClass),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/subject/(?P<id>\d+)/exam/$',ajaxHandeler.ajax_Subject_Exam),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/subject/(?P<id>\d+)/mark/$',ajaxHandeler.ajax_Subject_Mark),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/subject/aq/$',ajaxHandeler.ajax_Subject_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/subject/mv/$',ajaxHandeler.ajax_Subject_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/myclass/$',ajaxHandeler.ajax_MyClass),
    (r'^api/myclass/(?P<id>\d+)/$',ajaxHandeler.ajax_MyClass),
    #(r'^myclass/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/myclass/(?P<id>\d+)/employee/$',ajaxHandeler.ajax_MyClass_Employee),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/myclass/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_MyClass_Subject),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/myclass/(?P<id>\d+)/student/$',ajaxHandeler.ajax_MyClass_Student),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/myclass/(?P<id>\d+)/attendance/$',ajaxHandeler.ajax_MyClass_Attendance),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/myclass/aq/$',ajaxHandeler.ajax_MyClass_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/myclass/mv/$',ajaxHandeler.ajax_MyClass_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/exam/$',ajaxHandeler.ajax_Exam),
    (r'^api/exam/(?P<id>\d+)/$',ajaxHandeler.ajax_Exam),
    #(r'^exam/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/exam/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_Exam_Subject),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/exam/(?P<id>\d+)/employee/$',ajaxHandeler.ajax_Exam_Employee),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/exam/(?P<id>\d+)/mark/$',ajaxHandeler.ajax_Exam_Mark),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/exam/(?P<id>\d+)/result/$',ajaxHandeler.ajax_Exam_Result),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/exam/aq/$',ajaxHandeler.ajax_Exam_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/exam/mv/$',ajaxHandeler.ajax_Exam_min_view),
)


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
    (r'^api/student/(?P<id>\d+)/myclass/$',ajaxHandeler.ajax_Student_MyClass),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/mark/$',ajaxHandeler.ajax_Student_Mark),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/result/$',ajaxHandeler.ajax_Student_Result),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/attendance/$',ajaxHandeler.ajax_Student_Attendance),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/fees/$',ajaxHandeler.ajax_Student_Fees),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/student/(?P<id>\d+)/sport/$',ajaxHandeler.ajax_Student_Sport),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/student/aq/$',ajaxHandeler.ajax_Student_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/student/mv/$',ajaxHandeler.ajax_Student_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/mark/$',ajaxHandeler.ajax_Mark),
    (r'^api/mark/(?P<id>\d+)/$',ajaxHandeler.ajax_Mark),
    #(r'^mark/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/mark/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Mark_Student),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/mark/(?P<id>\d+)/subject/$',ajaxHandeler.ajax_Mark_Subject),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/mark/(?P<id>\d+)/exam/$',ajaxHandeler.ajax_Mark_Exam),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/mark/aq/$',ajaxHandeler.ajax_Mark_asearch),
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
    # Many2 many key Operations
    (r'^api/result/(?P<id>\d+)/exam/$',ajaxHandeler.ajax_Result_Exam),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/result/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Result_Student),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/result/aq/$',ajaxHandeler.ajax_Result_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/result/mv/$',ajaxHandeler.ajax_Result_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/attendance/$',ajaxHandeler.ajax_Attendance),
    (r'^api/attendance/(?P<id>\d+)/$',ajaxHandeler.ajax_Attendance),
    #(r'^attendance/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/attendance/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Attendance_Student),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/attendance/(?P<id>\d+)/myclass/$',ajaxHandeler.ajax_Attendance_MyClass),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/attendance/aq/$',ajaxHandeler.ajax_Attendance_asearch),
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
    # Many2 many key Operations
    (r'^api/fees/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Fees_Student),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/fees/aq/$',ajaxHandeler.ajax_Fees_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/fees/mv/$',ajaxHandeler.ajax_Fees_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/sport/$',ajaxHandeler.ajax_Sport),
    (r'^api/sport/(?P<id>\d+)/$',ajaxHandeler.ajax_Sport),
    #(r'^sport/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/sport/(?P<id>\d+)/student/$',ajaxHandeler.ajax_Sport_Student),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/sport/aq/$',ajaxHandeler.ajax_Sport_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/sport/mv/$',ajaxHandeler.ajax_Sport_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/account/$',ajaxHandeler.ajax_Account),
    (r'^api/account/(?P<id>\d+)/$',ajaxHandeler.ajax_Account),
    #(r'^account/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/account/(?P<id>\d+)/setting/$',ajaxHandeler.ajax_Account_Setting),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/account/aq/$',ajaxHandeler.ajax_Account_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/account/mv/$',ajaxHandeler.ajax_Account_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/setting/$',ajaxHandeler.ajax_Setting),
    (r'^api/setting/(?P<id>\d+)/$',ajaxHandeler.ajax_Setting),
    #(r'^setting/$',views.tt_home),
)


urlpatterns += patterns('',
    # Many2 many key Operations
    (r'^api/setting/(?P<id>\d+)/account/$',ajaxHandeler.ajax_Setting_Account),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/setting/aq/$',ajaxHandeler.ajax_Setting_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/setting/mv/$',ajaxHandeler.ajax_Setting_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/fund/$',ajaxHandeler.ajax_Fund),
    (r'^api/fund/(?P<id>\d+)/$',ajaxHandeler.ajax_Fund),
    #(r'^fund/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/fund/aq/$',ajaxHandeler.ajax_Fund_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/fund/mv/$',ajaxHandeler.ajax_Fund_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/book/$',ajaxHandeler.ajax_Book),
    (r'^api/book/(?P<id>\d+)/$',ajaxHandeler.ajax_Book),
    #(r'^book/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/book/aq/$',ajaxHandeler.ajax_Book_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/book/mv/$',ajaxHandeler.ajax_Book_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/event/$',ajaxHandeler.ajax_Event),
    (r'^api/event/(?P<id>\d+)/$',ajaxHandeler.ajax_Event),
    #(r'^event/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/event/aq/$',ajaxHandeler.ajax_Event_asearch),
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
    # Allowing advance search
    (r'^api/discipline/aq/$',ajaxHandeler.ajax_Discipline_asearch),
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
    # Allowing advance search
    (r'^api/notice/aq/$',ajaxHandeler.ajax_Notice_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/notice/mv/$',ajaxHandeler.ajax_Notice_min_view),
)


urlpatterns += patterns('',
    # Read Operation
    (r'^api/instrument/$',ajaxHandeler.ajax_Instrument),
    (r'^api/instrument/(?P<id>\d+)/$',ajaxHandeler.ajax_Instrument),
    #(r'^instrument/$',views.tt_home),
)


urlpatterns += patterns('',
    # Allowing advance search
    (r'^api/instrument/aq/$',ajaxHandeler.ajax_Instrument_asearch),
)


urlpatterns += patterns('',
    # Allowing Min View
    (r'^api/instrument/mv/$',ajaxHandeler.ajax_Instrument_min_view),
)

