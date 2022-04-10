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

    connect(start_button, &QPushButton::released,
            this, &Sprinter::startSessionInThread);
    connect(textarea, &QTextEdit::textChanged,
            this, &Sprinter::updateTextchangedTime);

    //shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), textarea)
    //shortcut.activated.connect(backup_text_to_disk)
}

void Sprinter::startSessionInThread()
{
    int minutes_per_sprint = minutes_per_sprint_spinbox->value();
    int target_wordcount = target_wordcount_spinbox->value();
    int severity = severity_slider->value();

    QString initialTextString = textarea->toPlainText();
    Text text = Text(initialTextString);
    session = Session(minutes_per_sprint,
                      target_wordcount,
                      severity,
                      text);

    QThread* thread = new QThread();
    worker = new Worker();

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
    //    start_button.setEnabled(False)
    //    thread.finished.connect(
    //        lambda: start_button.setEnabled(True)
    //    )
}

void Sprinter::updateStatus() {

    if ((session.seconds_remaining > 0) & (session.words_remaining > 0)) {

        QString currentTextString = textarea->toPlainText();

        // update all session variables
        session.update_session_status(currentTextString);

        // update text in labels in UI
        updateStatusBar();

        checkAlarmCondition();

        return;
    }

    if (session.seconds_remaining <=0) {
        std::cout << "Times up!";
        worker->stop();
    }

    if (session.words_remaining <= 0) {
        std::cout << "Well done!";
        worker->stop();
    }
}

void Sprinter::updateStatusBar() {
//    """
//    Update text in labels in the status bar in the UI.
//    """

    int addedWordcount = session.text.addedWordcount;
    int minutes_remaining = session.minutes_remaining;
    int perc_time_remaining = session.perc_time_remaining;
    int perc_wc_achieved = session.perc_wc_achieved;

    QString tr_text = QString("%1:00").arg(minutes_remaining);
    time_remaining_value_label->setText(tr_text);
    time_remaining_progressBar->setProperty("value", perc_time_remaining);

    QString wc_text = QString("%1 / %2").arg(addedWordcount).arg(session.target_wordcount);
    wordcount_value_label->setText(wc_text);
    wordcount_progressBar->setProperty("value", perc_wc_achieved);
}
    
void Sprinter::checkAlarmCondition() {
/*
"""
Change app colour scheme based on number of seconds since last
user interaction with text area

# TODO linear change from pink to red
"""*/

    int seconds_since_last_interaction = time(NULL) - session.time_lastmodified_textarea;

    if (seconds_since_last_interaction > session.seconds_allowed_since_lastmodified) {
        textarea->setStyleSheet("QTextEdit { background-color: rgb(255, 0, 0); color: black;}");
        std::cout << "alarm!";
    } else {
        textarea->setStyleSheet("QTextEdit { background-color: rgb(0, 0, 0); color: white;}");
    }

}

void Sprinter::updateTextchangedTime()
{
    /*
    Record the time at which the user last changed the text
    in the textarea
    */

    session.time_lastmodified_textarea = time(NULL);
}