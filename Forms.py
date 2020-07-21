# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg
import wx.adv

###########################################################################
## Class winMain
###########################################################################

class winMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"State Estimator", pos = wx.DefaultPosition, size = wx.Size( 785,439 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.mnuBar = wx.MenuBar( 0 )
		self.mnuFile = wx.Menu()
		self.mnuExport = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"&Export", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuFile.Append( self.mnuExport )

		self.mnuSettings = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"Se&ttings", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuFile.Append( self.mnuSettings )

		self.mnuFile.AppendSeparator()

		self.mnuExit = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"E&xit"+ u"\t" + u"Ctrl+X", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuFile.Append( self.mnuExit )

		self.mnuBar.Append( self.mnuFile, u"&File" )

		self.mnuView = wx.Menu()
		self.mnuBar.Append( self.mnuView, u"&View" )

		self.mnuEstimate = wx.Menu()
		self.mnuLoadSnap = wx.MenuItem( self.mnuEstimate, wx.ID_ANY, u"Load S&napshot", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuEstimate.Append( self.mnuLoadSnap )

		self.mnuExecute = wx.MenuItem( self.mnuEstimate, wx.ID_ANY, u"E&xcecute"+ u"\t" + u"F5", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuEstimate.Append( self.mnuExecute )

		self.mnuEstimate.AppendSeparator()

		self.mnuApplySnapp = wx.MenuItem( self.mnuEstimate, wx.ID_ANY, u"tmp: apply current snap to database", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuEstimate.Append( self.mnuApplySnapp )

		self.mnuBar.Append( self.mnuEstimate, u"E&stimate" )

		self.mnuHelp = wx.Menu()
		self.mnuTutorial = wx.MenuItem( self.mnuHelp, wx.ID_ANY, u"&Tutorial", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuHelp.Append( self.mnuTutorial )

		self.mnuHelp.AppendSeparator()

		self.mnuAbout = wx.MenuItem( self.mnuHelp, wx.ID_ANY, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnuHelp.Append( self.mnuAbout )

		self.mnuBar.Append( self.mnuHelp, u"&Help" )

		self.SetMenuBar( self.mnuBar )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.splMain = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.splMain.SetSashGravity( 0.8 )
		self.splMain.Bind( wx.EVT_IDLE, self.splMainOnIdle )

		self.pnlSplitter = wx.Panel( self.splMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.splGrid = wx.SplitterWindow( self.pnlSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.splGrid.Bind( wx.EVT_IDLE, self.splGridOnIdle )

		self.pnlLeft = wx.Panel( self.splGrid, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.treObjects = wx.TreeCtrl( self.pnlLeft, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer5.Add( self.treObjects, 1, wx.ALL|wx.EXPAND, 5 )


		self.pnlLeft.SetSizer( bSizer5 )
		self.pnlLeft.Layout()
		bSizer5.Fit( self.pnlLeft )
		self.pnlMain = wx.Panel( self.splGrid, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.nBook = wx.Notebook( self.pnlMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )

		bSizer6.Add( self.nBook, 1, wx.EXPAND |wx.ALL, 5 )


		self.pnlMain.SetSizer( bSizer6 )
		self.pnlMain.Layout()
		bSizer6.Fit( self.pnlMain )
		self.splGrid.SplitVertically( self.pnlLeft, self.pnlMain, 220 )
		bSizer7.Add( self.splGrid, 1, wx.ALIGN_LEFT|wx.EXPAND, 5 )


		self.pnlSplitter.SetSizer( bSizer7 )
		self.pnlSplitter.Layout()
		bSizer7.Fit( self.pnlSplitter )
		self.pnlOutput = wx.Panel( self.splMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.txtOutput = wx.TextCtrl( self.pnlOutput, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.txtOutput, 1, wx.ALL|wx.EXPAND, 5 )


		self.pnlOutput.SetSizer( bSizer8 )
		self.pnlOutput.Layout()
		bSizer8.Fit( self.pnlOutput )
		self.splMain.SplitHorizontally( self.pnlSplitter, self.pnlOutput, 250 )
		bSizer2.Add( self.splMain, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.onExport, id = self.mnuExport.GetId() )
		self.Bind( wx.EVT_MENU, self.onSettings, id = self.mnuSettings.GetId() )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.mnuExit.GetId() )
		self.Bind( wx.EVT_MENU, self.onLoadSnap, id = self.mnuLoadSnap.GetId() )
		self.Bind( wx.EVT_MENU, self.onExecute, id = self.mnuExecute.GetId() )
		self.Bind( wx.EVT_MENU, self.on_apply_snapp, id = self.mnuApplySnapp.GetId() )
		self.Bind( wx.EVT_MENU, self.onTutorial, id = self.mnuTutorial.GetId() )
		self.Bind( wx.EVT_MENU, self.onAbout, id = self.mnuAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onExport( self, event ):
		event.Skip()

	def onSettings( self, event ):
		event.Skip()

	def onExit( self, event ):
		event.Skip()

	def onLoadSnap( self, event ):
		event.Skip()

	def onExecute( self, event ):
		event.Skip()

	def on_apply_snapp( self, event ):
		event.Skip()

	def onTutorial( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()

	def splMainOnIdle( self, event ):
		self.splMain.SetSashPosition( 250 )
		self.splMain.Unbind( wx.EVT_IDLE )

	def splGridOnIdle( self, event ):
		self.splGrid.SetSashPosition( 220 )
		self.splGrid.Unbind( wx.EVT_IDLE )


###########################################################################
## Class dlgSettings
###########################################################################

class dlgSettings ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Settings", pos = wx.DefaultPosition, size = wx.Size( 546,342 ), style = wx.CAPTION|wx.CLOSE_BOX )

		self.SetSizeHints( wx.Size( 200,200 ), wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,320 ), wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.pgSettings = pg.PropertyGrid(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_DEFAULT_STYLE|wx.TAB_TRAVERSAL)
		bSizer13.Add( self.pgSettings, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer13 )
		self.m_panel10.Layout()
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onSettingsSave )
		self.Bind( wx.EVT_INIT_DIALOG, self.onSettingsLoad )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSettingsSave( self, event ):
		event.Skip()

	def onSettingsLoad( self, event ):
		event.Skip()


###########################################################################
## Class dlgAbout
###########################################################################

class dlgAbout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 403,401 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"icons/main-icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"State Estimator", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"0.0.1 Beta", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		bSizer15.Add( self.m_staticText4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"File Hunter is an advanced file manager for\nthe Unix operating system. Features include powerful built-in editor,\nadvanced search capabilities, powerful batch renaming, file comparison,\nextensive archive handling and more.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		bSizer15.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"http://www.daali.ir", u"http://www.daali.ir", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_DEFAULT_STYLE )
		bSizer16.Add( self.m_hyperlink1, 0, wx.EXPAND|wx.ALL, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"© 2020 - 2024 SeStim", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText5.Wrap( -1 )

		bSizer15.Add( self.m_staticText5, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnCredit = wx.Button( self, wx.ID_ANY, u"Credit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.btnCredit, 0, wx.ALL, 5 )

		self.btnLicense = wx.Button( self, wx.ID_ANY, u"License", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.btnLicense, 0, wx.ALL, 5 )


		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnClose = wx.Button( self, wx.ID_OK, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnClose.SetDefault()
		bSizer17.Add( self.btnClose, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnCredit.Bind( wx.EVT_BUTTON, self.onCredit )
		self.btnLicense.Bind( wx.EVT_BUTTON, self.onLicense )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onCredit( self, event ):
		event.Skip()

	def onLicense( self, event ):
		event.Skip()


###########################################################################
## Class dlgInfoBox
###########################################################################

class dlgInfoBox ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,204 ), wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.txtInfo = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,158 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer18.Add( self.txtInfo, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnPrint = wx.Button( self.m_panel12, wx.ID_ANY, u"&Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.btnPrint, 0, wx.ALL, 5 )

		self.btnCopy = wx.Button( self.m_panel12, wx.ID_ANY, u"&Copy", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.btnCopy, 0, wx.ALL, 5 )


		bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnClose = wx.Button( self.m_panel12, wx.ID_OK, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnClose.SetDefault()
		bSizer19.Add( self.btnClose, 0, wx.ALL, 5 )


		bSizer18.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.m_panel12.SetSizer( bSizer18 )
		self.m_panel12.Layout()
		bSizer21.Add( self.m_panel12, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer21 )
		self.Layout()
		bSizer21.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnPrint.Bind( wx.EVT_BUTTON, self.onPrint )
		self.btnCopy.Bind( wx.EVT_BUTTON, self.onCopy )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onPrint( self, event ):
		event.Skip()

	def onCopy( self, event ):
		event.Skip()


