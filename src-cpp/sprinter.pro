QT += widgets

HEADERS       = sprinter.h \
                worker.h \
                text.h
SOURCES       = sprinter.cpp \
                worker.cpp \
                text.cpp \
                main.cpp

FORMS = sprintermainwindow.ui

# install
target.path = wordsprinter
INSTALLS += target
