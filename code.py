import time
from collections import namedtuple
import board
import displayio
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
from adafruit_button import Button
from adafruit_pyportal import PyPortal
import adafruit_touchscreen

Coords = namedtuple("Point", "x y")

pyportal = PyPortal()
# ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
#                                      board.TOUCH_YD, board.TOUCH_YU,
#                                      calibration=(
#                                          (5200, 59000), (5800, 57000)),
#                                      size=(480, 320))

ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      calibration=(
                                          (6691, 60304), (9232, 56895)),
                                      size=(480, 320))


# Settings
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 30
BUTTON_MARGIN = 8
MAX_DIGITS = 29
BLACK = 0x0
ORANGE = 0xFF8800
WHITE = 0xFFFFFF
GRAY = 0x888888
STEELBLUE = 0x4682b4
BLUE = 0x0000FF
RED = 0xFF0000
MAROON = 0x800000
OLIVE = 0x808000
LIME = 0x00FF00
TEAL = 0x008080
SEAGREEN = 0x2E8B57
GREEN = 0x006600
YELLOW = 0xFFFF00
LABEL_OFFSET = 290

one_color_fill = RED
one_color_label = WHITE
two_color_fill = GREEN
two_color_label = WHITE
three_color_fill = BLACK
three_color_label = WHITE
four_color_fill = YELLOW
four_color_label = BLACK
score_color_fill_active = BLACK
score_color_fill_not_active = TEAL
score_color_label = YELLOW
reset_color_fill = RED
reset_color_label = WHITE

one = 'one'
two = 'two'
three = 'three'
four = 'four'
players = [one, two, three, four]

five = 'five'
ten = 'ten'
fifteen = 'fifteen'
twenty = 'twenty'
regions = [five, ten, fifteen, twenty]

labels = {five: 5, ten: 10, fifteen: 15, twenty: 20}

active_players = {one: True, two: True, three: False, four: False}


def get_count_container():
    return {'one': {'five': 0, 'ten': 0, 'fifteen': 0, 'twenty': 0},
            'two': {'five': 0, 'ten': 0, 'fifteen': 0, 'twenty': 0},
            'three': {'five': 0, 'ten': 0, 'fifteen': 0, 'twenty': 0},
            'four': {'five': 0, 'ten': 0, 'fifteen': 0, 'twenty': 0}}


def count_for(player, region):
    counts[player][region] = counts[player][region] + 1
    if counts[player][region] >= 6:
        counts[player][region] = 0
    label_text = f'{labels[region]} ({counts[player][region]})'
    buttons[player][region].label = label_text
    calculate_scores()


def calculate_count(player):
    player_counts = counts[player]
    count = 0
    for region in regions:
        count = count + (player_counts[region] * labels[region])

    return count


def calculate_scores():
    score_sheet = ['X', 'X', 'X', 'X']
    count = active_player_count()

    if count == 2:
        score_sheet = get_two_player_score(
            get_count_for_active_pos(1), get_count_for_active_pos(2))
    elif count == 3:
        score_sheet = get_three_player_score(get_count_for_active_pos(
            1), get_count_for_active_pos(2), get_count_for_active_pos(3))
    elif count == 4:
        score_sheet = get_four_player_score(get_count_for_active_pos(1), get_count_for_active_pos(
            2), get_count_for_active_pos(3), get_count_for_active_pos(4))

    print(f'score: {score_sheet}')
    update_scores(score_sheet)


def get_active_player_in_pos(count):
    current_count = 1
    location = 0
    # we pull them in this way so the list is ordered
    for player in players:
        if is_active(player):
            if current_count == count:
                return location
            else:
                current_count = current_count + 1
        location = location + 1
    raise Exception("Critial error in active player pos")


def update_scores(score_sheet):
    one_score_button.label = str(score_sheet[0])
    two_score_button.label = str(score_sheet[1])
    three_score_button.label = str(score_sheet[2])
    four_score_button.label = str(score_sheet[3])


