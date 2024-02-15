#include <wiringPi.h>
#include <softPwm.h>
#include <unistd.h>

class Motor {
private:
    int EnaA, In1A, In2A, EnaB, In1B, In2B, EnaC, In1C, In2C;

public:
    Motor(int EnaA, int In1A, int In2A, int EnaB, int In1B, int In2B, int EnaC, int In1C, int In2C) {
        this->EnaA = EnaA;
        this->In1A = In1A;
        this->In2A = In2A;
        this->EnaB = EnaB;
        this->In1B = In1B;
        this->In2B = In2B;
        this->EnaC = EnaC;
        this->In1C = In1C;
        this->In2C = In2C;

        pinMode(this->EnaA, OUTPUT);
        pinMode(this->In1A, OUTPUT);
        pinMode(this->In2A, OUTPUT);
        pinMode(this->EnaB, OUTPUT);
        pinMode(this->In1B, OUTPUT);
        pinMode(this->In2B, OUTPUT);
        pinMode(this->EnaC, OUTPUT);
        pinMode(this->In1C, OUTPUT);
        pinMode(this->In2C, OUTPUT);

        softPwmCreate(this->EnaA, 0, 100);
        softPwmCreate(this->EnaB, 0, 100);
        softPwmCreate(this->EnaC, 0, 100);
    }

    void move(double speed = 0.5, double turn = 0, int t = 0) {
        int pwmSpeed = static_cast<int>(speed * 100);
        int pwmTurn = static_cast<int>(turn * 100);

        softPwmWrite(this->EnaA, abs(pwmSpeed));
        softPwmWrite(this->EnaB, abs(pwmSpeed));
        softPwmWrite(this->EnaC, abs(pwmTurn));

        if (pwmSpeed > 0) {
            digitalWrite(this->In1A, HIGH);
            digitalWrite(this->In2A, LOW);
            digitalWrite(this->In1B, LOW);
            digitalWrite(this->In2B, HIGH);
        } else if (pwmSpeed < 0) {
            digitalWrite(this->In1A, LOW);
            digitalWrite(this->In2A, HIGH);
            digitalWrite(this->In1B, HIGH);
            digitalWrite(this->In2B, LOW);
        }

        if (pwmTurn > 0) {
            digitalWrite(this->In1C, HIGH);
            digitalWrite(this->In2C, LOW);
            softPwmWrite(this->EnaA, abs(pwmTurn));
            digitalWrite(this->In1A, HIGH);
            digitalWrite(this->In2A, LOW);
            softPwmWrite(this->EnaB, abs(pwmTurn));
            digitalWrite(this->In1B, HIGH);
            digitalWrite(this->In2B, LOW);
        } else if (pwmTurn < 0) {
            digitalWrite(this->In1C, LOW);
            digitalWrite(this->In2C, HIGH);
            softPwmWrite(this->EnaA, abs(pwmTurn));
            digitalWrite(this->In1A, LOW);
            digitalWrite(this->In2A, HIGH);
            softPwmWrite(this->EnaB, abs(pwmTurn));
            digitalWrite(this->In1B, LOW);
            digitalWrite(this->In2B, HIGH);
        }

        sleep(t);
    }

    void stop(int t = 0) {
        softPwmWrite(this->EnaA, 0);
        softPwmWrite(this->EnaB, 0);
        softPwmWrite(this->EnaC, 0);
        sleep(t);
    }
};

// int main() {
//     wiringPiSetup();

//     Motor motor(10, 9, 11, 17, 22, 27, 14, 15, 18);

//     motor.move(0.4, 0.2, 2);
//     motor.stop(2);
//     motor.move(-0.3, -0.2, 2);
//     motor.stop(2);

//     return 0;
// }