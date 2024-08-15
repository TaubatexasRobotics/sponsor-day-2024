import wpilib
import phoenix5
import wpilib.drive 

class Drivetrain():
    def drivetrainInit(self):
        self.left_front = phoenix5.WPI_VictorSPX(12) 
        self.left_back = phoenix5.WPI_VictorSPX(4)  
        self.right_front = phoenix5.WPI_VictorSPX(3) 
        self.right_back = phoenix5.WPI_VictorSPX(2) 

        self.left = wpilib.MotorControllerGroup(self.left_front, self.left_back)
        self.right = wpilib.MotorControllerGroup(self.right_front, self.right_back)

        self.robot_drive = wpilib.drive.DifferentialDrive(
            self.left, self.right
        )

        self.joystick = wpilib.Joystick(0)


    def TeleopPeriodic(self):
        move_value = self.joystick.getRawAxis(0)
        rotate_value = self.joystick.getRawAxis(1)

        self.robot_drive.arcadeDrive(move_value, rotate_value)