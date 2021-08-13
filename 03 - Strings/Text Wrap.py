def wrap(string, max_width):
    wrap_string = '\n'.join(textwrap.wrap(string, max_width))
    return wrap_string