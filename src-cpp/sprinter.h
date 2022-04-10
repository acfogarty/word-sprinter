#ifndef SPRINTER_H
#define SPRINTER_H

#include <QWidget>
#include <QMainWindow>

#include "ui_sprintermainwindow.h"

class Sprinter : public QMainWindow, private Ui_MainWindow
{
    Q_OBJECT

public:
    Sprinter(QMainWindow *parent = 0);

private slots:
    void startSessionInThread();
    void updateTextchangedTime();

private:
    int minutes_per_sprint;
    int target_wordcount;
    int severity;
    //Session session;
};

#endif
