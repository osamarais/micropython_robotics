# Main Program



# First make all the necessary imports
# import PyQt stuff and sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from category_class import *

# create the application
game_manager_app = QApplication(sys.argv)


###############################################################################################################
###############################################################################################################
#################   PUT UI HERE ##################################

#################################################################################

# Main Window UI

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 357)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.category_box = QtWidgets.QGroupBox(self.centralwidget)
        self.category_box.setObjectName("category_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.category_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_category_button = QtWidgets.QPushButton(self.category_box)
        self.add_category_button.setObjectName("add_category_button")
        self.gridLayout_2.addWidget(self.add_category_button, 0, 1, 1, 1)
        self.category_list = QtWidgets.QListWidget(self.category_box)
        self.category_list.setObjectName("category_list")
        self.gridLayout_2.addWidget(self.category_list, 0, 0, 3, 1)
        self.remove_category_button = QtWidgets.QPushButton(self.category_box)
        self.remove_category_button.setObjectName("remove_category_button")
        self.gridLayout_2.addWidget(self.remove_category_button, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.category_box)
        self.members_box = QtWidgets.QGroupBox(self.centralwidget)
        self.members_box.setObjectName("members_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.members_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.members_list = QtWidgets.QListWidget(self.members_box)
        self.members_list.setObjectName("members_list")
        self.gridLayout_3.addWidget(self.members_list, 0, 0, 2, 1)
        self.horizontalLayout.addWidget(self.members_box)
        self.details_box = QtWidgets.QGroupBox(self.centralwidget)
        self.details_box.setObjectName("details_box")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.details_box)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.broadcast_checkbox = QtWidgets.QCheckBox(self.details_box)
        self.broadcast_checkbox.setObjectName("broadcast_checkbox")
        self.gridLayout_4.addWidget(self.broadcast_checkbox, 0, 0, 1, 1)
        self.IP_field = QtWidgets.QLineEdit(self.details_box)
        self.IP_field.setObjectName("IP_field")
        self.gridLayout_4.addWidget(self.IP_field, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.details_box)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.details_box)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.can_see_list = QtWidgets.QListWidget(self.details_box)
        self.can_see_list.setObjectName("can_see_list")
        self.gridLayout_4.addWidget(self.can_see_list, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.details_box)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thicc Boi"))
        self.category_box.setTitle(_translate("MainWindow", "Category"))
        self.add_category_button.setText(_translate("MainWindow", "Add"))
        self.remove_category_button.setText(_translate("MainWindow", "Remove"))
        self.members_box.setTitle(_translate("MainWindow", "Members"))
        self.details_box.setTitle(_translate("MainWindow", "Details"))
        self.broadcast_checkbox.setText(_translate("MainWindow", "Broadcast"))
        self.label_2.setText(_translate("MainWindow", "I.P. : Port"))
        self.label_4.setText(_translate("MainWindow", "Can see:"))




#################################################################################

# Add category dialog UI


