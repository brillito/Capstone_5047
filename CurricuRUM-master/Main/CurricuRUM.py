from flask_restful import Resource, Api
from flask import Flask, render_template
from flask_jwt import JWT
from Login_SIgnUp.Security import authenticate,identity

# administrator
from Handlers.Administrator_API.admi_api import Create_Curriculum
from Handlers.Administrator_API.admi_api import Test_ViewCourses
from Handlers.Administrator_API.admi_api import Upload_Grades
from Handlers.Administrator_API.admi_api import Edit_Curriculum
from Handlers.Administrator_API.admi_api import View_Curriculums
from Handlers.Administrator_API.admi_api import View_Curriculum
from Handlers.Administrator_API.admi_api import Create_VersionCurriculum
from Handlers.Administrator_API.admi_api import Edit_CurriculumVersion

#super administrator
from Handlers.Super_Administrator_API.Super_api import Super_Administrator
from Handlers.Super_Administrator_API.Super_api import SuperTest_ViewCourses

#Students
from Handlers.Student_API.student_api import Plan_Next_Semester
from Handlers.Student_API.student_api import Student_Curriculum
from Handlers.Student_API.student_api import Course_Description
from Handlers.Adicional_Information_Students.GetsCouses import Professional_AllCredits
from Handlers.Adicional_Information_Students.GetsCouses import Electives_AllCredits
from Handlers.Adicional_Information_Students.GetsCouses import SocioHumanistic_AllCredits
from Handlers.Student_API.student_api import Course_OpenOtherCourse



app = Flask (__name__)
app.secret_key= 'Upr@2018_C@sptone_Fall@2018'
api = Api(app)

jwt =JWT(app, authenticate ,identity)
#------------------------------------------ HOME Page ------------------------------------------------------------------
# Aqui estara la pagina principal del programa
class HomePage (Resource):
    def get(self):
        return {render_template : ""}




#-------------------------------------------------Routes ---------------------------------------------------------------
api.add_resource(HomePage,'/')

api.add_resource(SignIn,'/CurricuRUM/Login/<string: email>/<string:password>')
api.add_resource(Register,'/CurricuRUM/Login/<string: Name>/<string:LastName>/<string: Email>/<string: StudentNumber>/<string: Password>')


api.add_resource(Create_Curriculum,'/CurricuRUM/Administrator/Create_Curriculum/<string: Coursecode>/<string:courseName>/<string: credits>/<string:Semester>/<string:Year>/<string; categoria>/<string:pre-requisitos>/<string: co-requisitos>')
api.add_resource(Edit_CurriculumVersion,'/CurricuRUM/Administrator/Edit_CurriculumVersion/<string: semester>/<string: year>')
api.add_resource(Edit_Curriculum, '/CurricuRUM/Administrator/Edit_Curriculum/<string:courseId>/<string:pre-requisito>/<string:co-requisito>')#preguntar
api.add_resource(Upload_Grades,'/CurricuRUM/SuperAdministrator/Upload_Grades/<string: file>')
api.add_resource(View_Curriculums,'/CurricuRUM/Administrator/View_Curriculums')
api.add_resource(View_Curriculum,'/CurricuRUM/Administrator/View_Curriculum/<string: semester>/<string: year>')
api.add_resource(Create_VersionCurriculum,'/CurricuRUM/Administrator/Create_VersionCurriculum/<string: program>/<string:year>/<string:semester>/<string:category>/<string: credits>')


api.add_resource(Super_Administrator, '/CurricuRUM/SuperAdmisnistration/Add_DeleteAdministration/<string:email>')

api.add_resource(Student_Curriculum,'/Curriculum/Student/ShowCurriculum/<int:Id>')
api.add_resource(Plan_Next_Semester,'/Curriculum/Student/Plan Next Semester/<int:Id>')
api.add_resource(Course_Description,'/Curriculum/Student/Course_Description/<string:CourseCode>')

#to get credits only
api.add_resource(Electives_AllCredits,'/Curriculum/Student/Electives_AllCredits')
api.add_resource(SocioHumanistic_AllCredits,'/Curriculum/Student/SocioHumanistic_AllCredits')
api.add_resource(Professional_AllCredits,'/Curriculum/Student/Professional_AllCredits')

#addicionales (optional -student)
api.add_resource(SuperTest_ViewCourses,'/CurricuRUM/SuperAdministrator/Test_ViewCourses')
api.add_resource(Test_ViewCourses,'/CurricuRUM/Administrator/Test_ViewCourses')  # esto es pueba








#---------------------------------------------Main of the app-----------------------------------------------------------
app.run(port=5000, debug= True) # error message for a html page