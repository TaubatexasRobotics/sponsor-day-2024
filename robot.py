import wpilib
import wpilib.drive
import phoenix5 
from pieceSys import ShooterSys

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
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
        self.shooter = ShooterSys()
        self.shooter.shooterInit()

    def teleopPeriodic(self):
        move_value = self.joystick.getRawAxis(0)
        rotate_value = self.joystick.getRawAxis(1)

        self.robot_drive.arcadeDrive(move_value, rotate_value)

        self.shooter.shooterPeriodic()


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass 

#if _name_ == "_main_":
#    wpilib.run(TestRobot)