#include <wiringPi.h>
#include <softPwm.h>
#include <unistd.h>

class Motor {
private:
    int EnaA, In1A, In2A, EnaB, In1B, In2B;

public:
    Motor(int EnaA, int In1A, int In2A, int EnaB, int In1B, int In2B) {
        this->EnaA = EnaA;
        this->In1A = In1A;
        this->In2A = In2A;
        this->EnaB = EnaB;
        this->In1B = In1B;
        this->In2B = In2B;

        pinMode(this->EnaA, OUTPUT);
        pinMode(this->In1A, OUTPUT);
        pinMode(this->In2A, OUTPUT);
        pinMode(this->EnaB, OUTPUT);
        pinMode(this->In1B, OUTPUT);
        pinMode(this->In2B, OUTPUT);

        softPwmCreate(this->EnaA, 0, 100);
        softPwmCreate(this->EnaB, 0, 100);
    }

    void move(double speed = 0.5, double turn = 0, int t = 0) {
        int pwmSpeed = static_cast<int>(speed * 100);
        int pwmTurn = static_cast<int>(turn * 70);
        int leftSpeed = pwmSpeed - pwmTurn;
        int rightSpeed = pwmSpeed + pwmTurn;

        if (leftSpeed > 100)
            leftSpeed = 100;
        else if (leftSpeed < -100)
            leftSpeed = -100;
        if (rightSpeed > 100)
            rightSpeed = 100;
        else if (rightSpeed < -100)
            rightSpeed = -100;

        softPwmWrite(this->EnaA, abs(leftSpeed));
        softPwmWrite(this->EnaB, abs(rightSpeed));

        if (leftSpeed > 0) {
            digitalWrite(this->In1A, HIGH);
            digitalWrite(this->In2A, LOW);
        } else {
            digitalWrite(this->In1A, LOW);
            digitalWrite(this->In2A, HIGH);
        }

        if (rightSpeed > 0) {
            digitalWrite(this->In1B, HIGH);
            digitalWrite(this->In2B, LOW);
        } else {
            digitalWrite(this->In1B, LOW);
            digitalWrite(this->In2B, HIGH);
        }

        sleep(t);
    }

    void stop(int t = 0) {
        softPwmWrite(this->EnaA, 0);
        softPwmWrite(this->EnaB, 0);
        sleep(t);
    }
};

// int main() {
//     wiringPiSetup();

//     Motor motor(10, 9, 11, 17, 22, 27);

//     motor.move(0.5, 0, 2);
//     motor.stop(2);
//     motor.move(-0.5, 0, 2);
//     motor.stop(2);
//     motor.move(0, 0.5, 2);
//     motor.stop(2);
//     motor.move(0, -0.5, 2);
//     motor.stop(2);

//     return 0;
// }