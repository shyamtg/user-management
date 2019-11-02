from flask_restful import Resource
from flask import request, jsonify
from models import UserData, user_schema, db, user_schema_list
from flask_api import status
from flask import Response
from sqlalchemy import exc

class UserDataManagement(Resource):
    """
    This class holds the code for handling user data management
    """
    def get(self):
        users = UserData.query.all()
        response = user_schema_list.jsonify(users)
        response.status_code = status.HTTP_200_OK
        return response

    def post(self):
        self.error_message = {}
        mandatory_fields = ['first_name','email','phone_number','dob']
        for field in mandatory_fields:
            if field not in request.json:
                self.error_message[field] = 'This field is required'
        if self.error_message:
            response = jsonify(self.error_message)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response
        try:
            first_name = request.json['first_name']
            last_name = request.json.get('last_name', None)
            email = request.json['email']
            phone_number = request.json['phone_number']
            dob = request.json['dob']
            new_entry = UserData(first_name,last_name,email,phone_number,dob)
            db.session.add(new_entry)
            db.session.commit()
            response = user_schema.jsonify(new_entry)
            response.status_code = status.HTTP_201_CREATED
            return response
        except exc.IntegrityError as e:
            self.error_message["message"] = str(e.orig)
            response = jsonify(self.error_message)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response
        except Exception as e:
            self.error_message["message"] = "Something went wrong"
            response = jsonify(self.error_message)
            response.status_code = status.HTTP_501_NOT_IMPLEMENTED
            return response