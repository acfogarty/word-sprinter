#ifndef SPRINTER_H
#define SPRINTER_H

#include <QWidget>

class Sprinter : public QWidget
{
    Q_OBJECT

public:
    Sprinter(QWidget *parent = 0);

private:
    double sumInMemory;
};

#endif
