from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from models.requests.signup import SignupReq
from models.data.sqlalchemy_models import Signup
from repository.sqlalchemy.signup import SignupRepository, LoginMemberRepository, MemberAttendanceRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/signup/add")
def add_signup(req: SignupReq, sess:Session = Depends(sess_db)):
    repo:SignupRepository = SignupRepository(sess)
    signup = Signup(password= req.password, username=req.username,id=req.id)
    result = repo.insert_signup(signup)
    if result == True:
        return signup
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

@router.get("/signup/list", response_model=List[SignupReq])
def list_signup(sess:Session = Depends(sess_db)):
    repo:SignupRepository = SignupRepository(sess)
    return repo.get_all_signup()

@router.patch("/signup/update")
def update_signup(id:int, req: SignupReq, sess:Session = Depends(sess_db) ):
    signup_dict = req.dict(exclude_unset=True)
    repo:SignupRepository = SignupRepository(sess)
    if result := repo.update_signup(id, signup_dict):
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message':'update profile error'}, status_code=500)
    

@router.delete("/signup/delete/{id}")
def delete_signup(id:int, sess:Session = Depends(sess_db) ):
    repo:SignupRepository = SignupRepository(sess)
    if result := repo.delete_signup(id):
        return JSONResponse(content={'message':'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message':'delete profile error'}, status_code=500)
    
@router.get("/signup/list/{id}", response_model=SignupReq)
def get_signup(id:int, sess:Session = Depends(sess_db)): 
    repo:SignupRepository = SignupRepository(sess)
    return repo.get_signup(id)

@router.get("/login/memberslist")
def get_join_login_members(sess:Session = Depends(sess_db)): 
    repo:LoginMemberRepository = LoginMemberRepository(sess)
    return repo.join_login_members()

@router.get("/member/attendance")
def get_join_member_attendance(sess:Session = Depends(sess_db)): 
    repo:MemberAttendanceRepository = MemberAttendanceRepository(sess)
    return repo.join_member_attendance()
