def last_or_none(st):
    if len(st) == 0:
        return None
    else:
        return st[-1]


def update_available_spot(node, thing):
    if type(node) != tuple:
        return thing

    (left, center, right) = node
    if left is None:
        current = (thing, None, None)
        return True, current
    elif center is None:
        current = (left, thing, None)
        return True, current
    elif right is None:
        current = (left, center, thing)
        return True, current
    else:
        lf, ln = update_available_spot(left, thing)
        if lf:
            return True, ln
        cf, cn = update_available_spot(center, thing)
        if cf:
            return True, cn
        rf, rn = update_available_spot(right, thing)
        if rf:
            return True, rn

        return False, node


def reduce(st):
    if len(st) >= 2:
        last = st[-1]
        one_last = st[-2]

        if not all(map(lambda x: x, last)):
            return st

        st.pop()
        (_, current) = update_available_spot(one_last, last)
        st.pop()

        st.append(current)

        if all(map(lambda x: x, list(st[-1]))):
            st = reduce(st)
        return st
    else:
        return st


def shift(st, thing):
    current = last_or_none(st)
    if current is None:
        st.append(thing)
    else:
        can_reduce = False
        (left, center, right) = current
        if left is None:
            current = (thing, None, None)
        elif center is None:
            current = (left, thing, None)
        elif right is None:
            current = (left, center, thing)
            can_reduce = True

        st.pop()
        st.append(current)

        if can_reduce:
            st = reduce(st)

        return st


def add_buffer_if_any(st, buffer):
    if buffer:
        thing = int(buffer)
        st = shift(st, thing)
        buffer = ''

    return buffer, st


def parentheses_to_tree(str_lit):
    buffer = ''
    st = []
    for c in list(str_lit):
        if c == ' ':
            continue
        elif c == '-':
            buffer += c
            continue
        elif c.isdigit():
            buffer += c
            continue
        elif c == ',':
            buffer, st = add_buffer_if_any(st, buffer)
        elif c == '(':
            st.append((None, None, None))
        elif c == ')':
            buffer, st = add_buffer_if_any(st, buffer)

    return last_or_none(st)


tree = '(((-3, -2, -1), 2, 3), 4, (5, 6, 7))'
print(parentheses_to_tree(tree))
