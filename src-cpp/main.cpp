#include <QApplication>

#include "sprinter.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Sprinter sprinter;
    sprinter.show();
    return app.exec();
}
