QT += widgets

HEADERS       = sprinter.h 
SOURCES       = sprinter.cpp \
                main.cpp

FORMS = sprintermainwindow.ui

# install
target.path = wordsprinter
INSTALLS += target
