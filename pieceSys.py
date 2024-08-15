import wpilib
import wpilib.drive
import phoenix5 
import rev

class ShooterSys():
    def shooterInit(self):
        self.controle = wpilib.Joystick(0)

        self.shooter = phoenix5.WPI_VictorSPX(5)
        self.intake = rev.CANSparkMax(54, rev.CANSparkMax.MotorType.kBrushless)
        self.threadmill = phoenix5.WPI_VictorSPX(1)
        ()

    def shooterPeriodic(self):
        self.intake_value = self.controle.getRawAxis(5) # Moves the intake
        self.intake.set(self.intake_value)

        if self.controle.getRawButton(2) == True:
            self.threadmill.set(1.0)
        else:
            self.threadmill.set(0)
        
        if self.controle.getRawButton(3) == True:
            self.shooter.set(1.0)
        else:
            self.shooter.set(0)

