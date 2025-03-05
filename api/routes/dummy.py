from fastapi import APIRouter
from backend.api.deps import PBClientDep


router = APIRouter(prefix="/dummy", tags=["dummy"])

@router.get("/")
def list_dummy(pb_client: PBClientDep):
    return pb_client.collection("users").get_list()
