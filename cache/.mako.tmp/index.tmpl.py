# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499745900.257
_enable_loop = True
_template_filename = u'themes/planetoid/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="postindex">\n')
        for post in posts:
            __M_writer(u'    <article class="h-entry" style="border: 2px solid darkgrey; margin-bottom: 12px; border-radius: 4px; padding:12px; overflow: auto;">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(unicode(post.meta('link')))
            __M_writer(u'" class="u-url">')
            __M_writer(unicode(post.title()))
            __M_writer(u'</h1></a>\n        <div class="metadata">\n            <p class="dateline"><a href="')
            __M_writer(unicode(post.meta('link')))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'" itemprop="datePublished" title="')
            __M_writer(unicode(messages("Publication date")))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time></a></p>\n        </div>\n    </header>\n    <div class="p-summary entry-summary">\n    ')
            __M_writer(unicode(post.text()))
            __M_writer(u'\n    </div>\n    </article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 2, "29": 0, "40": 2, "41": 3, "46": 22, "52": 5, "62": 5, "63": 7, "64": 8, "65": 10, "66": 10, "67": 10, "68": 10, "69": 12, "70": 12, "71": 12, "72": 12, "73": 12, "74": 12, "75": 12, "76": 12, "77": 16, "78": 16, "79": 20, "80": 21, "81": 21, "87": 81}, "uri": "index.tmpl", "filename": "themes/planetoid/templates/index.tmpl"}
__M_END_METADATA
"""
