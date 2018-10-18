from flask_restful import Resource, Api
from flask import Flask, request
from flask_jwt import JWT, jwt_required
import sqlite3
courses=[]
versions_Curriculum= []
emails=[]
showCurriculum=[]
################################################################
#                                                              #
#           Upload the grades                                  #
#                                                              #
################################################################

class Upload_Grades(Resource):
    def put(self,file):
        courseName = request.get_json()
        course = next(filter(lambda x: x['courseName'] == courseName, courses), None)
        print("course", course)
        data = request.get_json()
        if course is None:
            print(data)
            course = {'courseName': courseName, 'pre-requisito': data['pre-requisito'],
                      'co-requisito': data['co-requisito']}
            print(courses.append(course))
        else:
            course.update(data)
        return course, 201
################################################################
#                                                              #
#           Edit a Curriculum Administrator                    #
#                                                              #
################################################################

class Edit_Curriculum (Resource):
    @jwt_required
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

class Edit_CurriculumVersion (Resource):
    def get(self):
        pass

    def put(self):
        pass
################################################################
#                                                              #
#           Creating a  Version Curriculum Administrator       #
#                                                              #
################################################################

class Create_VersionCurriculum(Resource):
    def post(self):
        pass
################################################################
#                                                              #
#           Creating a Curriculum Administrator                #
#                                                              #
################################################################

class Create_Curriculum (Resource):# copy with a things changes
    @jwt_required()
    def get(self,):
        '''
        course= next(filter(lambda x: x ['courseName']== courseName ,courses),None)# default value
        return {'Course' : course}, 200 if course else 404 # aqui pongo el static code de error'''

    def post(self):
        courseName = request.get_json()
        if next(filter(lambda x: x ['courseName']== courseName ,courses),None) is not None:
            return {'message': "This course '{}'already exits.".format(courseName)}, 400# bad request
        data= request.get_json()
        print (data)
        course = {'courseName': courseName , 'pre-requisito': data['pre-requisito'], 'co-requisito':data['co-requisito']}
        courses.append(course)
        return course, 201 # esto es para saber que el item se hizo


    def delete(self):
        courseName = " "
        global  courses  # esto es como un this en java
        courses = list (filter(lambda x :x['courseName'] != courseName,courses))
        return {'message': 'course deleted'}, 201


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

# Test
class Test_ViewCourses(Resource):
    def get(self):
        return{'courses':courses}

################################################################
#                                                              #
#           View Curriculum                                    #
#                                                              #
################################################################
class View_Curriculums (Resource):
    def get(self):
        return {"Versions":versions_Curriculum}, 200 if versions_Curriculum else 404

    def get(self):
       data= request.get_json()
       year = data['year']
       semester = data['semester']
       Version = next(filter(lambda x: x['year'] == year and x['semester']== semester, versions_Curriculum), None)  # default value
       return {'Version': Version}, 200 if Version else 404  # aqui pongo el static code de error

class View_Curriculum (Resource):
    def get(self,year,semester):
        pass