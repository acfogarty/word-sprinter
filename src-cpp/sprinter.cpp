#include <iostream>
#include <string>
#include <QtWidgets>
#include <QMainWindow>

#include <cmath>

#include "sprinter.h"
#include "text.h"

Sprinter::Sprinter(QMainWindow *parent)
    : QMainWindow(parent)
{

    setupUi(this);

    //self.app = app

    //# Force the style to be the same on all OSs:
    //self.app.setStyle("Fusion")

    //palette = make_darktheme_palette()
    //self.app.setPalette(palette)

    //self.start_button.clicked.connect(self.start_session_in_thread)
    //self.textarea.textChanged.connect(self.update_textchanged_time)

    connect(start_button, &QPushButton::released,
            this, &Sprinter::startSessionInThread);
    connect(textarea, &QPlainTextEdit::textChanged,
            this, &Sprinter::updateTextchangedTime);

    //shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self.textarea)
    //shortcut.activated.connect(self.backup_text_to_disk)
}

void Sprinter::startSessionInThread()
{
    int minutes_per_sprint = minutes_per_sprint_spinbox->value();
    int target_wordcount = target_wordcount_spinbox->value();
    int severity = severity_slider->value();

    QString initial_text_string = textarea->toPlainText();
    start_button->setText("Example");
    std::cout << "Hello World!";
    Text text = Text(initial_text_string=initial_text_string);
    //session = Session(minutes_per_sprint=minutes_per_sprint,
    //                  target_wordcount=target_wordcount,
    //                  severity=severity,
    //                  text=text);
}

void Sprinter::updateTextchangedTime()
{
    std::cout << "Hello World!";
    start_button->setText("Yay");
}
