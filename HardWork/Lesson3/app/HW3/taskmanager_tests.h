#ifndef TASKMANAGER_TESTS_H
#define TASKMANAGER_TESTS_H

#include <iostream>
#include "taskmanager.h"

class TaskManagerTests {
public:
    void test_addTask() {
        m_taskManager.addTask("clean room", 1, "18.06.2024");
        auto task1 = m_taskManager.m_tasks.at(0);
        bool firstTest = task1.taskName == "clean room" &&
                         task1.priority == 1 &&
                         task1.status == false &&
                         task1.deadLine == "18.06.2024" &&
                         m_taskManager.m_tasks.size() == 1;

        m_taskManager.addTask("run", 2, "20.06.2024");
        auto task2 = m_taskManager.m_tasks.at(0);
        bool secondTest = task2.taskName == "run" &&
                          task2.priority == 2 &&
                          task2.status == false &&
                          task2.deadLine == "20.06.2024" &&
                          m_taskManager.m_tasks.size() == 2;

        std::cout << "_add_ Test1 is " << (firstTest ? "passed" : "error") << std::endl;
        std::cout << "_add_ Test2 is " << (secondTest ? "passed" : "error") << std::endl;

        m_taskManager.m_tasks.clear();
    };

    void test_removeTask() {
        m_taskManager.addTask("clean room", 1, "18.06.2024");
        m_taskManager.addTask("run", 2, "20.06.2024");
        m_taskManager.addTask("cleans room", 1, "18.06.2024");
        m_taskManager.addTask("cleanser room", 1, "18.06.2024");

        m_taskManager.removeTask("run");
        bool test1 = m_taskManager.m_tasks.size() == 3 &&
                     m_taskManager.m_tasks.at(1).taskName == "cleans room";

        m_taskManager.removeTask("clean room");
        bool test2 = m_taskManager.m_tasks.size() == 2 &&
                     m_taskManager.m_tasks.at(0).taskName == "cleanser room";

        m_taskManager.removeTask("error!");
        bool test3 = m_taskManager.m_tasks.size() == 2 &&
                     m_taskManager.m_tasks.at(0).taskName == "cleanser room";

        m_taskManager.removeTask("cleans room");
        bool test4 = m_taskManager.m_tasks.size() == 1 &&
                     m_taskManager.m_tasks.at(0).taskName == "cleanser room";

        m_taskManager.removeTask("cleanser room");
        bool test5 = m_taskManager.m_tasks.size() == 0;

        m_taskManager.removeTask("empty");
        bool test6 = m_taskManager.m_tasks.size() == 0;

        std::cout << "_remove_ Test1 is " << (test1 ? "passed" : "error") << std::endl;
        std::cout << "_remove_ Test2 is " << (test2 ? "passed" : "error") << std::endl;
        std::cout << "_remove_ Test3 is " << (test3 ? "passed" : "error") << std::endl;
        std::cout << "_remove_ Test4 is " << (test4 ? "passed" : "error") << std::endl;
        std::cout << "_remove_ Test5 is " << (test5 ? "passed" : "error") << std::endl;
        std::cout << "_remove_ Test6 is " << (test6 ? "passed" : "error") << std::endl;

        m_taskManager.m_tasks.clear();
    };

    void test_markTaskCompleted() {
        m_taskManager.addTask("first task", 1, "18.06.2024");
        m_taskManager.addTask("second task", 2, "20.06.2024");
        m_taskManager.addTask("third task", 1, "18.06.2024");
        bool result = m_taskManager.m_tasks.at(0).status == false &&
                     m_taskManager.m_tasks.at(1).status == false &&
                     m_taskManager.m_tasks.at(2).status == false;

        m_taskManager.markTaskCompleted("first task");
        bool test1 = result && (m_taskManager.m_tasks.at(0).status == false) &&
                               (m_taskManager.m_tasks.at(1).status == false) &&
                               (m_taskManager.m_tasks.at(2).status == true);

        m_taskManager.markTaskCompleted("second task");
        bool test2 = result && (m_taskManager.m_tasks.at(1).status == true) &&
                               (m_taskManager.m_tasks.at(0).status == false) &&
                               (m_taskManager.m_tasks.at(2).status == true);

        m_taskManager.markTaskCompleted("third task");
        bool test3 = result && (m_taskManager.m_tasks.at(2).status == true) &&
                               (m_taskManager.m_tasks.at(1).status == true) &&
                               (m_taskManager.m_tasks.at(0).status == true);

        std::cout << "_markTaskCompleted_ Test1 is " << (test1 ? "passed" : "error") << std::endl;
        std::cout << "_markTaskCompleted_ Test2 is " << (test2 ? "passed" : "error") << std::endl;
        std::cout << "_markTaskCompleted_ Test3 is " << (test3 ? "passed" : "error") << std::endl;

        m_taskManager.m_tasks.clear();
    };

