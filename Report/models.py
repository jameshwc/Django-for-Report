from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    def has_permission(request):
        if 'username' in request.session:
            user = User.objects.get(id=request.session['uid'])
            if user.student_id.lower() == "b07902001":
                return True
        return False

admin_site = MyAdminSite(name='myadmin')