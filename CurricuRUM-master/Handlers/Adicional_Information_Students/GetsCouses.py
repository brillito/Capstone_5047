from flask_restful import Resource, Api
from flask import Flask, request
from flask_jwt import JWT, jwt_required



#Devuelve las clases  de la socioHumanistica
class SocioHumanistics(Resource):
    def get(self):
        ResultSocioHumanistic = request.get_json()# busco la clases que tiene en socioHumanisticas
        courseHumanistis=[]
        if len(ResultSocioHumanistic) ==0:
            return {'Not found '},404
        for course in ResultSocioHumanistic:
            courseHumanistis.append(course)
        return {courseHumanistis},201

#Devuelve el cretido de la socioHumanistica
class SocioHumanistic (Resource):
    def get(self):
        data = request.get_json()  # aqui  escogo los parametros de lo que la codificacion de la clase
        # se lo envio al query par aque me traiga:
        # el nomber del curso
        # codificacion del curso
        # la nota del curso
        return {data},201

# Devuelve el total de cretidos que tiene aprovado en sociohumanisticas
class SocioHumanistic_AllCredits(Resource):
    def get(self):
        Credits=[]
        count=0
        if len(Credits==0):
            return {'Not found '}, 404
        # llamo a la tabla que me den todos los creditos de las socio humanisticas  o todas las humanisticas
        for credits in Credits :
            count +=credits
        return { "Total of credits" :credits}

#Devuelve el cretido de las Electiva
class Elective(Resource):
    def get(self):
        data = request.get_json()  # aqui  escogo los parametros de lo que la codificacion de la clase
        # se lo envio al query par aque me traiga:
        # el nomber del curso
        # codificacion del curso
        # la nota del curso
        return {data},201


#Devuelve las clases  de la Electrivas LIbres
class Electives(Resource):
    def get(self):
        ResultElectives = request.get_json()# busco la clases que tiene en socioHumanisticas
        courseElectives=[]
        if len(ResultElectives) ==0:
            return {'Not found '},404
        for course in ResultElectives:
            courseElectives.append(course)
        return {courseElectives},201

# Devuelve el total de cretidos que tiene aprovado en Electivas Libres
class Electives_AllCredits(Resource):
    def get(self):
        Credits = []
        count=0
        if len(Credits == 0):
            return {'Not found '}, 404
        # llamo a la tabla que me den todos los creditos de las socio humanisticas  o todas las humanisticas
        for credits in Credits :
            count +=credits
        return { "Total of credits" :credits},201

#Devuelve los creditos y la clase profesional
class ProfessionalElective(Resource):
    def get(self):
        data = request.get_json()  # aqui  escogo los parametros de lo que la codificacion de la clase
        # se lo envio al query par aque me traiga:
        # el nomber del curso
        # codificacion del curso
        # la nota del curso
        return {data},201


 # Devuelve el total de cretidos que tiene aprovado en Profesionales
class Professional_AllCredits(Resource):
    def get(self):
        Credits = []
        count=0
        if len(Credits == 0):
            return {'Not found '}, 404
        # llamo a la tabla que me den todos los creditos de las socio humanisticas  o todas las humanisticas
        for credits in Credits :
            count +=credits
        return { "Total of credits" :credits},201

#Devuelve las clases  de la profesionales
class ProfessionalElectives(Resource):
    def get(self):
        ResultProfessional = request.get_json()# busco la clases que tiene en socioHumanisticas
        courseProfessional=[]
        if len(ResultProfessional) ==0:
            return {'Not found '},404
        for course in ResultProfessional:
            courseProfessional.append(course)
        return {courseProfessional},201
