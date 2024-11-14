// Метод №1. Исходная реализация
void MobiventTest::validateSensorTest (Service_t::OPER_MODE typeOfTest, ushort timeOfTest)
{
    using enum ContourTestsErrors;

    switch (typeOfTest) {
    case Service_t::OPER_MODE::USER_TEST_FLOW_SENSORS: {

        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::FLOW_TEST)] = false;
            m_resultErrorText[to<int>(Tests::FLOW_TEST)] = m_testsErMap[to<int>(TIMEOUT)].data();
        } else if (m_service.FlowMetersSpread > MAX_FLOW_METER_SPREAD) {
            m_result[to<int>(Tests::FLOW_TEST)] = false;
            m_resultErrorText[to<int>(Tests::FLOW_TEST)] = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        } else {
            m_result[to<int>(Tests::FLOW_TEST)] = true;
        }

        break;
    }

    case Service_t::OPER_MODE::USER_TEST_PRESS_SENSORS: {
        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::PRESSURE_TEST_P)] = false;
            m_result[to<int>(Tests::PRESSURE_TEST_LEAK)] = false;
            m_resultErrorText[to<int>(Tests::PRESSURE_TEST_P)] = m_testsErMap[to<int>(TIMEOUT)].data();
            m_resultErrorText[to<int>(Tests::PRESSURE_TEST_LEAK)] = "";
        } else if(m_service.PressureMetersSpread > MAX_PRESSURE_METER_SPREAD) {
            m_result[to<int>(Tests::PRESSURE_TEST_P)] = false;
            m_resultErrorText[to<int>(Tests::PRESSURE_TEST_P)] = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        } else if(m_service.CalculatedLeakMlMin > MAX_LEAK) {
            m_result[to<int>(Tests::PRESSURE_TEST_LEAK)] = false;
            m_resultErrorText[to<int>(Tests::PRESSURE_TEST_LEAK)] = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        } else {
            m_result[to<int>(Tests::PRESSURE_TEST_P)] = true;
            m_result[to<int>(Tests::PRESSURE_TEST_LEAK)] = true;
        }
        break;
    }

    case Service_t::OPER_MODE::USER_TEST_CONT_COMPL: {
        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::COMPLINCE_TEST)] = false;
            m_resultErrorText[to<int>(Tests::COMPLINCE_TEST)] = m_testsErMap[to<int>(TIMEOUT)].data();
        } else if(static_cast<float>(m_service.Cmpl) / 100 < MIN_COMPLINCE) {
            m_result[to<int>(Tests::COMPLINCE_TEST)] = false;
            m_resultErrorText[to<int>(Tests::COMPLINCE_TEST)] = m_testsErMap[to<int>(TO_LOW_VALUE)].data();
        } else {
            m_result[to<int>(Tests::COMPLINCE_TEST)] = true;
        }
        break;
    }

    case Service_t::OPER_MODE::USER_TEST_CONT_INSP_RES: {
        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::INSP_RES_TEST)] = false;
            m_resultErrorText[to<int>(Tests::INSP_RES_TEST)] = m_testsErMap[to<int>(TIMEOUT)].data();
        } else if(m_service.Rinsp > MAX_RINSP) {
            m_result[to<int>(Tests::INSP_RES_TEST)] = false;
            m_resultErrorText[to<int>(Tests::INSP_RES_TEST)] = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        } else {
            m_result[to<int>(Tests::INSP_RES_TEST)] = true;
        }
        break;
    }

    case Service_t::OPER_MODE::USER_TEST_CONT_EXP_RES: {
        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::EXP_RES_TEST)] = false;
            m_resultErrorText[to<int>(Tests::EXP_RES_TEST)] = m_testsErMap[to<int>(TIMEOUT)].data();
        } else if(m_service.Rexp > MAX_REXP) {
            m_result[to<int>(Tests::EXP_RES_TEST)] = false;
            m_resultErrorText[to<int>(Tests::EXP_RES_TEST)] = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        } else {
            m_result[to<int>(Tests::EXP_RES_TEST)] = true;
        }
        break;
    }

    default:
        qDebug() << "неопределённое поведение";
    }
}

