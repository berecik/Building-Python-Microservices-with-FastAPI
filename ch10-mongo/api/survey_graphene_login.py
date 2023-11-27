from models.data.pccs_graphql import LoginData
from graphene import ObjectType, List, String, Schema, Field, Mutation, Boolean, Int
from repository.login import LoginRepository

from datetime import date, datetime
from json import dumps, loads
import os

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError(f"The type {type(obj)} not serializable.")
  
class LoginQuery(ObjectType):
    login_list = None
    get_login = Field(List(LoginData))
  
    async def resolve_get_login(self, info):
      repo = LoginRepository()
      login_list = await repo.get_all_login()
      print(login_list)
      return login_list

   
class CreateLoginData(Mutation):
    class Arguments:
      id = Int(required=True)
      username = String(required=True)
      password = String(required=True)

    ok = Boolean()
    loginData = Field(lambda: LoginData)

    async def mutate(self, info, id, username, password):
        
        login_dict = {"id": id, "username": username, "password": password}
        login_json = dumps(login_dict, default=json_serial)
        repo = LoginRepository()
        result = await repo.add_login(loads(login_json))
        ok = result is not None
        return CreateLoginData(loginData=result, ok=ok)

class ChangeLoginPassword(Mutation):
    class Arguments:
      username = String(required=True)
      password = String(required=True)

    ok = Boolean()
    loginData = Field(lambda: LoginData)

    async def mutate(self, info, username, password):
                
        repo = LoginRepository()
        result = await repo.change_password(username, password)

        ok = result is not None
        return CreateLoginData(loginData=result, ok=ok)
      
class DeleteLoginData(Mutation):
    class Arguments:
      id = Int(required=True)
      
    ok = Boolean()
    loginData = Field(lambda: LoginData)

    async def mutate(self, info, id):
                
        repo = LoginRepository()
        result = await repo.delete_login(id)

        ok = result is not None
        return DeleteLoginData(loginData=result, ok=ok)


class LoginMutations(ObjectType):
    create_login = CreateLoginData.Field()
    edit_login = ChangeLoginPassword.Field()
    delete_login = DeleteLoginData.Field()
      
schema = Schema(query=LoginQuery, mutation=LoginMutations,
    auto_camelcase=False,)