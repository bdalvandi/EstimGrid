import wx
from win_main import MainWindow
from win_settings import SettingsDlg


def main():
    app = wx.App()
    win = MainWindow(None)
    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
