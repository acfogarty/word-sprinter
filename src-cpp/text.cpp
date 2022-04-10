#include <QString>
#include <QStringList>
#include <QRegularExpression>
#include "text.h"

Text::Text()
{}

Text::Text(QString initialTextString)
{

    initialWordcount = countWords(initialTextString);
    currentWordcount = initialWordcount;
    addedWordcount = getAddedWordcount();

}

void Text::updateWordcountInfo(QString currentTextString) {

    currentWordcount = countWords(currentTextString);
    addedWordcount = getAddedWordcount();
}

int Text::countWords(QString textString) {
    // """Counts words using same method as linux wc"""

    QStringList words = textString.split(QRegularExpression("\\s+"),
                                         Qt::SkipEmptyParts);
    int wc = words.length();

    return wc;
}

int Text::getAddedWordcount() {
    return currentWordcount - initialWordcount;
}