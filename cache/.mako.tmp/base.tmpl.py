# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499745756.527
_enable_loop = True
_template_filename = u'themes/hack/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'header', context._clean_inheritance_tokens(), templateuri=u'base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'header')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    ns = runtime.TemplateNamespace(u'annotations', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'annotations')] = ns

    ns = runtime.TemplateNamespace(u'footer', context._clean_inheritance_tokens(), templateuri=u'base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        HACK_VARIANT = _import_ns.get('HACK_VARIANT', context.get('HACK_VARIANT', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        header = _mako_get_namespace(context, 'header')
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n')
        if not HACK_VARIANT:
            __M_writer(u'    <body class="hack">\n')
        elif HACK_VARIANT == 'dark':
            __M_writer(u'    <body class="hack dark">\n')
        elif HACK_VARIANT == 'dark-grey':
            __M_writer(u'    <body class="hack dark-grey">\n')
        elif HACK_VARIANT == 'solarized-dark':
            __M_writer(u'    <body class="hack solarized-dark">\n')
        elif HACK_VARIANT == 'standard':
            __M_writer(u'    <body class="hack standard">\n')
        __M_writer(u'\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(unicode(messages("Skip to main content")))
        __M_writer(u'</a>\n    <div id="container">\n         ')
        __M_writer(unicode(header.html_header()))
        __M_writer(u'\n         <main id="content">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n         </main>\n         ')
        __M_writer(unicode(footer.html_footer()))
        __M_writer(u'\n    </div>\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'header')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'footer')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"137": 8, "143": 34, "23": 3, "26": 2, "29": 5, "158": 143, "32": 4, "35": 0, "59": 2, "60": 3, "61": 4, "62": 5, "63": 6, "64": 6, "65": 7, "66": 7, "71": 10, "72": 11, "73": 11, "74": 13, "75": 14, "76": 15, "77": 16, "78": 17, "79": 18, "80": 19, "81": 20, "82": 21, "83": 22, "84": 24, "85": 25, "86": 25, "87": 27, "88": 27, "93": 29, "94": 31, "95": 31, "96": 33, "97": 33, "102": 34, "103": 35, "104": 35, "105": 36, "106": 36, "112": 29, "127": 8}, "uri": "base.tmpl", "filename": "themes/hack/templates/base.tmpl"}
__M_END_METADATA
"""
