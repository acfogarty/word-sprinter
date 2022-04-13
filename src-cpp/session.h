#ifndef SESSION_H
#define SESSION_H

#include <QString>
#include "text.h"

class Session {

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

    void update_session_status(QString current_text_string);
    void calc_minutes_remaining();
    void calc_word_stats();

    // time since textarea was last modified
    int time_lastmodified_textarea;
    // during the grace period, the textarea background retains its original color
    int seconds_grace_period;
    // grace period when the slider is set to maximum severity
    int seconds_grace_period_at_max_slider;
    // during the color change period, the textarea changes to red
    int seconds_color_change;
    int severity_slider_max_value;
    void calc_grace_period(int severity);

private:
    //TODO transfer private variables here
};

#endif
