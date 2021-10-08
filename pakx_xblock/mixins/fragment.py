"""
Mixin fragment/html behavior into XBlocks

Note: We should resume test coverage for all lines in this file once
split into its own library.
"""
from django.template.context import Context
from xblock.core import XBlock
from xblock.fragment import Fragment


class XBlockFragmentBuilderMixin:
    """
    Create a default XBlock fragment builder
    """
    static_css = [
        'view.css',
    ]
    static_js = [
        'view.js',
    ]
    static_js_init = 'ModalView'
    template = 'view.html'
    mako_template = 'view_mako.html'

    def provide_context(self, context):  # pylint: disable=no-self-use
        """
        Build a context dictionary to render the student view

        This should generally be overriden by child classes.
        """
        context = context or {}
        context = dict(context)
        return context

    @XBlock.supports('multi_device')
    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """

        data = {
            'template': self.template,
            'js_init': self.static_js_init,
            'static_js': self.static_js or [],
            'mako_template': self.mako_template,
            'static_css': self.static_css or [],
            'context': self.provide_context(context),
        }

        fragment = self.build_fragment(data)
        return fragment

    def build_fragment(self, data):
        """
        Creates a fragment for display.
        """

        css = data.pop('static_css')
        js = data.pop('static_js')
        js_init = data.pop('js_init')
        rendered_template = self.get_rendered_template(data)
        fragment = Fragment(rendered_template)
        for item in css:
            fragment.add_css_url(self.get_local_for_resource_url(item, 'css'))

        for item in js:
            fragment.add_javascript_url(self.get_local_for_resource_url(item, 'src'))
        if js_init:  # pragma: no cover
            fragment.initialize_js(js_init)
        return fragment

    def get_rendered_template(self, data):
        """
        get rendered template based upon user's selection between Django & Mako
        :param data: (dict) data dict

        :return: rendered template
        """
        context = data.pop('context')
        use_mako_template = context.pop('user_mako_template', False)
        template = data.pop('template', None)
        if template and not use_mako_template:
            return self.loader.render_django_template('templates/{}'.format(template), context=Context(context))
        mako_template = data.pop('mako_template', None)
        if mako_template:
            return self.loader.render_mako_template('templates/{}'.format(mako_template), context=context)
        return ''

    def get_local_for_resource_url(self, item, item_type):
        """
        get local URL for given item and type

        :param item: (str) item source in str form
        :param item_type: (str) css or src

        :return: (str) url
        """

        if item.startswith("/") or item.startswith("http"):
            return item
        relative_path = 'public/{}/{}'.format(item_type, item)
        return self.runtime.local_resource_url(self, relative_path)
