""""
У цьому прикладі ми маємо клас Engine, який має два методи: start і stop. У нас також є автомобіль класу, який успадковується
від Engine і має метод приводу. Однак клієнт приходить до використання і каже, що хоче мати різні види
автомобілі: з газовим двигуном і з електричним. Газовий двигун повинен мати спосіб заправки і
електричний двигун повинен мати метод заряду. Як ми можемо це реалізувати?
Використовуйте те, що ми навчилися на уроці. Який зв'язок між автомобілем і двигуном? Це "має" чи "є"?
Виходячи з відповіді, перебудуйте код таким чином, щоб ми могли мати різні типи автомобілів з різними типами двигунів.
"""""
class Engine:
    @staticmethod
    def start():
        print("Engine started")

    @staticmethod
    def stop():
        print("Engine stopped")


class Car(Engine):
    @staticmethod
    def drive():
        print("Car is moving")


if __name__ == '__main__':
    my_car = Car()
    my_car.start()
    my_car.drive()
    my_car.stop()   

