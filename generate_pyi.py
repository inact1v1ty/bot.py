import re

with open('bot/types.py', 'r') as f:
    source = f.read()

classes = {}

reg = re.compile(
    r'^@attr\.s\(auto_attribs=True\)$\n' +
    r'^class\s(\w+)\(\w+\):$\n((?:^\s{4}\w+:\s?[^\n]*$\n)*)',
    re.M
)

attrib = re.compile(r'\s?=\s?attr\.ib\(.+\)$', re.M)
attrib2 = re.compile(r'\s?=\s?attr\.ib\(\n.+\n\s*\)', re.M)


def repl(m):
    s = m.group(0)
    if 'default' in s:
        return ' = None'
    else:
        return ''


source = attrib.sub(repl, source)
source = attrib2.sub(repl, source)

for m in reg.finditer(source):
    name = m.group(1)
    lines = m.group(2)
    lines = lines.split('\n')
    classes[name] = list(
        filter(
            lambda line: line != '',
            map(
                lambda line: line.lstrip(), lines
            )
        )
    )

i = '    '

with open('bot/types.pyi', 'w') as f:
    f.write('import typing\n')
    f.write('from typing import Optional as o\n\n\n')

    for idx, (name, lines) in enumerate(classes.items()):

        f.write('class {}:\n'.format(name))
        f.write(i + 'def __init__(\n')

        f.write(',\n'.join(map(lambda line: i * 2 + line, lines)) + '\n')

        f.write(i + ') -> None: ...\n\n')
        if idx != len(classes) - 1:
            f.write('\n')
