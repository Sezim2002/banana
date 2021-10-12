from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        """Срабатывает при дейстриях, в которых не нужен конкретный объект:
        list и create."""
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Срабатывает при действиях, в которых используется один конкретный объект:
        retrieve, update, delete.
        Всегда срабатывает после верхнего метода"""
        if request.method in SAFE_METHODS:
            return True
        return request.user and (request.user == obj.user or request.user.is_staff)


class IsAuthor(BasePermission):
    # работа с одним объектом
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user == obj.user)
