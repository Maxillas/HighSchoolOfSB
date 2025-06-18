#ifndef USER_H
#define USER_H

#include "../Statistics/statistic.h"
#include "../Errors/errorshistory.h"
#include "../Errors/error.h"
#include <string>
#include <memory>

class IUser {
public:
    virtual ~IUser() = default;

    virtual std::string name() const = 0;
    virtual const Statistic& statistics() const = 0;
    virtual const ErrorHistory& errorsHistory() const = 0;
    virtual void setName(const std::string& name) = 0;
};

class User : public IUser {
public:
    User(const std::string& name);

    std::string name() const override;

    const Statistic& statistics() const override;

    const ErrorHistory& errorsHistory() const override;

    void setName(const std::string& name) override;

    void addError(const std::shared_ptr<IError>& error);

    void updateStatistics(const Step& step, int score);

private:
    std::string m_name;
    Statistic m_statistics;
    ErrorHistory m_errorHistory;
};

#endif // USER_H