def get_two_player_score(count_1, count_2):
    #    print('getting 2 player score')
    score_sheet = ['X', 'X', 'X', 'X']
    if count_1 > count_2:
        score_1 = count_1 - count_2
        score_2 = 0
    else:
        score_2 = count_2 - count_1
        score_1 = 0

    score_sheet[get_active_player_in_pos(1)] = score_1
    score_sheet[get_active_player_in_pos(2)] = score_2

    return score_sheet


def get_three_player_score(count_1, count_2, count_3):
    #    print('getting 3 player score')
    score_sheet = ['X', 'X', 'X', 'X']

    if count_1 < count_2 and count_1 < count_3:
        smallest = count_1
    elif count_2 < count_3:
        smallest = count_2
    else:
        smallest = count_3

    score_1 = count_1 - smallest
    score_2 = count_2 - smallest
    score_3 = count_3 - smallest

    score_sheet[get_active_player_in_pos(1)] = score_1
    score_sheet[get_active_player_in_pos(2)] = score_2
    score_sheet[get_active_player_in_pos(3)] = score_3

    return score_sheet


def get_four_player_score(count_1, count_2, count_3, count_4):
    #    print('getting 4 player score')
    score_sheet = ['X', 'X', 'X', 'X']

    if count_1 < count_2 and count_1 < count_3 and count_1 < count_4:
        smallest = count_1
    elif count_2 < count_3 and count_2 < count_4:
        smallest = count_2
    elif count_3 < count_4:
        smallest = count_3
    else:
        smallest = count_4

    score_1 = count_1 - smallest
    score_2 = count_2 - smallest
    score_3 = count_3 - smallest
    score_4 = count_4 - smallest

    score_sheet[get_active_player_in_pos(1)] = score_1
    score_sheet[get_active_player_in_pos(2)] = score_2
    score_sheet[get_active_player_in_pos(3)] = score_3
    score_sheet[get_active_player_in_pos(4)] = score_4

    return score_sheet


def active_player_count():
    global active_players
    active_count = 0

    for player in players:
        if active_players[player]:
            active_count = active_count + 1

    return active_count


def get_count_for_active_pos(pos):
    active_count = 0
    for player in players:
        if is_active(player):
            if (active_count + 1) == pos:
                return calculate_count(player)
            else:
                active_count = active_count + 1
    raise Exception("Critial error in count module")


def is_active(player):
    return active_players[player]


def toggle_active(player):
    global active_players, score_buttons

    active_players[player] = not active_players[player]

    if active_players[player]:
        score_buttons[player].fill_color = score_color_fill_active
    else:
        score_buttons[player].fill_color = score_color_fill_not_active
        score_buttons[player].label = 'X'

    calculate_scores()


def reset_counts():
    #    print('reseting counts')
    for player in players:
        for region in regions:
            counts[player][region] = 0
    reset_count_display()
    calculate_scores()


def reset_count_display():
    for player in players:
        for region in regions:
            label = labels[region]
            buttons[player][region].label = str(label)


# Make the display context
poker_group = displayio.Group()
popup = displayio.Group()
board.DISPLAY.show(poker_group)
# board.DISPLAY.rotation = 180

# Make a background color fill
color_bitmap = displayio.Bitmap(480, 320, 1)
color_palette = displayio.Palette(1)
# color_palette[0] = GRAY
color_palette[0] = SEAGREEN
bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
poker_group.append(bg_sprite)

# Load the font
font = bitmap_font.load_font("/fonts/Arial-Bold-18.bdf")
# timer_font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")
# blind_font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")
button_font = bitmap_font.load_font("/fonts/Arial-Bold-18.bdf")
# adjuster_font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")
reset_font = bitmap_font.load_font("/fonts/Arial-Bold-12.bdf")
# message_font = bitmap_font.load_font("/fonts/Arial-Bold-24.bdf")

message_border = Rect(20, 30, 280, 60, fill=ORANGE, outline=BLACK, stroke=2)
message_info = Label(font, text="", color=WHITE)
message_info.x = 30
message_info.y = 60
popup.append(message_border)
popup.append(message_info)

poker_title_border = Rect(20, 8, 375, 35, fill=BLACK, outline=BLACK, stroke=2)
poker_title = Label(font, text="       Crokinole Scorer", color=ORANGE)
poker_title.x = 55
poker_title.y = 25

