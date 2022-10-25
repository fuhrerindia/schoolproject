from patient import newpatient
from mainmenu import rootmenu
from constant import show_options
show_options([{
    'm': 'Patient Menu',
    'f': newpatient
}, {
    'm': 'Main Menu',
    'f': rootmenu
}])