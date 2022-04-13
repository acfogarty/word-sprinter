#include <QString>
#include <QStringList>
#include <QRegularExpression>
#include "text.h"

Text::Text() {}

Text::Text(QString initialTextString) {

    initialWordcount = countWords(initialTextString);
    currentWordcount = initialWordcount;
    addedWordcount = getAddedWordcount();

}

void Text::updateWordcountInfo(QString currentTextString) {

    currentWordcount = countWords(currentTextString);
    addedWordcount = getAddedWordcount();
}

// Counts words using same method as linux wc
int Text::countWords(QString textString) {

    QStringList words = textString.split(QRegularExpression("\\s+"),
                                         Qt::SkipEmptyParts);
    int wc = words.length();

    return wc;
}

int Text::getAddedWordcount() {
    return currentWordcount - initialWordcount;
}
