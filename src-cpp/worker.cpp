#include <QObject>
#include <chrono>
#include <thread>

#include "worker.h"

//Worker::Worker(QObject *parent) : QObject(parent)
Worker::Worker() : QObject()
{
    //"""Class for process running in background thread"""
    //QObject.__init__(self) . TODO!!
    //self._mutex = QMutex()
    this->_running = true;
}


    //def stop(self):
    //    """
    //    Switches infinite while loop condition to False
    //    """
    //    self._mutex.lock()
    //    self._running = False
    //     self._mutex.unlock()

    bool Worker::running() {

        //try:
        //    self._mutex.lock()
            return _running;
        //finally:
        //    self._mutex.unlock()
    }

    void Worker::runSession() {

        while (running())
        {
            std::this_thread::sleep_for(std::chrono::milliseconds(1000)); // sleep for 1 second
            emit progress();

        }
        emit workFinished();
    }


