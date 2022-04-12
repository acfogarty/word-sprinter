#include <time.h>
#include <math.h>

#include "session.h"
#include "text.h"


Session::Session() {}
Session::Session(int _minutes_per_sprint, int _target_wordcount,
                 int severity, Text _text) {

// parameters for mapping slider to seconds
// TODO make constant
severity_slider_max_value = 100.0;
max_seconds_grace_period = 30.0;

    text = _text;

    minutes_per_sprint = _minutes_per_sprint;
    minutes_remaining = minutes_per_sprint;
    seconds_remaining = minutes_per_sprint * 60;
    perc_time_remaining = 100;

    starttime = time(NULL);
    finishtime = starttime + minutes_per_sprint * 60;

    target_wordcount = _target_wordcount;
    words_remaining = target_wordcount;
    perc_wc_achieved = 0;

    time_lastmodified_textarea = time(NULL);
    seconds_allowed_since_lastmodified = calc_grace_period(severity);

}

void Session::update_session_status(QString current_text_string) {

    text.updateWordcountInfo(current_text_string);

    calc_minutes_remaining();

    calc_word_stats();
}

void Session::calc_minutes_remaining() {

    seconds_remaining = finishtime - time(NULL);
    minutes_remaining = round(seconds_remaining / 60.0);
    minutes_remaining = std::max(minutes_remaining, 0);

    if (minutes_per_sprint > 0) {
        perc_time_remaining = int((float)minutes_remaining / (float)minutes_per_sprint * 100);
    } else {
        perc_time_remaining = 0;
    }

}

void Session::calc_word_stats() {

    words_remaining = target_wordcount - text.addedWordcount;

    if (target_wordcount > 0) {
        perc_wc_achieved = int((float)text.addedWordcount / (float)target_wordcount * 100);
    }
    else {
        perc_wc_achieved = 0;
    }
}

int Session::calc_grace_period(int severity){
//        Map from slider value to seconds

    return int((float)severity / severity_slider_max_value * max_seconds_grace_period);
}
