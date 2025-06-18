# Инструкция по сборке и запуску игры "Три в ряд"

## 📋 Технические требования

### Минимальные
- **ОС**: Windows 10 (x64), Linux (Ubuntu 20.04+), macOS 10.15+
- **Компилятор**: GCC 9+/Clang 12+/MSVC 2019 (поддержка C++17)
- **Память**: 512 МБ RAM
- **Дисковое пространство**: 50 МБ

### Рекомендуемые
- **ОС**: Windows 11/Ubuntu 22.04 LTS/macOS 12+
- **Компилятор**: GCC 11+/Clang 14+/MSVC 2022+
- **Память**: 1 ГБ RAM

## 📦 Зависимости

### Обязательные
- Компилятор с поддержкой C++17
- CMake 3.12+

### Опциональные
- Doxygen (для документации)
- Git (для клонирования)

## 🛠 Сборка проекта

### Linux/macOS
```bash
# 1. Клонировать репозиторий
git clone https://github.com/your-repo/three-in-a-row.git
cd three-in-a-row

# 2. Создать папку сборки
mkdir build && cd build

# 3. Собрать проект
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

# 4. Запустить игру
./three_in_a_row
