from arraystack import ArrayStack
def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    s = ArrayStack()
    j = raw.find('<')               # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)    # find next '>' character
        if k == -1:
            return False            # invalid tag
        tag = raw[j+1:k]            # strip away <>
        if not tag.startswith('/'): # this is opening tag
            s.push(tag)
        else:                       # this is closing tag
            if s.is_empty():
                return False        # nothing to match with
            if tag [1:] != s.pop():
                return False        # mismatched delimiter
        j = raw.find('<', k + 1)    # find next '<' character (if any)
    return s.is_empty()             # were all opening tags matched?

# sample usage
matched = is_matched_html('<p>')
#print(matched)

matched = is_matched_html('<body><h1></h1></body>')
print(matched)
