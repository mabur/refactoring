import svgwrite

content = {
    #'Symbols': [
    #    'Rename',
    #    'Extract / Inline',
    #    'Remove / Add',
    #    'Move',
    #    'Hide',
    #    'Re-use / duplicate',
    #],
    'Variables': [
        'Rename variable',
        'Extract variable / Inline variable',
        'Remove variable / Add variable',
        'Move variable',
        'Hide variable',
        'Re-use variable / Duplicate variable',
    ],
    'Functions': [
        'Rename function',
        'Extract function / Inline function',
        'Remove function / Add function',
        'Move function',
        'Hide function',
        'Re-use function / Duplicate function',
        'Encapsulate mutable variable',
        'Separate query and modifier',
        'Replace parameter with function / Parameterize function',
        'Encapsulate mutable variable',
        'Remove mutable control flag',
        'Nested conditionals / Guard clauses',
        'Move fragment to caller/called',
        'Replace loop with recursion',
    ],
    'Types': [
        'Rename type',
        'Extract type / Inline type',
        'Remove type / Add type',
        'Move type',
        'Hide type',
        'Re-use type / Duplicate type',
        'Make type immutable / Make type mutable',
        'Get data via function',
        'Set data via function',
        'Hide/remove delegate',
        'Add/remove constructor',
        'Add/remove destructor',
        'Reduce state space',
        'Constructor / Factory function',
        'Replace integer/string with enum',
    ],
    'Polymorphism': [
        'Rename interface',
        'Extract interface / Inline interface',
        'Remove interface / Add interface',
        'Move interface',
        'Hide interface',
        'Re-use interface / Duplicate interface',
        'Inheritance / Composition',
        'Add factory function',
        'Conditionals and type codes / Polymorphism',
        'Replace subclass with fields',
        'Add null object / special case',
        'Custom type / Generic collection',
        'Custom loop / Generic algorithm',
    ],
    'Files': [
        'Rename file',
        'Extract file / Inline file',
        'Remove / Add file',
        'Move file',
        'Hide file',
        'Re-use file / Duplicate file',
    ],
    'Directories': [
        'Rename directory',
        'Extract directory / Inline directory',
        'Remove / Add directory',
        'Move directory',
        'Hide directory',
        'Re-use directory / Duplicate directory',
    ]
}

other = {
    'Control Flow': [
        'Decompose conditional',
        'Consolidate conditional expression',
        'Consolidate duplicated conditional fragment',
        'Change loop/conditional construct',
        'Scope based resource management',
        'Error code, Optional, Exception',
        ],
    'Tests': [
        'Add compile time error detection',
        'Add compile time warning',
        'Add static analyzer',
        'Add linter',
        'Add stronger type check',
        'Make object immutable',
        'Add assertion',
        'Assert pre condition',
        'Assert post condition',
        'Add bounds check',
        'Add null pointer check',
        'Add unit test',
        'Add property test',
        'Add integration test',
    ]
}


def _draw_text(drawing, text: str, x: int, y: int, **kwargs) -> None:
    t = drawing.text(text='')
    t.add(drawing.tspan(text, x=[x], y=[y], **kwargs))
    drawing.add(t)


def _draw_line(drawing, x0, y0, x1, y1):
    drawing.add(drawing.line((x0, y0), (x1, y1), stroke=svgwrite.rgb(0, 0, 0, '%')))


def _draw_line_vertical(drawing, x, y, h):
    drawing.add(drawing.line((x, y), (x, y + h), stroke=svgwrite.rgb(0, 0, 0, '%')))


def _draw_line_horizontal(drawing, x, y, w):
    drawing.add(drawing.line((x, y), (x + w, y), stroke=svgwrite.rgb(0, 0, 0, '%')))


def _draw_circle(drawing, x, y, r, c):
    drawing.add(drawing.circle(center=(x, y), r=r, fill=c))

def _draw_arrows(drawing, x, y, h, a):
    _draw_line_vertical(drawing, x, y - h / 2, h)
    _draw_line(drawing, x0=x, y0=y - h / 2, x1=x + a, y1=y - h / 2 + a)
    _draw_line(drawing, x0=x, y0=y - h / 2, x1=x - a, y1=y - h / 2 + a)
    _draw_line(drawing, x0=x, y0=y + h / 2, x1=x + a, y1=y + h / 2 - a)
    _draw_line(drawing, x0=x, y0=y + h / 2, x1=x - a, y1=y + h / 2 - a)


FONT_NAME = 'Oxygen Mono'#'Raleway'#'Oxygen Mono'

FONT = {
    'font_size': '0.8em',
    'font-family': FONT_NAME,
    'fill': 'black',
}

COLOR_FROM_CATEGORY = {
    'Variables': '#42bdc5',
    'Functions': '#fccc8b',
    'Types': '#99d5e2',
    'Polymorphism': '#ef7f8e',
    'Files': '#6674b6',
    'Directories': '#1f2547',
}

DX = 300
DY = 80
DY_LINE = 40
X_START = 30
Y_START = 100
TEXT_OFFSET_X = 20
TEXT_OFFSET_Y = -DY + 20
CIRCLE_OFFSET_X = DX - 20
CIRCLE_OFFSET_Y = -DY + 20
DIVIDER = 0

x = X_START
last_height = 0
current_height = 0
drawing = svgwrite.Drawing('refactorings.svg')

drawing.embed_google_web_font(name=FONT_NAME, uri="https://fonts.googleapis.com/css?family={}".format(FONT_NAME.replace(' ', '+')))

for category_name, refactorings in content.items():
    y = Y_START
    current_height = DY * len(refactorings)
    _draw_line_vertical(drawing, x=x, y=Y_START, h=max(current_height, last_height))
    last_height = current_height
    _draw_text(drawing, category_name.upper(), x + TEXT_OFFSET_X, y + TEXT_OFFSET_Y, **FONT, font_weight='bold')
    _draw_line_horizontal(drawing, x=x, y=y, w=DX)
    y += DY
    for refactoring in refactorings:
        _draw_line_horizontal(drawing, x=x, y=y, w=DX)
        _draw_line_horizontal(drawing, x=x, y=y - DY / 2, w=DIVIDER)
        _draw_line_horizontal(drawing, x=x + DX - DIVIDER, y=y - DY / 2, w=DIVIDER)

        lines = refactoring.split('/')
        _draw_text(drawing, lines[0], x=x + TEXT_OFFSET_X, y=y + TEXT_OFFSET_Y, **FONT)
        if len(lines) > 1:
            _draw_text(drawing, lines[1], x=x + TEXT_OFFSET_X, y=y + TEXT_OFFSET_Y + DY_LINE, **FONT)
            _draw_arrows(drawing, x=x + DX / 2, y=y - DY / 2, h=14, a=4)

        _draw_circle(drawing, x=x + CIRCLE_OFFSET_X, y=y + CIRCLE_OFFSET_Y, r=5, c=COLOR_FROM_CATEGORY[category_name])
        y += DY
    x += DX
_draw_line_vertical(drawing, x=x, y=Y_START, h=max(current_height, last_height))

drawing.save()
