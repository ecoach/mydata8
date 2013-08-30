from django.db import models
from django.contrib.auth.models import User

# table format source data
from djangotailoring.models import SubjectData

# Create your models here.

# python ../manage.py makemtsmodel > MODEL.OUT (results go below here)
# matching version 1650

INT_APCOURSES_CHOICES = (
    ('1', 'Chemistry'),
    ('2', 'Biology'),
    ('3', 'Physics'),
    ('4', 'Calculus/Statistics'),
    ('5', 'Other AP/IB Course'),
)

INT_ATTENDANCE_CHOICES = (
    ('0', 'Never'),
    ('1', '1 to 5 times'),
    ('2', '5 to 10 times'),
    ('3', '10 or more times'),
    ('4', "I don't plan on attending lecture"),
)

INT_SLC_CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
    ('2', "What's an SLC study group?"),
)

INT_DISCUSSIONATTENDANCE_CHOICES = (
    ('0', 'Never'),
    ('1', '1 to 2 times'),
    ('2', '3 to 5 times'),
    ('3', 'More than 5 times'),
)

CTEXT_COLLEGE_CHOICES = (
    ('LSA', 'LSA'),
    ('Engineering', 'Engineering'),
    ('Kinesiology', 'Kinesiology'),
    ('Other', 'Other'),
)

INT_YESNO_CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
)

INT_CONFIDENCERANGE_CHOICES = (
    ('0', 'Not at all confident<br>0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', 'Extremely Confident<br>10'),
)

CTEXT_GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

CINT_SEMSESTERS_COMPLETED_CHOICES = (
    ('9', 'More than 8 semesters'),
)

CTEXT_COLLEGE_CONCENTRATE_CHOICES = (
    ('Engineering', 'Engineering'),
    ('Physics', 'Physics/Astrophysics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Biology_MCDB', 'Biology MCDB'),
    ('Biology_EEB', 'Biology EEB'),
    ('Health', 'Health-related Field (Physical Therapy, Pharmacology, Nursing, etc.)'),
    ('Humanities', 'Humanities'),
    ('Math', 'Mathematics'),
    ('Neurosci', 'Neuroscience'),
    ('Social_Science_not_Psych', 'Social Science (excluding Psychology)'),
    ('Psych_BBCS', 'Psychology or BBCS'),
    ('Education', 'Education'),
    ('IDK', 'I do not know'),
    ('Other', 'Other'),
)

CTEXT_POST_COLLEGE_CHOICES = (
    ('Employment', 'Employment'),
    ('Med_School', 'Medical School or other Health-related Professional School'),
    ('Dent_School', 'Dental School'),
    ('Education', 'Education (teaching, policy, or a certification program)'),
    ('Grad_Life_Sci', 'Graduate School in a Life Science discipline'),
    ('Grad_Other', 'Graduate School in another discipline'),
    ('IDK', "Unsure/I don't know"),
    ('Other', 'Other'),
)

INT_AGREEDISAGREE_CHOICES = (
    ('1', 'Agree'),
    ('0', 'Disagree'),
)

INT_INTERESTRANGE_CHOICES = (
    ('0', 'Not at all interested<br>0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', 'Extremely interested<br>10'),
)

CINT_GPA_CHOICES = (
    ('20', '2.0 or lower'),
    ('21', '2.1'),
    ('22', '2.2'),
    ('23', '2.3'),
    ('24', '2.4'),
    ('25', '2.5'),
    ('26', '2.6'),
    ('27', '2.7'),
    ('28', '2.8'),
    ('29', '2.9'),
    ('30', '3.0'),
    ('31', '3.1'),
    ('32', '3.2'),
    ('33', '3.3'),
    ('34', '3.4'),
    ('35', '3.5'),
    ('36', '3.6'),
    ('37', '3.7'),
    ('38', '3.8'),
    ('39', '3.9'),
    ('40', '4.0'),
)

