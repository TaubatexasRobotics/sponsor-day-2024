import wpilib
import wpilib.drive
from pieceSys import ShooterSys
from drivetrainSys import Drivetrain

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        
        self.drivetrain = Drivetrain()
        self.drivetrain.drivetrainInit()

        self.shooter = ShooterSys()
        self.shooter.shooterInit()

    def teleopPeriodic(self):

        self.drivetrain.TeleopPeriodic()
        
        self.shooter.shooterPeriodic()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass 

#if _name_ == "_main_":
#    wpilib.run(TestRobot)