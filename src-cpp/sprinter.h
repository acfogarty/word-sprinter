#ifndef SPRINTER_H
#define SPRINTER_H

#include <QWidget>
#include <QMainWindow>

#include "ui_sprintermainwindow.h"
#include "session.h"

class Sprinter : public QMainWindow, private Ui_MainWindow
{
    Q_OBJECT

public:
    Sprinter(QMainWindow *parent = 0);

public slots:
    void updateStatus();

private slots:
    void startSessionInThread();
    void updateTextchangedTime();

private:
    Session session;
    void updateStatusBar();
    void checkAlarmCondition();
};

#endif
