#include <iostream>
#include <string>
#include <QtWidgets>
#include <QShortcut>
#include <QKeySequence>
#include <QMainWindow>
#include <QDebug>

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
    connect(textarea, &QPlainTextEdit::textChanged,
            this, &Sprinter::updateTextchangedTime);

    QShortcut* shortcut = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_S), this);
    connect(shortcut, &QShortcut::activated, this, &Sprinter::backup_text_to_disk);
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
    time_remaining_progressBar->setValue(perc_time_remaining);

    QString wc_text = QString("%1 / %2").arg(addedWordcount).arg(session.target_wordcount);
    wordcount_value_label->setText(wc_text);
    wordcount_progressBar->setValue(perc_wc_achieved);
}
    
void Sprinter::checkAlarmCondition() {
/*
"""
Change app colour scheme based on number of seconds since last
user interaction with text area

Seconds_since_last_interaction < seconds_allows_since

"""*/

    int seconds_since_last_interaction = time(NULL) - session.time_lastmodified_textarea;
    int red;
    int green;
    int blue;
    int redmin = 21;
    int redmax = 255;
    int greenmin = 21;
    int greenmax = 0;
    int bluemin = 21;
    int bluemax = 0;
    QString textcolor;

    // during the grace period, the textarea background retains its original color
    // during the color change period, the textarea changes to red

    red = linearColorMap(seconds_since_last_interaction, redmin, redmax,
                         session.seconds_grace_period, session.seconds_color_change);
    green = linearColorMap(seconds_since_last_interaction, greenmin, greenmax,
                         session.seconds_grace_period, session.seconds_color_change);
    blue = linearColorMap(seconds_since_last_interaction, bluemin, bluemax,
                         session.seconds_grace_period, session.seconds_color_change);

    int brightness = calcBrightness(red, green, blue);
    qDebug() << "brightness: " << brightness;

    if (brightness < 60) {
        textcolor = "white";
    } else {
        textcolor = "black";
    }

    QString stylesheet = QString("QPlainTextEdit { background-color: rgb(%1, %2, %3); color: %4}").arg(red).arg(green).arg(blue).arg(textcolor);
    textarea->setStyleSheet(stylesheet);
}

int Sprinter::calcBrightness(int red, int green, int blue) {
    return (red + red + blue + green + green + green) / 6;
}

int Sprinter::linearColorMap(int seconds, int colorMin, int colorMax,
                              int secondsStartChange, int secondsChangePeriod) {
/* 0 to secondsStartChange seconds: color is colorMin
    secondsStartChange to secondsStartChange+secondsChangePeriod: linear color change
    > secondsStartChange+secondsChangePeriod seconds: color is colorMax */

    if (seconds < secondsStartChange) {
        return colorMin;
    }

    if (seconds > secondsStartChange + secondsChangePeriod) {
        return colorMax;
    }

    int slope = (colorMax - colorMin) / (float) secondsChangePeriod;
    int intercept = colorMin - slope * secondsStartChange;

    return (int) (slope * seconds + intercept);
}

void Sprinter::updateTextchangedTime()
{
    /*
    Record the time at which the user last changed the text
    in the textarea
    */

    session.time_lastmodified_textarea = time(NULL);
}

void Sprinter::backup_text_to_disk()
{
/*
        """
        Save contents of textarea to temporary file on disk
        """
*/

        QString current_text_string = textarea->toPlainText();

        // TODO set path to write to instead of hard coding
        QFile file("/Users/aoife/sprinter.bkp.txt");
        file.open(QIODevice::WriteOnly);
        file.write(current_text_string.toUtf8());
        file.close();

        qDebug() << "Backed up text to disk.";
}