poker_group.append(poker_title_border)
poker_group.append(poker_title)

# RESET BUTTON
reset_button = Button(x=400, y=8, width=60, height=35, label="Reset",
                      label_font=reset_font, label_color=reset_color_label, fill_color=reset_color_fill, style=Button.ROUNDRECT)
poker_group.append(reset_button)


# PLAYER ONE
one_five_button = Button(x=20, y=55, width=90, height=60, label="5",
                         label_font=button_font, label_color=one_color_label, fill_color=one_color_fill, style=Button.ROUNDRECT)
poker_group.append(one_five_button)
one_ten_button = Button(x=115, y=55, width=90, height=60, label="10",
                        label_font=button_font, label_color=one_color_label, fill_color=one_color_fill, style=Button.ROUNDRECT)
poker_group.append(one_ten_button)
one_fifteen_button = Button(x=210, y=55, width=90, height=60, label="15",
                            label_font=button_font, label_color=one_color_label, fill_color=one_color_fill, style=Button.ROUNDRECT)
poker_group.append(one_fifteen_button)
one_twenty_button = Button(x=305, y=55, width=90, height=60, label="20",
                           label_font=button_font, label_color=one_color_label, fill_color=one_color_fill, style=Button.ROUNDRECT)
poker_group.append(one_twenty_button)
one_score_button = Button(x=400, y=55, width=60, height=60, label="0",
                          label_font=button_font, label_color=score_color_label, fill_color=score_color_fill_active, style=Button.ROUNDRECT)
poker_group.append(one_score_button)


# PLAYER TWO
two_five_button = Button(x=20, y=120, width=90, height=60, label="5",
                         label_font=button_font, label_color=two_color_label, fill_color=two_color_fill, style=Button.ROUNDRECT)
poker_group.append(two_five_button)
two_ten_button = Button(x=115, y=120, width=90, height=60, label="10",
                        label_font=button_font, label_color=two_color_label, fill_color=two_color_fill, style=Button.ROUNDRECT)
poker_group.append(two_ten_button)
two_fifteen_button = Button(x=210, y=120, width=90, height=60, label="15",
                            label_font=button_font, label_color=two_color_label, fill_color=two_color_fill, style=Button.ROUNDRECT)
poker_group.append(two_fifteen_button)
two_twenty_button = Button(x=305, y=120, width=90, height=60, label="20",
                           label_font=button_font, label_color=two_color_label, fill_color=two_color_fill, style=Button.ROUNDRECT)
poker_group.append(two_twenty_button)
two_score_button = Button(x=400, y=120, width=60, height=60, label="0",
                          label_font=button_font, label_color=score_color_label, fill_color=score_color_fill_active, style=Button.ROUNDRECT)
poker_group.append(two_score_button)


# PLAYER THREE
three_five_button = Button(x=20, y=185, width=90, height=60, label="5",
                           label_font=button_font, label_color=three_color_label, fill_color=three_color_fill, style=Button.ROUNDRECT)
poker_group.append(three_five_button)
three_ten_button = Button(x=115, y=185, width=90, height=60, label="10",
                          label_font=button_font, label_color=three_color_label, fill_color=three_color_fill, style=Button.ROUNDRECT)
poker_group.append(three_ten_button)
three_fifteen_button = Button(x=210, y=185, width=90, height=60, label="15",
                              label_font=button_font, label_color=three_color_label, fill_color=three_color_fill, style=Button.ROUNDRECT)
poker_group.append(three_fifteen_button)
three_twenty_button = Button(x=305, y=185, width=90, height=60, label="20",
                             label_font=button_font, label_color=three_color_label, fill_color=three_color_fill, style=Button.ROUNDRECT)
poker_group.append(three_twenty_button)
three_score_button = Button(x=400, y=185, width=60, height=60, label="X",
                            label_font=button_font, label_color=score_color_label, fill_color=score_color_fill_not_active, style=Button.ROUNDRECT)
poker_group.append(three_score_button)


