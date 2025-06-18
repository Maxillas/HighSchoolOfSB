#ifndef ERRORSHISTORY_H
#define ERRORSHISTORY_H
#include "error.h"

class ErrorHistory {
public:
    void add(const std::shared_ptr<IError>& error);

    const std::list<std::shared_ptr<IError>>& all() const;

    void clear();

private:
    std::list<std::shared_ptr<IError>> m_errors;
    static const size_t MAX_HISTORY_SIZE = 100;
};


#endif // ERRORSHISTORY_H
