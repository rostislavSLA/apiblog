from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an article to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the article
        return obj.author == request.user


class IsSubscriberOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow subscribers to view articles.
    """

    def has_permission(self, request, view):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to authenticated authors
        return request.user.is_authenticated and request.user.is_author


class IsPublicReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow public articles to be viewed.
    """

    def has_permission(self, request, view):
        # Read-only permissions are allowed for any request to public articles
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are not allowed for non-authenticated users
        return request.user.is_authenticated
