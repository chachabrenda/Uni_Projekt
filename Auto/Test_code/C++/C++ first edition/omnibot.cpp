#include "MotorModule.h"
#include "LaneModule.h"
#include "WebcamModule.h"

// int main() {
//     Motor motor(10, 9, 11, 17, 22, 27);

//     cv::Mat img = WebcamModule::getImg();
//     double curveVal = getLaneCurve(img, 1);

//     double sen = 1.3;  // SENSITIVITY
//     double maxVal = 0.3; // MAX SPEED
//     if (curveVal > maxVal)
//         curveVal = maxVal;
//     if (curveVal < -maxVal)
//         curveVal = -maxVal;

//     if (curveVal > 0) {
//         sen = 1.7;
//         if (curveVal < 0.05)
//             curveVal = 0;
//     } else {
//         if (curveVal > -0.08)
//             curveVal = 0;
//     }

//     motor.move(0.20, -curveVal * sen, 0.05);

//     return 0;
// }