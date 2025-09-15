from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    Read-only permissions are allowed to any request.
    """

    # def has_permission(self, request, view):
    #     # Allow read-only access for any request
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     # Otherwise, user must be authenticated
    #     return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the object
        # return obj.author.profile.user == request.user
        return obj.author.user == request.user