#ifndef TEXT_H
#define TEXT_H

#include <QString>

class Text {

public:
    Text();
    Text(QString initialTextString);

public:
    int initialWordcount;
    int currentWordcount;
    int addedWordcount;
    void updateWordcountInfo(QString currentTextString);

private:
    int countWords(QString textString);
    int getAddedWordcount();
};

#endif
