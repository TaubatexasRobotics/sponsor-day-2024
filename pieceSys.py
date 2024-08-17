import wpilib
import wpilib.drive
import phoenix5 
import rev

class ShooterSys():
    def shooterInit(self):
        self.controle = wpilib.Joystick(0)

        self.shooter = phoenix5.WPI_VictorSPX(5)
        self.intake = rev.CANSparkMax(9, rev.CANSparkMax.MotorType.kBrushless)
        self.threadmill = phoenix5.WPI_VictorSPX(1)

    def shooterPeriodic(self):
        if self.controle.getRawButton(4): # Moves the intake
            self.intake.set(0.5)
        elif self.controle.getRawButton(2):
            self.intake.set(-0.2)
        else:
            self.intake.set(0)

        if self.controle.getRawButton(3) == True: # Moves the threadmill
            self.threadmill.set(-1.0)
        else:
            self.threadmill.set(0)

        if self.controle.getRawButton(1) == True: # Fires the shooter
            self.shooter.set(0.5)
        else:
            self.shooter.set(0)