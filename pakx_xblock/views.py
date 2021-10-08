"""
Handle view logic for the XBlock
"""
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin


class ModalViewMixin(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for Image Modal XBlock instances
    """

    loader = ResourceLoader(__name__)

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context = dict(context)
        # TODO: Update Context
        context.update({
            'counter': self.count,
            'display_name': self.display_name,
            'user_mako_template': self.user_mako_template,
            'logo_img': self.runtime.local_resource_url(self, 'public/images/logo.png'),
        })
        return context

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            # TODO: Edit these as per XBlock Naming Convention
            ("PakXXBlock",
             """<pakx_xblock/>
             """),
            ("Multiple PakXXBlock",
             """<vertical_demo>
                <pakx_xblock/>
                <pakx_xblock/>
                <pakx_xblock/>
                </vertical_demo>
             """),
        ]