// Результат доработки
// Был создал абстрактный класс TestObject и от него наследуются другие тесты,
// вместо нахождения их в одном методе
// У каждого класса сделан свой метод checkResult, в котором
// осуществляется проверка валидности результатов
// Привожу только частичную реализацию, т.к. полная довольно объемная
class TestObject : public QObject {
    virtual void checkResult() = 0;
};

class TestFlow: public TestObject {
    void checkResult() override;
};

class TestComplince: public TestObject {
    void checkResult() override;
};

class TestSensors: public TestObject {
    void checkResult() override;
};

class TestExpResistance : public TestObject {
    void checkResult() override;
};

class TestInspResistance : public TestObject {
    void checkResult() override;
};

//пример метода checkResult (у каждого класса он свой)
void TestFlow::checkResult(ushort timeOfTest)
{
    using enum ContourTestsErrors;

    setResultValue(m_service.FlowMetersSpread);

    if(timeOfTest > m_timeout) {
        m_result  = false;
        m_resultErrorText = m_testsErMap[to<int>(TIMEOUT)].data();
        return;
    }

    if(m_service.FlowMetersSpread > MAX_FLOW_METER_SPREAD) {
        m_result  = false;
        m_resultErrorText = m_testsErMap[to<int>(TO_HIGHT_VALUE)].data();
        return;
    }

    m_result = true;
}

//Были использованы:
//1. Полиморфизм подтипов
//2. Избавление от else
//3. Избавление от switch
// Исходная цикломатическая сложность = 18 (3+4+3+3+3(кол-во if) + 1 + 1)
// Конечная цикломатическая сложность отдельного метода = 3


// Метод №2. Исходная реализация
QStringList SoftwareUpdate::fileNameList()
{
    QDir dir;
    if(ptr_screenshot != nullptr) {
        dir = ptr_screenshot->getCurrentStorage();
    } else {
        qDebug () << "[SoftwareUpdate::fileNameList]  Ошибка алгоритма: ptr_screenshot = nullptr";
        return m_fileNameList;
    }

    if (dir.exists())
    {
        dir.setFilter(QDir::Files | QDir::NoDotAndDotDot | QDir::NoSymLinks);
        dir.setSorting(QDir::Time | QDir::Reversed);

        QString keyWord;
        if (shouldUpdateContrBoard()) {
            keyWord = "Mob_ctrl";
        } else if (shouldUpdateSupplyBoard()) {
            keyWord = "Mob_pwrb";
        } else if (shouldUpdateMonitBoard()) {
            keyWord = "Mob_monb";
        } else if (shouldUpdateTurbDriver()) {
            keyWord = "Mob_turb";
        }

        QStringList allBinFiles =
            dir.entryList(QStringList() << "*.bin", QDir::Files);

        QStringList newFileNameList;
        for (const QString &fileName : allBinFiles) {
            if (fileName.contains(keyWord, Qt::CaseInsensitive)) {
                newFileNameList << fileName;
            }
        }

        for (int i = 0; i < newFileNameList.count(); ++i)
        {
            newFileNameList[i].replace(".bin", "");
        }

        if (m_fileNameList != newFileNameList)
        {
            m_fileNameList = newFileNameList;
            if (m_isFileNameListInitialized) {
                emit fileNameListChanged(m_fileNameList);
            }
        }
    }

    m_isFileNameListInitialized = true;
    return m_fileNameList;
}

//Результат доработки

QStringList SoftwareUpdate::fileNameList()
{
    QDir dir;
    dir = screenshot.getCurrentStorage();
    // заменил Screenshot* ptr_screenshot на Screenshot m_sctreenshot (теперь хранится по значению)

    if (!dir.exists()) {return m_fileNameList;}

    dir.setFilter(QDir::Files | QDir::NoDotAndDotDot | QDir::NoSymLinks);
    dir.setSorting(QDir::Time | QDir::Reversed);

    QString keyWord = keywordDefinition();
    QStringList allBinFiles = dir.entryList(QStringList() << "*.bin", QDir::Files);
    QStringList newFileNameList = allBinFiles.filter(keyWord);
    newFileNameList.replaceInStrings(".bin", "");
    setFileNameList(newFileNameList);

    m_isFileNameListInitialized = true;
    return m_fileNameList;
}

