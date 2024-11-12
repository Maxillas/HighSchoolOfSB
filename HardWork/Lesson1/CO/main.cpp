//Исходный код
void MobiventTest::validateSensorTest (Service_t::OPER_MODE typeOfTest, ushort timeOfTest)
{
    using enum ContourTestsErrors;

    switch (typeOfTest) {
    case Service_t::OPER_MODE::USER_TEST_FLOW_SENSORS: {

        if(timeOfTest > m_timeout) {
            m_result[to<int>(Tests::FLOW_TEST)] = false;
            m_resultErrorText[to<int>(Tests::FLOW_TEST)] = m_testsErMap[to<int>(TIMEOUT)].data();
        }

        else if(m_service.FlowMetersSpread > MAX_FLOW_METER_SPREAD) {
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
          m_result[to<int>(Tests::PRESSURE_TEST_LEAK)] = true;
          m_result[to<int>(Tests::PRESSURE_TEST_P)] = true;
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

Способы:
1. Полиморфизм подтипов
2. Избавление от вложенных if
3. Избавление от else



