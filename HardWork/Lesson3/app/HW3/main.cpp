#include "taskmanager_tests.h"



int main()
{
    TaskManagerTests test;
    test.test_addTask();
    test.test_removeTask();
    test.test_markTaskCompleted();
    test.test_filterByStatus();
    test.test_sortByField();

    //cout << "Hello World!" << endl;
    return 0;
}