QString keywordDefinition() {
    if (shouldUpdateContrBoard()) {
        return "Mob_ctrl";
    }
    if (shouldUpdateSupplyBoard()) {
        return "Mob_pwrb";
    }
    if (shouldUpdateMonitBoard()) {
        return "Mob_monb";
    }
    if (shouldUpdateTurbDriver()) {
        return "Mob_turb";
    }
}

void setFileNameList(const QStringList& newName) {
    if (m_fileNameList == newName) {
        return;
    }
    m_fileNameList = newName;
    if (m_isFileNameListInitialized) {
        emit fileNameListChanged(m_fileNameList);
    }
}

//1. Избавление от nullptr
//2. Исключил for там где он не нужен
//3. Вынос инструкций в отдельную функцию
//4. Исключил вложенные if
// Исходная цикломатическая сложность = 26 (11(кол-во if) + 15 (for))
// Конечная цикломатическая сложность отдельного метода = 1


// Метод №3. Исходная реализация
bool SoftwareUpdate::isBoardVersionEqualToFilename(QString &error_notice)
{
    bool result = true;

    QString recieved_version;
    InfoSettings &l_info_set = *Mobivent::settings().info();

    if (shouldUpdateContrBoard()) {
        recieved_version = l_info_set.controlBoardSoftwareVersion();
    } else if (shouldUpdateSupplyBoard()) {
        recieved_version = l_info_set.powerBoardSoftwareVersion();
    } else if (shouldUpdateMonitBoard()) {
        recieved_version = l_info_set.monitorBoardSoftwareVersion();
    } else if (shouldUpdateTurbDriver()) {
        recieved_version = l_info_set.turbineDriverSoftwareVersion();
    }

    if (recieved_version.isEmpty()) {
        error_notice = "Сообщение с версией платы не получено.";
        return false;
    }
    QString versionFromFile;
    QString fileName = m_destination_file_info.fileName();

    int firstUnderscoreIndex = fileName.indexOf("_");
    int secondUnderscoreIndex = fileName.indexOf("_", firstUnderscoreIndex + 1);

    if (secondUnderscoreIndex != -1) {
        versionFromFile = fileName.mid(secondUnderscoreIndex + 1);

        if (versionFromFile.endsWith(".bin")) {
            versionFromFile.replace(".bin", "");
        }

        result = recieved_version.endsWith(versionFromFile);
        if (!result) {
            error_notice =
                "Внимание: обновление ...";
            return false;
        }
    } else {
        error_notice =
            "Внимание: обновление прошивки платы ...";
        return false;
    }

    return result;
}

// Результат доработки
bool SoftwareUpdate::isBoardVersionEqualToFilename(QString &error_notice)
{

    InfoSettings &l_info_set = *Mobivent::settings().info();
    QString recieved_version = recievedVersionDefinition();

    if (recieved_version.isEmpty()) {
        error_notice = "Сообщение с версией платы не получено.";
        return false;
    }
    QString versionFromFile;
    QString fileName = m_destination_file_info.fileName();

    int firstUnderscoreIndex = fileName.indexOf("_");
    int secondUnderscoreIndex = fileName.indexOf("_", firstUnderscoreIndex + 1);

    if(secondUnderscoreIndex == -1) {
        error_notice = "Внимание: обновление прошивки платы ...";
        return false;
    }

    versionFromFile = fileName.mid(secondUnderscoreIndex + 1);

    if (versionFromFile.endsWith(".bin")) {
        versionFromFile.replace(".bin", "");
    }

    if(!recieved_version.endsWith(versionFromFile)) {
        error_notice = "Внимание: обновление ...";
        return false;
    }

    return true;
}


QString recievedVersionDefinition() {
    if (shouldUpdateContrBoard()) {
        return l_info_set.controlBoardSoftwareVersion();
    }
    if (shouldUpdateSupplyBoard()) {
        return l_info_set.powerBoardSoftwareVersion();
    }
    if (shouldUpdateMonitBoard()) {
        return l_info_set.monitorBoardSoftwareVersion();
    }
    if (shouldUpdateTurbDriver()) {
        return l_info_set.turbineDriverSoftwareVersion();
    }
}


//1. Вынос инструкций в отдельную функцию
//2. Избавление от else
//3. Избавление от вложенных условий
// Исходная цикломатическая сложность = 9 (кол-во if)
// Конечная цикломатическая сложность отдельного метода = 4
