#include <QObject>
#include <chrono>
#include <thread>

#include "worker.h"

Worker::Worker() : QObject()
{
    //"""Class for process running in background thread"""
    //QObject.__init__(self) . TODO!!
    //self._mutex = QMutex()
    this->_running = true;
}


// Switches infinite while loop condition to False
void Worker::stop() {
    //    self._mutex.lock()
    _running = false;
    //     self._mutex.unlock()

}

bool Worker::running() {

    //try:
    //    self._mutex.lock()
        return _running;
    //finally:
    //    self._mutex.unlock()
}

void Worker::runSession() {

    while (running()) {
        std::this_thread::sleep_for(std::chrono::milliseconds(5000)); // sleep for 1 second
        emit progress();
    }
    emit workFinished();
}
