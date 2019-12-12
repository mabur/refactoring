import svgwrite

MOVE = '-->'
RENAME = 'Abc'
EXTRACT_INLINE = '...'
REMOVE_ADD = '+ -'
VISIBILITY = '( )'
STATE_SPACE = '\u00A0!'
CONTROL = 'JMP'

SPECIAL_STRINGS = [MOVE, RENAME, EXTRACT_INLINE, REMOVE_ADD, VISIBILITY, STATE_SPACE, CONTROL]

def strip_special_strings(s: str) -> str:
    for special_string in SPECIAL_STRINGS:
        s = s.replace(special_string, '')
    return s

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
        'Move variable' + MOVE,
        'Rename variable' + RENAME,
        'Extract variable / Inline variable' + EXTRACT_INLINE,
        'Remove unused variable / Add unused variable' + REMOVE_ADD,
        'Public variable / Private variable' + VISIBILITY,
        'Check null pointer' + STATE_SPACE,
        'Check array bounds' + STATE_SPACE,
        'Check invariance' + STATE_SPACE,
    ],
    'Functions': [
        'Move function' + MOVE,
        'Rename function' + RENAME,
        'Extract function / Inline function' + EXTRACT_INLINE,
        'Remove unused function / Add unused function' + REMOVE_ADD,
        'Public function / Private function' + VISIBILITY,
        'Move code outside of function / Move code inside of function',
        'Separate query and modifier',
        'Explicit loop / Recursion' + CONTROL,
        'Nested conditionals / Guard clauses' + CONTROL,
        'Errors as return values / Exceptions' + CONTROL,
        'Remove mutable control flag' + CONTROL,
        'Encapsulate mutable variable' + STATE_SPACE,
        'Check pre-condition' + STATE_SPACE,
        'Check post-condition' + STATE_SPACE,
        #'Replace parameter with function / Parameterize function',
    ],
    'Types': [
        'Move type' + MOVE,
        'Rename type' + RENAME,
        'Extract type / Inline type' + EXTRACT_INLINE,
        'Remove unused type / Add unused type' + REMOVE_ADD,
        'Public type / Private type' + VISIBILITY,
        'Direct member reading / Getter function',
        'Direct member writing / Setter function',
        'Scope based resource management / Manual resource management' + CONTROL,
        'Add constructor / Remove constructor',
        'Add destructor / Remove destructor',
        'Constructor / Factory function',
        'Mutable / Immutable' + STATE_SPACE,
        'Categorical constants / Enums' + STATE_SPACE,
        'Reduce state space' + STATE_SPACE,
        #'Hide delegate /remove delegate',
    ],
    'Polymorphism': [
        'Move interface' + MOVE,
        'Rename interface' + RENAME,
        'Extract interface / Inline interface' + EXTRACT_INLINE,
        'Remove unused interface / Add unused interface' + REMOVE_ADD,
        'Public interface / Private interface' + VISIBILITY,
        'Inheritance / Composition',
        'Custom type / Generic collection',
        'Custom loop / Generic algorithm' + CONTROL,
        'Switch cases or conditionals / Polymorphism' + CONTROL,
        'Conditionals for special case / Polymorphic null object' + CONTROL,
        #'Replace subclass with fields',
        #'Add unused factory function',
    ],
    'Files': [
        'Move file' + MOVE,
        'Rename file' + RENAME,
        'Extract file / Inline file' + EXTRACT_INLINE,
        'Remove unused file / Add unused file' + REMOVE_ADD,
        'Visible file / Hidden file' + VISIBILITY,
    ],
    'Directories': [
        'Move directory' + MOVE,
        'Rename directory' + RENAME,
        'Extract directory / Inline directory' + EXTRACT_INLINE,
        'Remove unused directory / Add unused directory' + REMOVE_ADD,
        'Visible directory / Hidden directory' + VISIBILITY,
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
    'font_size': '2.2em',
    'font-family': 'Lato',# 'Noto Sans',#'Noto Sans', #'Merriweather', #'Playfair Display',#'Merriweather', 'Oxygen Mono'
    'fill': 'black',
    #'font_weight': 'bold',
    'text-anchor': 'middle',
    'letter-spacing': '5px',
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
CIRCLE_OFFSET_Y = -DY + 20 #-DY + 20
DIVIDER = 0
ARROW_OFFSET_X = +DX * 0.2
ARROW_OFFSET_Y = -DY * 0.5

CAPTION_OFFSET_X = DX / 2 #20
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

        lines = [line for line in strip_special_strings(refactoring).split('/')]

        for special_string in SPECIAL_STRINGS:
            if special_string in refactoring:
                _draw_text(drawing, special_string, x=x + CIRCLE_OFFSET_X - 16, y=y + TEXT_OFFSET_Y + DY_LINE, **FONT)

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
