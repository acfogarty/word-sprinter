#ifndef SESSION_H
#define SESSION_H

#include <QString>
#include "text.h"

class Session
{

public:
    Session();
    Session(int minutes_per_sprint, int target_wordcount,
                 int severity, Text text);

public:
    Text text;

    int minutes_per_sprint;
    int minutes_remaining;
    int seconds_remaining;
    int perc_time_remaining;

    int starttime;
    int finishtime;

    int target_wordcount;
    int words_remaining;
    int perc_wc_achieved;

    int time_lastmodified_textarea;
    int seconds_allowed_since_lastmodified;
    void update_session_status(QString current_text_string);
    void calc_minutes_remaining();
    void calc_word_stats();
    int calc_grace_period(int severity);
    int severity_slider_max_value;
    int max_seconds_grace_period;

private:
    //TODO transfer private variables here
};

#endif
