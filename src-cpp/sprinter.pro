QT += widgets

HEADERS       = sprinter.h \
                text.h
SOURCES       = sprinter.cpp \
                text.cpp \
                main.cpp

FORMS = sprintermainwindow.ui

# install
target.path = wordsprinter
INSTALLS += target