CTEXT_EMPLOYMENT_STATUS_CHOICES = (
    ('No_Job', 'I do not have a job'),
    ('Part_Time', 'I work a part-time job (20 hours or less a week)'),
    ('Full_Time', 'I work a full-time job (more than 20 hours a week)'),
)

CTEXT_YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

CTEXT_INVOLVED_IN_CHOICES = (
    ('Greek', 'Greek Life (Sororities/Fraternities)'),
    ('Sports', 'Sports/Club Sports'),
    ('Religious', 'Religious Organizations'),
    ('Research', 'Research (Thesis, UROP, Lab work)'),
    ('Volunteering', 'Volunteering'),
    ('Music_Art', 'Music/Art'),
    ('Other', 'Other Student Clubs/Organzations'),
)

TEXT_CHEMREASON_CHOICES = (
    ('Possible_Concentrate_req', 'I am considering chemisrty as my concentration'),
    ('Concentration_req', 'Chemistry is required by my concentration'),
    ('Grad_req', 'I need this class to prepare for my graduate/professional program'),
    ('Credit', 'For a specific credit (NS, QR, etc.)'),
    ('Interest', "I'm taking this class because of my interest in chemistry"),
)

INT_HOURSSTUDY_CHOICES = (
    ('21', 'More than 20'),
)

CTEXT_CLASS_STANDING_CHOICES = (
    ('Freshman', 'Freshman'),
    ('Sophomore', 'Sophomore'),
    ('Junior', 'Junior'),
    ('Senior', 'Senior'),
)

INT_YCLASS_CHOICES = (
    ('1', 'Strongly Disagree<br>1'),
    ('2', '<br>2'),
    ('3', '<br>3'),
    ('4', '<br>4'),
    ('5', 'Strongly Agree<br>5'),
)

INT_TODO_CHOICES = (
    ('0', 'Not Done'),
    ('1', 'Done'),
)

INT_GRADE_DISTRIBUTION_CHOICES = (
    ('8', 'A'),
    ('7', 'A-'),
    ('6', 'B+'),
    ('5', 'B'),
    ('4', 'B-'),
    ('3', 'C+'),
    ('2', 'C'),
    ('1', 'C-'),
    ('0', 'D+ or lower'),
)

