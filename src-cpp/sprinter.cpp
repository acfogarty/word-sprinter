#include <iostream>
#include <string>
#include <QtWidgets>
#include <QMainWindow>

#include <cmath>

#include "sprinter.h"
#include "text.h"
#include "worker.h"

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

    QString initialTextString = textarea->toPlainText();
    start_button->setText("Example");
    std::cout << "Hello World!";
    Text text = Text(initialTextString);
    //session = Session(minutes_per_sprint=minutes_per_sprint,
    //                  target_wordcount=target_wordcount,
    //                  severity=severity,
    //                  text=text);
    QThread* thread = new QThread();
    Worker* worker = new Worker();

    // move the worker object to the thread BEFORE connecting any signal/slots
    worker->moveToThread(thread);

    connect(thread, SIGNAL(started()), worker, SLOT(runSession()));
    connect(worker, SIGNAL(workFinished()), thread, SLOT(quit()));

    // automatically delete thread and worker object when work is done:
    connect(worker, SIGNAL(workFinished()), worker, SLOT(deleteLater()));
    connect(thread, SIGNAL(finished()), thread, SLOT(deleteLater()));

    connect(worker, SIGNAL(progress()), this, SLOT(updateStatus()));

    updateStatus();

    thread->start();

    //    # Final resets
    //    self.start_button.setEnabled(False)
    //    self.thread.finished.connect(
    //        lambda: self.start_button.setEnabled(True)
    //    )
}

void Sprinter::updateStatus() {

        std::cout << "Update Status" << std::endl;

        //if (self.session.seconds_remaining > 0) and (self.session.words_remaining > 0):
        if (true) {

            QString currentTextString = textarea->toPlainText();

            // update all session variables
            //session.updateSessionStatus(currentTextString);

            // update text in labels in UI
            //updateStatusBar();

            //checkAlarmCondition();
            start_button->setText("Wow");

            return;
        }

        //if self.session.seconds_remaining <=0:
        //    self.worker.stop()
        //    print('Times up!')

        //if self.session.words_remaining <= 0:
        //    self.worker.stop()
        //    print('Well done!')
    }

void Sprinter::updateTextchangedTime()
{
    std::cout << "Hello World!";
    start_button->setText("Yay");
}
