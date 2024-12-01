#include "taskmanager.h"
#include "algorithm"

void TaskManager::addTask(const std::string &name, uint8_t priority, const std::string &deadline)
{
    Task task;
    task.taskName = name;
    task.priority = priority;
    task.deadLine = deadline;
    task.status = false;

    m_tasks.insert(m_tasks.begin(), task);
}

void TaskManager::removeTask(const std::string &name)
{
    for(auto it = m_tasks.begin(); it < m_tasks.end(); ++it) {
        if((*it).taskName == name) {
            m_tasks.erase(it);
        }
    }
}

void TaskManager::markTaskCompleted(const std::string &name)
{
    for(auto it = m_tasks.begin(); it < m_tasks.end(); ++it) {
        if((*it).taskName == name) {
            it->status = true;
        }
    }
}

std::vector<std::string> TaskManager::filterByStatus(bool completed) const
{
    std::vector<std::string> result;

    for(auto it = m_tasks.begin(); it < m_tasks.end(); ++it) {
        if((*it).status == completed) {
            result.push_back((*it).taskName);
        }
    }
    return result;
}

void TaskManager::sortByField(const std::string &field)
{
    if(field == "priority") {

        std::sort(m_tasks.begin(), m_tasks.end(),
                  [](Task a, Task b){
                        return a.priority < b.priority;
                  }
        );
        return;
    }

    if(field == "taskName") {
        std::sort(m_tasks.begin(), m_tasks.end(),
                  [](Task a, Task b){
                      return a.taskName < b.taskName;
                  }
                  );
        return;
    }
}

