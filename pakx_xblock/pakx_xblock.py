"""TO-DO: Write a description of what this XBlock is."""

from xblock.core import XBlock
from pakx_xblock.utils import json_response
from .XBlockFields import XBlockFieldsMixin
from .views import ModalViewMixin


# Edit the name of XBlock Class as per your requirement
class PakXXBlock(XBlockFieldsMixin, ModalViewMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # TODO: Call this function as per requirement
    def submit_grade(self):
        """
        Publish data for analytics purposes
        """

        self.runtime.publish(self, "grade", {'max_value': 1.0, 'value': 1.0})
        return {'result': 'success'}

    @XBlock.handler
    def get_state(self, request, suffix=''):  # pylint: disable=unused-argument
        dict_data = {"title": self.display_name}  # UPDATE here as per XBlock data
        return json_response(dict_data)

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):  # pylint: disable=unused-argument
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}
