from flask_restful import Resource, Api
from flask import Flask, request,render_template
from flask_jwt import JWT, jwt_required
# resource what an api can return
#utilizando flask-restful regresa json

app = Flask (__name__)
api = Api(app)


courses=[]
versions_Curriculum= []
emails=[]
showCurriculum=[]
################################################################
#                                                              #
#           Upload the grades                                  #
#                                                              #
################################################################

class SuperUpload_Grades(Resource):
    def put(self,file):
        pass
################################################################
#                                                              #
#           Edit a Curriculum Administrator                    #
#                                                              #
################################################################

class SuperEdit_Curriculum(Resource):
    def get(self):
        courseName = request.get_json()
        course= next(filter(lambda x: x ['courseName']== courseName ,courses),None)# default value
        return {'Course' : course}, 200 if course else 404 # aqui pongo el static code de error

    def put(self):
        courseName = request.get_json()
        course = next(filter(lambda x: x['courseName'] == courseName, courses), None)
        print("course",course)
        data = request.get_json()
        if course is None:
            print(data)
            course = {'courseName': courseName , 'pre-requisito': data['pre-requisito'], 'co-requisito':data['co-requisito']}
            print(courses.append(course))
        else:
            course.update(data)
        return course, 201

################################################################
#                                                              #
#           Creating a Curriculum Administrator                #
#                                                              #
################################################################

class SuperCreate_Curriculum (Resource):# copy with a things changes
    def get(self,courseName):
        course= next(filter(lambda x: x ['courseName']== courseName ,courses),None)# default value
        return {'Course' : course}, 200 if course else 404 # aqui pongo el static code de error

    def post(self,courseName):
        if next(filter(lambda x: x ['courseName']== courseName ,courses),None) is not None:
            return {'message': "This course '{}'already exits.".format(courseName)}, 400# bad request
        data= request.get_json()
        print (data)
        course = {'courseName': courseName , 'pre-requisito': data['pre-requisito'], 'co-requisito':data['co-requisito']}
        courses.append(course)
        return course, 201 # esto es para saber que el item se hizo

    def delete(self, courseName):
        global  courses  # esto es como un this en java
        courses = list (filter(lambda x :x['courseName'] != courseName,courses))
        return {'message': 'course deleted'}, 201

    def put(self,courseName):
        course = next(filter(lambda x: x['courseName'] == courseName, courses), None)
        print("course",course)
        data = request.get_json()
        if course is None:
            print(data)
            course = {'courseName': courseName , 'pre-requisito': data['pre-requisito'], 'co-requisito':data['co-requisito']}
            print(courses.append(course))
        else:
            course.update(data)
        return course, 201

# Test
class SuperTest_ViewCourses(Resource):
    def get(self):
        return{'courses':courses}

################################################################
#                                                              #
#           View Curriculum                                    #
#                                                              #
################################################################
class SuperView_Curriculums (Resource):
    def get(self):
        return {"Versions":versions_Curriculum}, 200 if versions_Curriculum else 404

    def get(self,year,sems):
        Version = next(filter(lambda x: x['year'] == year and x['semester']== sems, versions_Curriculum), None)  # default value
        return {'Version': Version}, 200 if Version else 404  # aqui pongo el static code de error

################################################################
#                                                              #
#           Super Administrator                                #
#                                                              #
################################################################

class Super_Administrator (Resource):
    def post(self):
        email= request.get_json()
        print(email)
        if next(filter(lambda x: x['email'] == email, emails), None) is not None:
            return {'message': "This email '{}'already exits.".format(email)}, 400  # bad request
        Email= {'email': email}
        emails.append(Email)
        return Email, 201  # esto es para saber que el item se hizo

    def delete(self):
        global emails # esto es como un this en java
        email=request.get_json()
        Email = {'email': email}
        if  len(emails)==0:
            return {'message':'There are no emails'}
        elif (Email in emails):
            emails = list(filter(lambda x: x['email'] != email, emails))
            return {'message': 'email deleted'},201
        else:
            return {'message': "This email '{}'does not exists.".format(email)}, 400  # bad request

    def get(self):
        return {'Emails': emails }, 200 if emails else 404