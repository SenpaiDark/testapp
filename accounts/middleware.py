from django.shortcuts import redirect


class AdminGateMiddleware:
    """Block /panel/ unless the admin gate session key is set."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/panel/"):
            if not request.session.get("admin_authed"):
                return redirect("/admin/")
        return self.get_response(request)
