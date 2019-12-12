import svgwrite

content = {
    #'Symbols': [
    #    'Rename',
    #    'Extract / Inline',
    #    'Remove unused / Add',
    #    'Move',
    #    'Hide',
    #    'Re-use / duplicate',
    #],
    'Variables': [
        'Move variable',
        'Rename variable',
        'Extract variable / Inline variable',
        'Remove unused variable / Add unused variable',
        'Public variable / Private variable',
        'Check null pointer',
        'Check array bounds',
    ],
    'Functions': [
        'Move function',
        'Rename function',
        'Extract function / Inline function',
        'Remove unused function / Add unused function',
        'Public function / Private function',
        'Move code outside of function / Move code inside of function',
        'Separate query and modifier',
        'Explicit loop / Recursion',
        'Nested conditionals / Guard clauses',
        'Encapsulate mutable variable',
        'Remove mutable control flag',
        'Errors as return values / Exceptions',
        'Check pre-condition',
        'Check post-condition',
        #'Replace parameter with function / Parameterize function',
    ],
    'Types': [
        'Move type',
        'Rename type',
        'Extract type / Inline type',
        'Remove unused type / Add unused type',
        'Public type / Private type',
        'Mutable / Immutable',
        'Direct member reading / Getter function',
        'Direct member writing / Setter function',
        'Scope based resource management / Manual resource management',
        'Add constructor / Remove constructor',
        'Add destructor / Remove destructor',
        'Constructor / Factory function',
        'Categorical constants / Enums',
        'Reduce state space',
        #'Hide delegate /remove delegate',
    ],
    'Polymorphism': [
        'Move interface',
        'Rename interface',
        'Extract interface / Inline interface',
        'Remove unused interface / Add unused interface',
        'Public interface / Private interface',
        'Custom type / Generic collection',
        'Custom loop / Generic algorithm',
        'Inheritance / Composition',
        'Switch cases or conditionals / Polymorphism',
        'Conditionals for special case / Add null object',
        #'Replace subclass with fields',
        #'Add unused factory function',
    ],
    'Files': [
        'Move file',
        'Rename file',
        'Extract file / Inline file',
        'Remove unused file / Add unused file',
        'Visible file / Hidden file',
    ],
    'Directories': [
        'Move directory',
        'Rename directory',
        'Extract directory / Inline directory',
        'Remove unused directory / Add unused directory',
        'Visible directory / Hidden directory',
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


FONT_CAPTION = {
    'font_size': '2.0em',
    'font-family': 'Lato',# 'Noto Sans',#'Noto Sans', #'Merriweather', #'Playfair Display',#'Merriweather', 'Oxygen Mono'
    'fill': 'black',
    #'font_weight': 'bold',
    'letter-spacing': '5px'
}

FONT = {
    'font_size': '1.0em',
    'font-family': 'Oxygen Mono',#'Raleway'#'Oxygen Mono'
    'fill': 'black',
}

FONTS = [FONT, FONT_CAPTION]

COLOR_FROM_CATEGORY = {
    'Variables': '#42bdc5',
    'Functions': '#fccc8b',
    'Types': '#7cc161',
    'Polymorphism': '#ef7f8e',
    'Files': '#6674b6',
    'Directories': '#1f2547',
}

DX = 350
DY = 80
DY_LINE = 45
X_START = 30
Y_START = 100
TEXT_OFFSET_X = 20
TEXT_OFFSET_Y = -DY + 22
CIRCLE_OFFSET_X = DX - 20
CIRCLE_OFFSET_Y = -DY / 2 #-DY + 20
DIVIDER = 0
ARROW_OFFSET_X = +DX * 0.2
ARROW_OFFSET_Y = -DY * 0.5

CAPTION_OFFSET_X = 20
CAPTION_OFFSET_Y = -DY + 45

RADIUS = 7

x = X_START
last_height = 0
current_height = 0
drawing = svgwrite.Drawing('refactorings.svg')

for font in FONTS:
    name = font['font-family']
    drawing.embed_google_web_font(name=name, uri="https://fonts.googleapis.com/css?family={}".format(name.replace(' ', '+')))

for category_name, refactorings in content.items():
    y = Y_START
    current_height = DY * len(refactorings)
    _draw_line_vertical(drawing, x=x, y=Y_START, h=max(current_height, last_height))
    last_height = current_height
    _draw_text(drawing, category_name.upper(), x + CAPTION_OFFSET_X, y + CAPTION_OFFSET_Y, **FONT_CAPTION)
    _draw_line_horizontal(drawing, x=x, y=y, w=DX)
    y += DY
    for refactoring in refactorings:
        _draw_line_horizontal(drawing, x=x, y=y, w=DX)
        _draw_line_horizontal(drawing, x=x, y=y - DY / 2, w=DIVIDER)
        _draw_line_horizontal(drawing, x=x + DX - DIVIDER, y=y - DY / 2, w=DIVIDER)

        lines = refactoring.split('/')
        if len(lines) < 2:
            _draw_text(drawing, lines[0], x=x + TEXT_OFFSET_X, y=y + TEXT_OFFSET_Y + DY_LINE / 2, **FONT)
        else:
            _draw_text(drawing, lines[0], x=x + TEXT_OFFSET_X, y=y + TEXT_OFFSET_Y, **FONT)
            _draw_text(drawing, lines[1], x=x + TEXT_OFFSET_X, y=y + TEXT_OFFSET_Y + DY_LINE, **FONT)
            _draw_arrows(drawing, x=x + ARROW_OFFSET_X, y=y + ARROW_OFFSET_Y, h=14, a=4)

        _draw_circle(drawing, x=x + CIRCLE_OFFSET_X, y=y + CIRCLE_OFFSET_Y, r=RADIUS, c=COLOR_FROM_CATEGORY[category_name])
        y += DY
    x += DX
_draw_line_vertical(drawing, x=x, y=Y_START, h=max(current_height, last_height))

drawing.save()
