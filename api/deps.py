from typing import Annotated

from fastapi import Depends, HTTPException

from backend.core.config import settings
from pocketbase import PocketBase 

from cachetools import cached, TTLCache


@cached(cache=TTLCache(maxsize=1024, ttl=300))
def __get_pb_client():
    print("getting pb client")
    client = PocketBase(settings.PB_URL)
    admin_data = client.admins.auth_with_password(settings.PB_USERNAME, settings.PB_PASSWORD)
    if not admin_data.is_valid:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return client


def get_pb_client() -> PocketBase:
    return __get_pb_client()


PBClientDep = Annotated[PocketBase, Depends(get_pb_client)]
