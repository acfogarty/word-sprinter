#include <QObject>
#include <QThread>

class Worker : public QObject
{
Q_OBJECT
public:
    Worker();
    //explicit Worker(QObject *parent = 0);
    //~Worker();

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