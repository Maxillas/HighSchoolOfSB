## Модульные противоречия

1. Ситуации, когда связи между модулями должны быть публичными существуют, например если это взаимодействие через какое-то внешнее api или нам может понадобиться отследить выходные данных каждого из модулей (например каждый модуль = устройство и нужно убедиться, что проблема не в железе)
2. Связность модулей - насколько методы класса используют одни и те же поля. Размер модуля в строках кода.
3. Связность модулей была равна 2 - у каждого модуля было по 2 публичных метода, связанных с другим модулем, то есть была связь с другими модулями. Размер модуля был около 200-300 строк кода.
