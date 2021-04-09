"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.core import XBlock
from web_fragments.fragment import Fragment
from xblock.fields import Integer, Scope, String

from pakx_feedback.utils import resource_string, render_template, json_response


class PakXFeedbackXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    has_score = True
    icon_class = 'problem'

    display_name = String(help='This name appears in horizontal navigation at the top of the page.',
                          default='PakistanX XYZ',
                          scope=Scope.content)
    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    # Context argument is specified for xblocks, but we are not using herein
    def student_view(self, context=None):  # pylint: disable=unused-argument
        """
        The primary view of the PakXFeedbackXBlock, shown to students
        when viewing courses.
        """

        html = render_template("static/html/pakx_feedback.html", {"self": self})
        fragment = Fragment(html.format(self=self))
        fragment.add_css(resource_string("static/css/pakx_feedback.css"))
        fragment.add_javascript(resource_string("static/js/src/pakx_feedback.js"))
        fragment.initialize_js('PakXFeedbackXBlock')
        return fragment

    # Context argument is specified for xblocks, but we are not using herein
    def studio_view(self, context):  # pylint: disable=unused-argument
        """
        Studio edit view
        """

        fragment = Fragment()
        fragment.add_content(render_template('static/html/pakx_feedback_edit.html', {'self': self}))
        fragment.add_javascript(resource_string('static/js/src/pakx_feedback_edit.js'))
        fragment.initialize_js('PakXFeedbackXBlockEdit')

        return fragment

    @XBlock.handler
    def get_state(self, request, suffix=''):
        dict_data = {"title": self.display_name}  # TODO UPDATE here
        return json_response(dict_data)

    @XBlock.json_handler
    def submit_grade(self, data, suffix=''):
        """
        Publish data for analytics purposes
        """
        data['max_value'] = 1.0

        self.runtime.publish(self, 'grade', data)
        return {'result': 'success'}

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        self.display_name = data.get('title')
        # TODO: FETCH other data as per requirements
        return {
            'result': 'success',
        }

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PakXFeedbackXBlock",
             """<pakx_feedback/>
             """),
            ("Multiple PakXFeedbackXBlock",
             """<vertical_demo>
                <pakx_feedback/>
                <pakx_feedback/>
                <pakx_feedback/>
                </vertical_demo>
             """),
        ]
