#!/usr/bin/env python3

import wpilib

class Onyx(wpilib.IterativeRobot):
    '''Main robot class'''
    
    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        self.motor=wpilib.Victor(1)
        self.motor2=wpilib.Victor(2)
        self.motor3=wpilib.Victor(3)
        self.motor4 = wpilib.Victor(4)
        self.state="Drive"
        self.timer=wpilib.Timer()
        self.drive=wpilib.RobotDrive

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        self.timer.start()

    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''
        if self.state == "Drive":
            self.motor.set(1)
            self.motor2.set(1)
            if self.timer.get()>2:
                self.state="LTurn"
        elif self.state == "LTurn":
            self.motor.set(0)
            if self.timer.get()>5.1:
                self.state="Drive2"
        elif self.state == "Drive2":
            self.motor.set(1)
            self.motor2.set(1)
            if self.timer.get()>7.1:
                self.state="RTurn"
        elif self.state == "RTurn":
            self.motor2.set(0)
            if self.timer.get()>10.2:
                self.state="Drive3"
        elif self.state == "Drive3":
            self.motor2.set(1)
            if self.timer.get()>12.2:
                self.state="Stop"
        elif self.state == "Stop":
            self.motor.set(0)
            self.motor2.set(0)


    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass
    
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        pass

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''
        pass
        

if __name__ == '__main__':
    wpilib.run(Onyx)