    void test_filterByStatus() {
        // удаляем задачи со статусом выполнено
        m_taskManager.addTask("first task", 1, "18.06.2024");
        m_taskManager.addTask("second task", 2, "20.06.2024");
        m_taskManager.addTask("third task", 1, "18.06.2024");

        m_taskManager.markTaskCompleted("first task");
        std::vector<std::string> firstRes = m_taskManager.filterByStatus(true);
        bool test1 = firstRes.size() == 1 && m_taskManager.m_tasks.size() == 3 &&
                     firstRes.at(0) == "first task";

        m_taskManager.markTaskCompleted("second task");
        std::vector<std::string> secondRes = m_taskManager.filterByStatus(true);
        bool test2 = secondRes.size() == 2 && m_taskManager.m_tasks.size() == 3 &&
                     secondRes.at(0) == "second task" && secondRes.at(1) == "first task";

        m_taskManager.markTaskCompleted("third task");
        std::vector<std::string> thirdRes = m_taskManager.filterByStatus(true);
        bool test3 = thirdRes.size() == 3 && m_taskManager.m_tasks.size() == 3 &&
                     thirdRes.at(0) == "third task" && thirdRes.at(1) == "second task" &&
                     thirdRes.at(2) == "first task";

        m_taskManager.m_tasks.clear();

        m_taskManager.addTask("first task", 1, "18.06.2024");
        m_taskManager.addTask("second task", 2, "20.06.2024");
        m_taskManager.addTask("third task", 1, "18.06.2024");
        bool temp = m_taskManager.m_tasks.size() == 3;
        std::vector<std::string> fourthRes = m_taskManager.filterByStatus(false);
        bool test4 = temp && (fourthRes.size() == 3 && m_taskManager.m_tasks.size() == 3) &&
                     fourthRes.at(0) == "third task" && fourthRes.at(1) == "second task" &&
                     fourthRes.at(2) == "first task";;

        std::cout << "_filterByStatus_ Test1 is " << (test1 ? "passed" : "error") << std::endl;
        std::cout << "_filterByStatus_ Test2 is " << (test2 ? "passed" : "error") << std::endl;
        std::cout << "_filterByStatus_ Test3 is " << (test3 ? "passed" : "error") << std::endl;
        std::cout << "_filterByStatus_ Test4 is " << (test4 ? "passed" : "error") << std::endl;

        m_taskManager.m_tasks.clear();
    };

    void test_sortByField() {
        std::string field;
        m_taskManager.addTask("d", 2, "18.06.2024");
        m_taskManager.addTask("b", 0, "20.06.2024");
        m_taskManager.addTask("a", 1, "18.06.2024");

        field = "priority";
        m_taskManager.sortByField(field);
        bool test1 = m_taskManager.m_tasks.at(0).taskName == "b" &&
                     m_taskManager.m_tasks.at(1).taskName == "a" &&
                     m_taskManager.m_tasks.at(2).taskName == "d";

        field = "taskName";
        m_taskManager.sortByField(field);
        bool test2 = m_taskManager.m_tasks.at(0).taskName == "a" &&
                     m_taskManager.m_tasks.at(1).taskName == "b" &&
                     m_taskManager.m_tasks.at(2).taskName == "d";

        std::cout << "_sortByField_ Test1 is " << (test1 ? "passed" : "error") << std::endl;
        std::cout << "_sortByField_ Test2 is " << (test2 ? "passed" : "error") << std::endl;
    };



private:
    TaskManager m_taskManager;

};


#endif // TASKMANAGER_TESTS_H
