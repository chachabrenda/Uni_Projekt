#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <unistd.h>

// Define some device parameters
#define I2C_ADDR 0x27 // I2C device address
#define LCD_WIDTH 16   // Maximum characters per line

// Define some device constants
#define LCD_CHR 1 // Mode - Sending data
#define LCD_CMD 0 // Mode - Sending command

#define LCD_LINE_1 0x80 // LCD RAM address for the 1st line
#define LCD_LINE_2 0xC0 // LCD RAM address for the 2nd line
#define LCD_LINE_3 0x94 // LCD RAM address for the 3rd line
#define LCD_LINE_4 0xD4 // LCD RAM address for the 4th line

#define LCD_BACKLIGHT  0x08  // On
//#define LCD_BACKLIGHT 0x00  // Off

#define ENABLE 0b00000100 // Enable bit

// Timing constants
#define E_PULSE 0.0005
#define E_DELAY 0.0005

int fd; // file descriptor for I2C

void lcd_byte(int bits, int mode);
void lcd_toggle_enable(int bits);
void lcd_init();
void lcd_string(char* message, int line);

int main(){
    // setup WiringPi library
    wiringPiSetup();
    
    // Initialize I2C
    fd = wiringPiI2CSetup(I2C_ADDR);

    // Initialize LCD
    lcd_init();

    // Show text on LCD
    lcd_string("Bakir", LCD_LINE_1);
    lcd_string("Charnel", LCD_LINE_2);
    lcd_string("Mohammed", LCD_LINE_3);
    lcd_string("Amr", LCD_LINE_4);

    return 0;
}

void lcd_byte(int bits, int mode) {
    // Send byte to data pins
    // bits = the data
    // mode = 1 for data
    //        0 for command

    int bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT;
    int bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT;

    // High bits
    wiringPiI2CWrite(fd, bits_high);
    lcd_toggle_enable(bits_high);

    // Low bits
    wiringPiI2CWrite(fd, bits_low);
    lcd_toggle_enable(bits_low);
}

void lcd_toggle_enable(int bits) {
    // Toggle enable
    usleep(E_DELAY*1000000);
    wiringPiI2CWrite(fd, (bits | ENABLE));
    usleep(E_PULSE*1000000);
    wiringPiI2CWrite(fd, (bits & ~ENABLE));
    usleep(E_DELAY*1000000);
}

void lcd_init() {
    // Initialise display
    lcd_byte(0x33,LCD_CMD); // 110011 Initialise
    lcd_byte(0x32,LCD_CMD); // 110010 Initialise
    lcd_byte(0x06,LCD_CMD); // 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD); // 001100 Display On,Cursor Off, Blink Off 
    lcd_byte(0x28,LCD_CMD); // 101
    lcd_byte(0x01,LCD_CMD); // Clear display
    usleep(E_DELAY*2000);
}

void lcd_string(char* message, int line) {
    // Send string to LCD
    
    lcd_byte(line, LCD_CMD);

    int i;
    for(i=0; message[i]!='\0'; i++)
        lcd_byte(message[i], LCD_CHR);
}
