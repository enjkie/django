from ..common.router import Router
from .service import get_users, post_users

__router = Router()



get_req = __router.get('', get_users)

post_req = __router.post('', post_users)

UserRouter = __router._routes