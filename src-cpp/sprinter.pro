QT += widgets

HEADERS       = sprinter.h \
                worker.h \
                session.h \
                text.h
SOURCES       = sprinter.cpp \
                worker.cpp \
                session.cpp \
                text.cpp \
                main.cpp

FORMS = sprintermainwindow.ui

# install
target.path = wordsprinter
INSTALLS += target
