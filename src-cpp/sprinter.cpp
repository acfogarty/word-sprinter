#include <QtWidgets>
#include <QMainWindow>

#include <cmath>

#include "sprinter.h"

Sprinter::Sprinter(QMainWindow *parent)
    : QMainWindow(parent)
{
    sumInMemory = 0.0;

    setupUi(this);
}

