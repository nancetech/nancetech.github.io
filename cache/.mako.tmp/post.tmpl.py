# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499745899.801
_enable_loop = True
_template_filename = u'themes/planetoid/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n<meta http-equiv="Refresh" content="0;url=')
        __M_writer(unicode(post.meta('link')))
        __M_writer(u'">\n</head>\n<body>\nRedirecting you to <a href="')
        __M_writer(unicode(post.meta('link')))
        __M_writer(u'">the original location.</a>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "16": 0, "22": 2, "23": 4, "24": 4, "25": 7, "26": 7}, "uri": "post.tmpl", "filename": "themes/planetoid/templates/post.tmpl"}
__M_END_METADATA
"""
