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

private:
    double sumInMemory;
};

#endif
