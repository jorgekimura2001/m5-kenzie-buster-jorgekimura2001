from rest_framework import permissions
from .models import User
from rest_framework.views import Request
import ipdb


class UserPermission(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view,
        user: User,
    ) -> bool:
        # ipdb.set_trace()
        if user == request.user:
            return True
        elif request.user.is_employee is True:
            return True
        else:
            return False