# PLAYER FOUR
four_five_button = Button(x=20, y=250, width=90, height=60, label="5",
                          label_font=button_font, label_color=four_color_label, fill_color=four_color_fill, style=Button.ROUNDRECT)
poker_group.append(four_five_button)
four_ten_button = Button(x=115, y=250, width=90, height=60, label="10",
                         label_font=button_font, label_color=four_color_label, fill_color=four_color_fill, style=Button.ROUNDRECT)
poker_group.append(four_ten_button)
four_fifteen_button = Button(x=210, y=250, width=90, height=60, label="15",
                             label_font=button_font, label_color=four_color_label, fill_color=four_color_fill, style=Button.ROUNDRECT)
poker_group.append(four_fifteen_button)
four_twenty_button = Button(x=305, y=250, width=90, height=60, label="20",
                            label_font=button_font, label_color=four_color_label, fill_color=four_color_fill, style=Button.ROUNDRECT)
poker_group.append(four_twenty_button)
four_score_button = Button(x=400, y=250, width=60, height=60, label="X",
                           label_font=button_font, label_color=score_color_label, fill_color=score_color_fill_not_active, style=Button.ROUNDRECT)
poker_group.append(four_score_button)


# put the buttons in a collection for easy access
one_buttons = {five: one_five_button, ten: one_ten_button,
               fifteen: one_fifteen_button, twenty: one_twenty_button}
two_buttons = {five: two_five_button, ten: two_ten_button,
               fifteen: two_fifteen_button, twenty: two_twenty_button}
three_buttons = {five: three_five_button, ten: three_ten_button,
                 fifteen: three_fifteen_button, twenty: three_twenty_button}
four_buttons = {five: four_five_button, ten: four_ten_button,
                fifteen: four_fifteen_button, twenty: four_twenty_button}
buttons = {one: one_buttons, two: two_buttons,
           three: three_buttons, four: four_buttons}
score_buttons = {one: one_score_button, two: two_score_button,
                 three: three_score_button, four: four_score_button}


def hideLayer(hide_target):
    try:
        poker_group.remove(hide_target)
    except ValueError:
        pass


def showLayer(show_target):
    try:
        # time.sleep(0.1)
        poker_group.append(show_target)
    except ValueError:
        pass


def showPopup(msg):
    msgTextSize = len(msg)
    if msgTextSize % 2:
        offset = int(msgTextSize / 2)
    else:
        offset = int(msgTextSize / 2) - 1
    xpos = int(210 - (offset * 18))
    message_info.text = msg
    message_info.x = xpos
    showLayer(popup)
    time.sleep(1.5)
    hideLayer(popup)


active = False
counts = get_count_container()

while True:
    point = ts.touch_point
    if point is not None:
        active = True
        print(f"POINT: {point}")
        if reset_button.contains(point):
            print('RESET')
            reset_counts()

        if one_five_button.contains(point):
            count_for(one, five)
        if one_ten_button.contains(point):
            count_for(one, ten)
        if one_fifteen_button.contains(point):
            count_for(one, fifteen)
        if one_twenty_button.contains(point):
            count_for(one, twenty)
        if one_score_button.contains(point):
            toggle_active(one)

        if two_five_button.contains(point):
            count_for(two, five)
        if two_ten_button.contains(point):
            count_for(two, ten)
        if two_fifteen_button.contains(point):
            count_for(two, fifteen)
        if two_twenty_button.contains(point):
            count_for(two, twenty)
        if two_score_button.contains(point):
            toggle_active(two)

        if three_five_button.contains(point):
            count_for(three, five)
        if three_ten_button.contains(point):
            count_for(three, ten)
        if three_fifteen_button.contains(point):
            count_for(three, fifteen)
        if three_twenty_button.contains(point):
            count_for(three, twenty)
        if three_score_button.contains(point):
            toggle_active(three)

        if four_five_button.contains(point):
            count_for(four, five)
        if four_ten_button.contains(point):
            count_for(four, ten)
        if four_fifteen_button.contains(point):
            count_for(four, fifteen)
        if four_twenty_button.contains(point):
            count_for(four, twenty)
        if four_score_button.contains(point):
            toggle_active(four)

    if active:
        time.sleep(.3)
        active = False
