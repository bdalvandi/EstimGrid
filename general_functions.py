import wx
from configobj import ConfigObj


# set layout of a control an all its children
def set_layout(control, layout=wx.Layout_LeftToRight):
    control.SetLayoutDirection(layout)
    if len(control.GetChildren()) == 0:
        return
    for child in control.GetChildren():
        set_layout(child, layout)


# convert any value to string
def convert_string(var):
    if var in ['True', 'False']:
        return bool(var)
    if var == 'None':
        return None
    funcs = [int, float, str]
    for func in funcs:
        try:
            return func(var)
        except ValueError:
            pass


class Wait:
    def __init__(self, message=None):
        self.message = message

    def __enter__(self):
        self.wait = wx.BusyCursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.wait
        if self.message is not None:
            wx.MessageBox(self.message)


# get a property value from settings.conf file
# base for other functions
def __get_value_from_settings(prop_label):
    config = ConfigObj('misc/settings.ini')
    return config[prop_label]


# get connection string from settings.conf file
def connection_string():
    return __get_value_from_settings('Connection String')


# get default snapshot folder path
def snap_dir():
    return __get_value_from_settings('Default Snapshot Path')


# open a snapshot file and returen its data
def read_snap(filename):
    with open(filename) as f:
        lines = f.readlines()
    objects = {}
    for line in lines:
        # try:
        obj, val, stat = tuple(line.split())
        # except:
        #     continue
        objects[obj] = (float(val), int(stat))
    return objects


def ttr(args):
    try:
        Mt, mt, Mv, mv, t = args
        return mv + ((Mv - mv) / (Mt - mt)) * (t - mt)
    except (TypeError, ValueError):
        return
