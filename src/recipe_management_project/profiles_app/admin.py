from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# "_" is the recomended conventions for converting the string in the python to
# human readable text and the reason to do this it gets the passed through the
# translation engine.
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    # Works with test_users_listed in test_admin.py
    ordering = ['id']
    list_display = ['email', 'name']

    # customize the user admin fields set to support our custom user model
    # Works with test_user_change_page in test_admin.py
    fieldsets = (
        # Define the sections to update in the django admin
        # (title, {list of data items to modify: (items)})
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    # Customize the the user add admin fields to support custom user model
    # Works with test_create_user_page in test_admin.py
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


# If we use the default admin class, we dont have to pass the second parameter
# Here we modified the default admin class
admin.site.register(models.UserProfile, UserAdmin)
