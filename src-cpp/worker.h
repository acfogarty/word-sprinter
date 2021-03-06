#ifndef WORKER_H
#define WORKER_H

#include <QObject>
#include <QThread>

class Worker : public QObject {
Q_OBJECT
public:
    Worker();

    void stop();

private:
    bool _running;
    bool running();

public slots:
    // runSession must emit workFinished when it is done.
    void runSession();
signals:
    void workFinished();
    void progress();
};

#endif
