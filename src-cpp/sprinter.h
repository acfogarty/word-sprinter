#ifndef SPRINTER_H
#define SPRINTER_H

#include <QWidget>
#include <QMainWindow>

#include "ui_sprintermainwindow.h"
#include "session.h"
#include "worker.h"

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
    void backup_text_to_disk();

private:
    Session session;
    Worker* worker;
    void updateStatusBar();
    void checkAlarmCondition();
};

#endif
