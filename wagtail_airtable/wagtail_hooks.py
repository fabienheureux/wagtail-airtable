from django.urls import reverse
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


@hooks.register("register_settings_menu_item")
def register_airtable_setting():
    return MenuItem(
        "Airtable Import",
        reverse("airtable_import_listing"),
        classnames="icon icon-cog",
        order=1000,
    )
