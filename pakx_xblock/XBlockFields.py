"""
Handle data access logic for the XBlock
"""
from django.utils.translation import ugettext_lazy as _
from xblock.fields import Scope
from xblock.fields import String, Integer, Boolean


class XBlockFieldsMixin:  # pylint: disable=too-few-public-methods
    """
    Handle data access for Image Modal XBlock instances
    """

    has_score = True
    icon_class = 'problem'

    # TODO: Update Editable fields via Studio
    editable_fields = [
        'display_name',
        'user_mako_template'
    ]

    show_in_read_only_mode = True

    # TODO: UPDATE Fields as per requirements
    display_name = String(
        display_name=_('Display Name'),
        default='Modal XBlock',
        scope=Scope.settings,
        help=_("This is the XBlock's display name"),
    )

    user_mako_template = Boolean(
        display_name=_('Use Mako Template'),
        default=True,
        scope=Scope.settings,
        help=_("Default Django Templating Engine is used"),
    )

    count = Integer(
        display_name=_("Counter"),
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