class Ui_AddCategory(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(438, 468)
		self.gridLayout = QtWidgets.QGridLayout(Form)
		self.gridLayout.setObjectName("gridLayout")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.name_input = QtWidgets.QLineEdit(Form)
		self.name_input.setObjectName("name_input")
		self.gridLayout.addWidget(self.name_input, 0, 1, 1, 1)
		self.label = QtWidgets.QLabel(Form)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.label_7 = QtWidgets.QLabel(Form)
		self.label_7.setObjectName("label_7")
		self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
		self.members_selection = QtWidgets.QListWidget(Form)
		self.members_selection.setObjectName("members_selection")
		self.gridLayout.addWidget(self.members_selection, 1, 1, 1, 1)
		self.can_see = QtWidgets.QLineEdit(Form)
		self.can_see.setObjectName("can_see")
		self.gridLayout.addWidget(self.can_see, 3, 1, 1, 1)
		self.IP = QtWidgets.QLineEdit(Form)
		self.IP.setObjectName("IP")
		self.gridLayout.addWidget(self.IP, 4, 1, 1, 1)
		self.label_3 = QtWidgets.QLabel(Form)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
		self.broadcastable = QtWidgets.QCheckBox(Form)
		self.broadcastable.setText("")
		self.broadcastable.setObjectName("broadcastable")
		self.gridLayout.addWidget(self.broadcastable, 2, 1, 1, 1)
		self.add_category_button = QtWidgets.QPushButton(Form)
		self.add_category_button.setObjectName("add_category_button")
		self.gridLayout.addWidget(self.add_category_button, 5, 1, 1, 1)
		self.label_4 = QtWidgets.QLabel(Form)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Add Category"))
		self.label_2.setText(_translate("Form", "Members:"))
		self.name_input.setText(_translate("Form", "Category_Name_without_spaces"))
		self.label.setText(_translate("Form", "Name:"))
		self.label_7.setText(_translate("Form", "IP and Port:"))
		self.can_see.setText(_translate("Form", "visible categories seperated by spaces"))
		self.IP.setText(_translate("Form", "0.0.0.0:8000"))
		self.label_3.setText(_translate("Form", "Broadcastable"))
		self.add_category_button.setText(_translate("Form", "Add"))
		self.label_4.setText(_translate("Form", "Can see categories:"))



###############################################################################################################
###############################################################################################################
#################   SET UP UI HERE ##################################


###########################################################################################

# Main Windows setup
# Make the main window
class main_window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.category_list.setSelectionMode(1)
		self.ui.members_list.setSelectionMode(0)
		self.ui.broadcast_checkbox.setEnabled(False)
		self.ui.broadcast_checkbox.setEnabled(False)
		self.ui.broadcast_checkbox.setEnabled(False)


mainwindow = main_window()
mainwindow.show()

# open add category dialog when clicked
#w.ui.add_category_button.clicked.connect(open_category_dialog)



###########################################################################################

## add category dialog setup

class add_category_dialog(QWidget):
	def __init__(self):
		super().__init__()
		self.ui = Ui_AddCategory()
		self.ui.setupUi(self)
		self.ui.members_selection.setSelectionMode(2)

addcategorydialog = add_category_dialog()
#addcategorydialog.show()


###############################################################################################################
###############################################################################################################
#################   MAKE CALLBACKS HERE ##################################

def load_category_dialog():
	# clear all previous info; reset the dialog
	addcategorydialog.ui.members_selection.clear()
	# look at all the unidentidfied markers
	#unidentifiedmarkers = [str(x) for x in unidentifiedmarkers]
	categorynames = [x.name for x in category.instances]
	indexofunidentified = categorynames.index('unidentified')
	unidentifiedcategory = category.instances[indexofunidentified]
	addcategorydialog.ui.members_selection.addItems(unidentifiedcategory.members)
	# add all the unidentified markers to the 
	update_unidentified_category()
	togglebroadcastable()
	addcategorydialog.show()

def add_category():
	# use the current state of the add category dialog to create a category
	name = addcategorydialog.ui.name_input.text()
	if name == 'unidentified':
		return
	if any([x.name == name for x in category.instances]):
		print('Category already exists!')
		return
	if (name.find(' ') + 1):
		print('Spaces not allowed')
		return
	members = [x.text() for x in addcategorydialog.ui.members_selection.selectedItems()]
	broadcastable = addcategorydialog.ui.broadcastable.isChecked()
	if broadcastable:
		cansee = addcategorydialog.ui.can_see.text()
		cansee = str.split(cansee)
		#filters = addcategorydialog.ui.filters.text()
		#filters = str.split(filters)
		ip = addcategorydialog.ui.IP.text()
		if not(isvalidIPandPort(ip)):
			print('Please enter a valid IP address')
			return()
	else:
		cansee = []
		ip = []
	category(name,members,broadcastable,cansee,ip)
	# then close the window
	addcategorydialog.hide()
	update_unidentified_category()
	update_categories_list()
	
def update_unidentified_category():
	# first delete the unidentified category
	update_allmarkers()
	categorynames = [x.name for x in category.instances]
	indexofunidentified = categorynames.index('unidentified')
	unidentifiedcategory = category.instances[indexofunidentified]
	unidentifiedcategory.members = []
	#unidentifiedcategory.__del__()
	# now make a list that has all the unidentified markers in it
	identifiedmarkers = [x.members for x in category.instances]
	identifiedmarkers = [x for sub in identifiedmarkers for x in sub]
	#global unidentifiedmarkers
	unidentifiedmarkers = [x for x in allmarkers if x not in identifiedmarkers]
	#category('unidentified', members = unidentifiedmarkers)
	unidentifiedcategory.members = unidentifiedmarkers
	#print('updated unidentified category')

def update_categories_list():
	categorynames = [x.name for x in category.instances]
	mainwindow.ui.category_list.clear()
	mainwindow.ui.category_list.addItems(categorynames)
	mainwindow.ui.members_list.clear()
	update_members_list()

def update_members_list():
	update_unidentified_category()
	selecteditemindex = mainwindow.ui.category_list.selectedIndexes()
	if selecteditemindex:
		# now get row and update
		selecteditemindex = selecteditemindex[0].row()
		categorymembers = category.instances[selecteditemindex].members
		mainwindow.ui.members_list.clear()
		mainwindow.ui.members_list.addItems(categorymembers)
	else:
		#now clear the list
		mainwindow.ui.members_list.clear()
	update_details()

def remove_category():
	selecteditemindex = mainwindow.ui.category_list.selectedIndexes()
	if selecteditemindex:
		selecteditemindex = selecteditemindex[0].row()
		categorytodelete = category.instances[selecteditemindex]
		if categorytodelete.name == 'unidentified':
			return
		categorytodelete.__del__()
	else:
		pass
	update_unidentified_category()
	update_categories_list()

def update_details():
	selecteditemindex = mainwindow.ui.category_list.selectedIndexes()
	if selecteditemindex:
		selecteditemindex = selecteditemindex[0].row()
		categoryofinterest = category.instances[selecteditemindex]
		#now update the details
		if categoryofinterest.broadcastable:
			mainwindow.ui.broadcast_checkbox.setCheckState(2)
			mainwindow.ui.can_see_list.clear()
			mainwindow.ui.can_see_list.addItems(categoryofinterest.cansee)
			#mainwindow.ui.is_visible_to_list.clear()
			#mainwindow.ui.is_visible_to_list.addItems(categoryofinterest.isvisibleto)
			#mainwindow.ui.data_filter_list.clear()
			#mainwindow.ui.data_filter_list.addItems(categoryofinterest.filters)
			mainwindow.ui.IP_field.clear()
			mainwindow.ui.IP_field.setText(categoryofinterest.IP)
		else:
			mainwindow.ui.broadcast_checkbox.setCheckState(0)
			mainwindow.ui.can_see_list.clear()
			#mainwindow.ui.is_visible_to_list.clear()
			#mainwindow.ui.data_filter_list.clear()
			mainwindow.ui.IP_field.clear()

			
	else:
		# clear all the fields
		mainwindow.ui.broadcast_checkbox.setCheckState(0)
		mainwindow.ui.can_see_list.clear()
		#mainwindow.ui.is_visible_to_list.clear()
		#mainwindow.ui.data_filter_list.clear()
		mainwindow.ui.IP_field.clear()

def update_allmarkers():
	d.Update()
	global allmarkers
	allmarkers = d.list_ID()
	##########################
	# latest change#
	allmarkers.sort()
	allmarkers = [str(x) for x in allmarkers]


def togglebroadcastable():
	if addcategorydialog.ui.broadcastable.isChecked():
		addcategorydialog.ui.can_see.setEnabled(True)
		addcategorydialog.ui.IP.setEnabled(True)
	else:
		addcategorydialog.ui.can_see.setEnabled(False)
		addcategorydialog.ui.IP.setEnabled(False)

def isvalidIPandPort(address):
	try:
		IP,port = str.split(address,':')
		socket.inet_aton(IP)
		port = int(port)
		if port > -1 and port < 65536:
			return True
		else:
			print('Port out of valid range')
			return False
	except OSError:
		print('Invalid IP')
		return False
	except ValueError:
		print('Incorrect Format')
		return False
	except TypeError:
		print('Port Must be an Integer')
		return False
	finally:
		pass


###############################################################################################################
###############################################################################################################
#################   MAKE CONNECTIONS HERE ##################################

mainwindow.ui.add_category_button.clicked.connect(load_category_dialog)
mainwindow.ui.remove_category_button.clicked.connect(remove_category)
mainwindow.ui.category_list.itemClicked.connect(update_members_list)


addcategorydialog.ui.add_category_button.clicked.connect(add_category)
addcategorydialog.ui.broadcastable.clicked.connect(togglebroadcastable)





###############################################################################################################
###############################################################################################################
#################   INITIALIZE ENVIRONMENT HERE ##################################

# create the unidentified category for the first time
#allmarkers = ['2','3','55','64','32','57','65','34','54','3']
#unidentifiedmarkers = []
#category('unidentified')
#update_unidentified_category()
#update_categories_list()













####################################################
# run as an app
#sys.exit(game_manager_app.exec_())



