from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Bids
from repository.bids import BidsRepository
from models.request.bids import BidsReq
from db_config.sqlalchemy_connect import sess_db
from security.secure import authenticate

router = APIRouter()

@router.post("/bid/add", dependencies=[Depends(authenticate)])
def add_bid(req: BidsReq, sess:Session = Depends(sess_db)): 
    bid_dict = req.dict(exclude_unset=True)
    repo:BidsRepository = BidsRepository(sess)
    bid = Bids(**bid_dict)
    result = repo.insert_bid(bid)
    if result == True:
        return bid
    else: 
        return JSONResponse(content={'message':'create bid problem encountered'}, status_code=500)   

@router.patch("/bid/update", dependencies=[Depends(authenticate)])
def update_bid(id:int, req: BidsReq, sess:Session = Depends(sess_db)): 
    bid_dict = req.dict(exclude_unset=True)
    repo:BidsRepository = BidsRepository(sess)
    if result := repo.update_bid(id, bid_dict):
        return JSONResponse(content={'message':'bid updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message':'update bid error'}, status_code=500)


@router.delete("/bid/delete/{id}", dependencies=[Depends(authenticate)])
def delete_bid(id:int, sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    if result := repo.delete_bid(id):
        return JSONResponse(content={'message':'auction updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message':'update auction error'}, status_code=500)

@router.get("/bid/all", dependencies=[Depends(authenticate)])
def list_all_bid(sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    return repo.get_all_bids()  

@router.post("/bid/{id}", dependencies=[Depends(authenticate)])
def get_bid(id:int, sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    return repo.get_bid(id)  
