#include "text.h"

Text::Text(QString initial_text_string)
{

    initialWordcount = countWords(initial_text_string);
    currentWordcount = initialWordcount;
    addedWordcount = getAddedWordcount();

}

void Text::updateWordcountInfo(QString currentTextString) {

    currentWordcount = countWords(currentTextString);
    addedWordcount = getAddedWordcount();
}

int Text::countWords(QString textString) {
    // """Counts words using same method as linux wc"""

    // TODO
    //wc = len(text_string.split())

    return 5;
}

int Text::getAddedWordcount() {
    return currentWordcount - initialWordcount;
}

