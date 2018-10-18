from flask_restful import Resource, Api
from flask import Flask, request



################################################################
#                                                              #
#           Show Curriculum to the Student                     #
#                                                              #
################################################################

#Se vera todo el curriculo
class Student_Curriculum(Resource):
    def get(self,Student_Id):
        showCurriculum=[]
        mapped_Curriculum=[] #llamo al query para que me traiga el curriculum del estudiante
        for course in mapped_Curriculum:
            showCurriculum.append(course)
        return {'Curriculum:', showCurriculum},201


# Devuelve la descripcion del curso ( nombre del curson, pre,co requisitos y los creditos)
class Course_Description(Resource):
    def get(self,CourseCode):
        # escogo el argumento
        courseDescription='' # se lo envio a query
        return {courseDescription},201

# Devuelve la nota de un curso en especifico
class TakeGrade_Course(Resource):
    def get(self):
        data = request.get_json() # aqui  escogo los parametros de lo que la codificacion de la clase
        # se lo envio al query par aque me traiga:
        if data['Grade']== " ":
            return{"message": "not taken "},404
        if data['Grade '] == "R":
            return {"message": "in process "}, 404
            # el nomber del curso
            #codificacion del curso
            # la nota del curso
        return {data}

################################################################
#                                                              #
#           Plan Next Semester                                 #
#                                                              #
################################################################

class Plan_Next_Semester(Resource):
    def get(self,Student_Id): # la parte para el semester
        PlanNextSemester= []
        return PlanNextSemester , 201  # esto es para saber que el item se hizo


class Course_OpenOtherCourse(Resource):
    def get(self,courseId):
        DropCourse= []
        # le envio la clase al query
        # que busque cuales que son pre-requisito de ella
        return {DropCourse}