CINT_BDAY_MONTH_CHOICES = (
    ('-1', 'Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)

CTEXT_PARENT_ED_CHOICES = (
    ('Less_HS', 'Less than High School'),
    ('HS', 'High School/GED'),
    ('Some_College', 'Some College'),
    ('2_Year_College', '2-Year College Degree (Associates)'),
    ('4_Year_College', '4-Year College Degree (BA, BS)'),
    ('Masters', "Master's Degree"),
    ('Doctoral', 'Doctoral Degree'),
    ('Professional', 'Professional Degree (MD, JD)'),
)


class Source1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_source1'
    ChemPrevious = models.IntegerField(null=True, blank=True)
    Math_Confidence = models.IntegerField(null=True, blank=True)
    YClass09 = models.IntegerField(null=True, blank=True)
    CHEM130HoursStudy = models.IntegerField(null=True, blank=True)
    CHEM130OWLHours = models.IntegerField(null=True, blank=True)
    Mat_Textbook = models.IntegerField(null=True, blank=True)
    Mat_iClicker = models.IntegerField(null=True, blank=True)
    Mat_Calculator = models.IntegerField(null=True, blank=True)
    Exam_1_Score = models.IntegerField(null=True, blank=True)
    Exam_2_Score = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_01 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_02 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_11 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_12 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_03 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_04 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_05 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_06 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_07 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_08 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_09 = models.IntegerField(null=True, blank=True)
    Discussion_Quiz_10 = models.IntegerField(null=True, blank=True)
    OWL_Chap_01 = models.FloatField(null=True, blank=True)
    OWL_Chap_02 = models.FloatField(null=True, blank=True)
    OWL_Chap_03 = models.FloatField(null=True, blank=True)
    OWL_Chap_04 = models.FloatField(null=True, blank=True)
    OWL_Chap_05 = models.FloatField(null=True, blank=True)
    OWL_Chap_06 = models.FloatField(null=True, blank=True)
    OWL_Chap_07 = models.FloatField(null=True, blank=True)
    OWL_Chap_08 = models.FloatField(null=True, blank=True)
    OWL_Chap_09 = models.FloatField(null=True, blank=True)
    OWL_Chap_10 = models.FloatField(null=True, blank=True)
    OWL_Chap_11 = models.FloatField(null=True, blank=True)
    OWL_Chap_14 = models.FloatField(null=True, blank=True)
    OWL_Chap_15 = models.FloatField(null=True, blank=True)
    Participation_L01 = models.FloatField(null=True, blank=True)
    Participation_L02 = models.FloatField(null=True, blank=True)
    Participation_L03 = models.FloatField(null=True, blank=True)
    Participation_L04 = models.FloatField(null=True, blank=True)
    Participation_L05 = models.FloatField(null=True, blank=True)
    Participation_L06 = models.FloatField(null=True, blank=True)
    Participation_L07 = models.FloatField(null=True, blank=True)
    Participation_L08 = models.FloatField(null=True, blank=True)
    Participation_L09 = models.FloatField(null=True, blank=True)
    Participation_L10 = models.FloatField(null=True, blank=True)
    Participation_L11 = models.FloatField(null=True, blank=True)
    Participation_L12 = models.FloatField(null=True, blank=True)
    Participation_L13 = models.FloatField(null=True, blank=True)
    Participation_L14 = models.FloatField(null=True, blank=True)
    Participation_L15 = models.FloatField(null=True, blank=True)
    Participation_L16 = models.FloatField(null=True, blank=True)
    Participation_L17 = models.FloatField(null=True, blank=True)
    Participation_L18 = models.FloatField(null=True, blank=True)
    Participation_L19 = models.FloatField(null=True, blank=True)
    Participation_L20 = models.FloatField(null=True, blank=True)
    Participation_L21 = models.FloatField(null=True, blank=True)
    Participation_L22 = models.FloatField(null=True, blank=True)
    Participation_L23 = models.FloatField(null=True, blank=True)
    Participation_L24 = models.FloatField(null=True, blank=True)
    Participation_L25 = models.FloatField(null=True, blank=True)
    Participation_L26 = models.FloatField(null=True, blank=True)
    Participation_L27 = models.FloatField(null=True, blank=True)
    Participation_L28 = models.FloatField(null=True, blank=True)
    Participation_L29 = models.FloatField(null=True, blank=True)
    Participation_L30 = models.FloatField(null=True, blank=True)
    Participation_L31 = models.FloatField(null=True, blank=True)
    Participation_L32 = models.FloatField(null=True, blank=True)
    Participation_L33 = models.IntegerField(null=True, blank=True)
    Participation_L34 = models.FloatField(null=True, blank=True)
    Participation_L35 = models.FloatField(null=True, blank=True)
    Participation_L36 = models.FloatField(null=True, blank=True)
    Participation_L37 = models.FloatField(null=True, blank=True)
    Participation_L38 = models.FloatField(null=True, blank=True)
    Participation_L39 = models.FloatField(null=True, blank=True)
    Participation_L40 = models.FloatField(null=True, blank=True)
    Final_Exam_Score = models.IntegerField(null=True, blank=True)
    CHEM130Friends = models.IntegerField(null=True, blank=True)
    APCourses = models.IntegerField(null=True, blank=True)
    APCoursesTaken__1 = models.NullBooleanField()
    APCoursesTaken__2 = models.NullBooleanField()
    APCoursesTaken__3 = models.NullBooleanField()
    APCoursesTaken__4 = models.NullBooleanField()
    APCoursesTaken__5 = models.NullBooleanField()
    CHEM130SLC = models.IntegerField(null=True, blank=True)
    CHEM130Attendance = models.IntegerField(null=True, blank=True)
    ToDo_01 = models.IntegerField(null=True, blank=True)
    ToDo_02 = models.IntegerField(null=True, blank=True)
    ToDo_03 = models.IntegerField(null=True, blank=True)
    ToDo_04 = models.IntegerField(null=True, blank=True)
    ToDo_05 = models.IntegerField(null=True, blank=True)
    ToDo_06 = models.IntegerField(null=True, blank=True)
    ToDo_07 = models.IntegerField(null=True, blank=True)
    ToDo_08 = models.IntegerField(null=True, blank=True)
    ToDo_09 = models.IntegerField(null=True, blank=True)
    ToDo_10 = models.IntegerField(null=True, blank=True)
    CHEM130DiscussionAttendance = models.IntegerField(null=True, blank=True)
    CHEM130GoalGrade = models.IntegerField(null=True, blank=True)
    YClass26 = models.IntegerField(null=True, blank=True)
    YClass27 = models.IntegerField(null=True, blank=True)
    YClass28 = models.IntegerField(null=True, blank=True)
    YClass29 = models.IntegerField(null=True, blank=True)
    YClass30 = models.IntegerField(null=True, blank=True)
    YClass31 = models.IntegerField(null=True, blank=True)
    YClass38 = models.IntegerField(null=True, blank=True)
    YClass39 = models.IntegerField(null=True, blank=True)
    YClass40 = models.IntegerField(null=True, blank=True)
    YClass42 = models.IntegerField(null=True, blank=True)
    YClass43 = models.IntegerField(null=True, blank=True)
    YClass44 = models.IntegerField(null=True, blank=True)
    YClass45 = models.IntegerField(null=True, blank=True)
    YClass48 = models.IntegerField(null=True, blank=True)
    YClass47 = models.IntegerField(null=True, blank=True)
    YClass49 = models.IntegerField(null=True, blank=True)
    YClass50 = models.IntegerField(null=True, blank=True)
    YClass46 = models.IntegerField(null=True, blank=True)
    YClass41 = models.IntegerField(null=True, blank=True)
    YClass32 = models.IntegerField(null=True, blank=True)
    YClass33 = models.IntegerField(null=True, blank=True)
    YClass34 = models.IntegerField(null=True, blank=True)
    YClass35 = models.IntegerField(null=True, blank=True)
    YClass36 = models.IntegerField(null=True, blank=True)
    YClass37 = models.IntegerField(null=True, blank=True)
    YClass10 = models.IntegerField(null=True, blank=True)
    YClass11 = models.IntegerField(null=True, blank=True)
    YClass12 = models.IntegerField(null=True, blank=True)
    YClass18 = models.IntegerField(null=True, blank=True)
    YClass19 = models.IntegerField(null=True, blank=True)
    YClass20 = models.IntegerField(null=True, blank=True)
    YClass21 = models.IntegerField(null=True, blank=True)
    YClass22 = models.IntegerField(null=True, blank=True)
    YClass23 = models.IntegerField(null=True, blank=True)
    YClass24 = models.IntegerField(null=True, blank=True)
    YClass25 = models.IntegerField(null=True, blank=True)
    YClass13 = models.IntegerField(null=True, blank=True)
    YClass14 = models.IntegerField(null=True, blank=True)
    YClass15 = models.IntegerField(null=True, blank=True)
    YClass16 = models.IntegerField(null=True, blank=True)
    YClass17 = models.IntegerField(null=True, blank=True)
    YClass01 = models.IntegerField(null=True, blank=True)
    YClass03 = models.IntegerField(null=True, blank=True)
    YClass02 = models.IntegerField(null=True, blank=True)
    YClass04 = models.IntegerField(null=True, blank=True)
    YClass05 = models.IntegerField(null=True, blank=True)
    YClass06 = models.IntegerField(null=True, blank=True)
    YClass07 = models.IntegerField(null=True, blank=True)
    YClass08 = models.IntegerField(null=True, blank=True)
    CHEM130Reason__Possible_Concentrate_req = models.NullBooleanField()
    CHEM130Reason__Concentration_req = models.NullBooleanField()
    CHEM130Reason__Grad_req = models.NullBooleanField()
    CHEM130Reason__Credit = models.NullBooleanField()
    CHEM130Reason__Interest = models.NullBooleanField()
    CHEM130Confidence = models.IntegerField(null=True, blank=True)
    CHEM130GradeConfidence = models.IntegerField(null=True, blank=True)
    dist_ID = models.TextField(null=True, blank=True)
    CHEM130Interest = models.IntegerField(null=True, blank=True)
    Message_2_Q1 = models.IntegerField(null=True, blank=True)
    Message_2_Q2 = models.IntegerField(null=True, blank=True)
    Message_2_Q3 = models.IntegerField(null=True, blank=True)

class EmptySource(SubjectData):
    pass

class Common1(SubjectData):
    # add meta property
    class Meta: 
        db_table = 'mydata_common1'
    First_Name = models.CharField(max_length=20, null=True, blank=True)
    Last_Name = models.CharField(max_length=20, null=True, blank=True)
    uniqname = models.CharField(max_length=20, null=True, blank=True)
    Gender = models.CharField(max_length=1, choices=CTEXT_GENDER_CHOICES, null=True, blank=True)
    BirthDay = models.IntegerField(null=True, blank=True)
    BirthMo = models.IntegerField(null=True, blank=True)
    BirthYr = models.IntegerField(null=True, blank=True)
    Semesters_Completed = models.IntegerField(null=True, blank=True)
    College = models.CharField(max_length=11, choices=CTEXT_COLLEGE_CHOICES, null=True, blank=True)
    College_Other = models.CharField(max_length=30, null=True, blank=True)
    Concentrate__Engineering = models.NullBooleanField()
    Concentrate__Physics = models.NullBooleanField()
    Concentrate__Chemistry = models.NullBooleanField()
    Concentrate__Biology = models.NullBooleanField()
    Concentrate__Biology_MCDB = models.NullBooleanField()
    Concentrate__Biology_EEB = models.NullBooleanField()
    Concentrate__Health = models.NullBooleanField()
    Concentrate__Humanities = models.NullBooleanField()
    Concentrate__Math = models.NullBooleanField()
    Concentrate__Neurosci = models.NullBooleanField()
    Concentrate__Social_Science_not_Psych = models.NullBooleanField()
    Concentrate__Psych_BBCS = models.NullBooleanField()
    Concentrate__Education = models.NullBooleanField()
    Concentrate__IDK = models.NullBooleanField()
    Concentrate__Other = models.NullBooleanField()
    Concentrate_Other = models.CharField(max_length=30, null=True, blank=True)
    Declared = models.CharField(max_length=3, choices=CTEXT_YES_NO_CHOICES, null=True, blank=True)
    Class_Standing = models.CharField(max_length=9, choices=CTEXT_CLASS_STANDING_CHOICES, null=True, blank=True)
    Cum_GPA_Survey = models.IntegerField(null=True, blank=True)
    Employment = models.CharField(max_length=9, choices=CTEXT_EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    Involved_In__Greek = models.NullBooleanField()
    Involved_In__Sports = models.NullBooleanField()
    Involved_In__Religious = models.NullBooleanField()
    Involved_In__Research = models.NullBooleanField()
    Involved_In__Volunteering = models.NullBooleanField()
    Involved_In__Music_Art = models.NullBooleanField()
    Involved_In__Other = models.NullBooleanField()
    Other_Commitment = models.CharField(max_length=30, null=True, blank=True)
    Post_College = models.CharField(max_length=13, choices=CTEXT_POST_COLLEGE_CHOICES, null=True, blank=True)
    Parent_Ed = models.CharField(max_length=14, choices=CTEXT_PARENT_ED_CHOICES, null=True, blank=True)
    High_School_CumGPA = models.IntegerField(null=True, blank=True)


