#include "MotorModule.h"
#include "LaneModule.h"
#include "WebcamModule.h"

int main() {
    // Initialisiere die Motorsteuerung mit den entsprechenden Pins
    Motor motor(10, 9, 11, 17, 22, 27);

    // Erfasse ein Bild von der Webcam
    cv::Mat img = WebcamModule::getImg();

    // Berechne die Kurvenbewertung für die Fahrspurerkennung
    double curveVal = getLaneCurve(img, 1);

    // Empfindlichkeit und maximale Geschwindigkeit einstellen
    double sen = 1.3;  // Empfindlichkeit
    double maxVal = 0.3; // Maximale Geschwindigkeit

    // Beschränke die Kurvenbewertung auf die maximale Geschwindigkeit
    if (curveVal > maxVal)
        curveVal = maxVal;
    if (curveVal < -maxVal)
        curveVal = -maxVal;

    // Feine Anpassungen der Empfindlichkeit je nach Kurvenbewertung vornehmen
    if (curveVal > 0) {
        sen = 1.7;
        if (curveVal < 0.05)
            curveVal = 0;
    } else {
        if (curveVal > -0.08)
            curveVal = 0;
    }

    // Motor mit Geschwindigkeit und Kurvenbewertung steuern
    motor.move(0.20, -curveVal * sen, 0.05);

    return 0;
}

