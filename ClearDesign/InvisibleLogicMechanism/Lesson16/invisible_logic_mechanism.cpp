
class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {

    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound();
    }
}
// Ответ: Не знаю, как в java, но в С++ ключевое слово override носит рекомендательный
// характер и только лишь наглядно показывает, что метод был переопределен, 
// и его исключение сути не изменит - в итоге будет вызван переопределенный метод makeSound.
// Думаю, что в java будет вызываться метод базового класса без override и метод класса 
// cat с override
