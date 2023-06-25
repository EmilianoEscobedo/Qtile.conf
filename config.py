




# ooooo                   o8o                                                  .o8              
# `888'                   `"'                                                 "888              
#  888          .oooo.   oooo  ooo. .oo.    .oooooooo  .oooo.   oooo d8b  .oooo888              
#  888         `P  )88b  `888  `888P"Y88b  888' `88b  `P  )88b  `888""8P d88' `888              
#  888          .oP"888   888   888   888  888   888   .oP"888   888     888   888              
#  888       o d8(  888   888   888   888  `88bod8P'  d8(  888   888     888   888              
# o888ooooood8 `Y888""8o o888o o888o o888o `8oooooo.  `Y888""8o d888b    `Y8bod88P"             
#                                          d"     YD                                            
#                                          "Y88888P'                                            
                                                                                                                                  
                                                          
                                                                                              
#   .oooooo.          .    o8o  oooo                   .oooooo.                          .o88o. 
#  d8P'  `Y8b       .o8    `"'  `888                  d8P'  `Y8b                         888 `" 
# 888      888    .o888oo oooo   888   .ooooo.       888           .ooooo.  ooo. .oo.   o888oo  
# 888      888      888   `888   888  d88' `88b      888          d88' `88b `888P"Y88b   888    
# 888      888      888    888   888  888ooo888      888          888   888  888   888   888    
# `88b    d88b      888 .  888   888  888    .o      `88b    ooo  888   888  888   888   888    
#  `Y8bood8P'Ybd'   "888" o888o o888o `Y8bod8P'       `Y8bood8P'  `Y8bod8P' o888o o888o o888o   
                                                                                                                                                     
                                                                                                                                        
import os
import subprocess
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

taskbarColor ="#282a36"
taskbarSize = 30
defaultFont = "Hack"

# Custom functions
def separator():
    return widget.Sep(
        linewidth = 0,
        padding = 6,
    )

keys = [

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),


    # Custom Shortcurs

    Key([mod], 'm', lazy.spawn("rofi -show drun"), desc="Show menu"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], 'f', lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], 'd', lazy.spawn("discord"), desc="Launch discord"),
    Key([mod], 'p', lazy.spawn("flameshot gui"), desc="Launch flameshot"),
    Key([mod], 's', lazy.spawn("pavucontrol -t 3"), desc="Launch sound control"),
    Key([mod], 'c', lazy.spawn("calc.sh"), desc="Launch calculator"),
    Key([mod], 't', lazy.spawn("trello"), desc="Launch trello"),
    Key([mod], 'i', lazy.spawn("/home/laingard/intelliJ/idea-IC-223.7571.182/bin/idea.sh", shell=True), desc="Launch IntelliJ"),
    Key([mod, "shift"], 'Return', lazy.spawn("/home/laingard/shellScripts/changeLayout.sh", shell=True), desc="Change layout"),
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.window.toggle_floating()),
]

groups = [Group(i) for i in [
    'WEB','WRK','DOC','ETC','LGD'
    ]]

for i, group in enumerate(groups):
    nDesktop = str(i+1)
    keys.extend(
        [
            Key(
                [mod],
                nDesktop,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                nDesktop,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus="#13dde8", border_width=3, margin=4),
    layout.Max(border_focus="#13dde8", border_width=3, margin=4),
    # layout.Stack(num_stacks=2),
    layout.Bsp(border_focus="#13dde8", border_width=3, margin=4),
    layout.Matrix(border_focus="#13dde8", border_width=3, margin=4)
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font= defaultFont,
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag = True,
                    borderwidth = 2,
                    highlight_method='line',
                    inactive = "#5c5b5b",
                    this_current_screen_border = "#bd93f9",
                     padding=5
                    ),
                separator(),
                widget.Image(margin=5, filename='/home/laingard/Images/archlogo.png'),
                widget.WindowTabs(
                    padding=20,
                    foreground = "#bd93f9",
                    max_chars = 30,
                    ),
                widget.Systray(
                    padding = 10
                    ),
                separator(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.TextBox(
                    "|",
                    padding = 10),
                widget.CurrentLayout(),
            ],
            taskbarSize,
            background = taskbarColor,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen()
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup_complete
def poststart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/home/laingard/shellScripts/sensorScreen.sh'])
