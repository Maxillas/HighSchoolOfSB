#ifndef TASKMANAGER_H
#define TASKMANAGER_H
#include <vector>
#include <cstdint>
#include <string>

class TaskManager {

public:
    void addTask(const std::string& name, int priority, const std::string& deadline);
    void removeTask(const std::string& name);
    void markTaskCompleted(const std::string& name);
    std::vector<std::string> filterByStatus(bool completed) const;
    void sortByField(const std::string& field); // "priority", "deadline", etc.
    void printAllTasks() const;

private:

    struct Task {
        std::string taskName;
        uint8_t priority;
        bool status;
        std::string deadLine;
    };

    std::vector<Task> m_tasks;



};

#endif // TASKMANAGER_H
