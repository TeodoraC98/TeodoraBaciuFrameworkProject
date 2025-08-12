from django.shortcuts import redirect
from django.contrib.auth.models import Group
class RoleBasedAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_staff and not request.user.is_superuser:
            if not request.user.groups.filter(name='Admin').exists():
                if not request.path.startswith('/no-permission'):
                    return redirect('/no-permission/')
        response = self.get_response(request)
        return response