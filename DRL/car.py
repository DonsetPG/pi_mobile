import brickpi3 # import the BrickPi3 drivers
import sys
"""
action_to_steer = {
    0: _reset_steer,
    1:_steer_right,
    2:_steer_left
}

action_to_speed = {
    0: _fast_forward,
    1:_slow_forward,
}
"""
class Car:

    def __init__(self):
        self.bp = brickpi3.BrickPi3() 
        self.PORT_MOTOR_LEFT    = self.bp.PORT_A # specify the motor ports
        self.PORT_MOTOR_RIGHT   = self.bp.PORT_D
        self.PORT_STEER         = self.bp.PORT_B 

        self.bp.reset_all()
        self.bp.offset_motor_encoder(self.PORT_MOTOR_LEFT, self.bp.get_motor_encoder(self.PORT_MOTOR_LEFT))
        self.bp.offset_motor_encoder(self.PORT_MOTOR_RIGHT, self.bp.get_motor_encoder(self.PORT_MOTOR_RIGHT))
        self.bp.offset_motor_encoder(self.PORT_MOTOR_STEER, self.bp.get_motor_encoder(self.PORT_MOTOR_STEER))

    def _safe_exit(self):
        self.bp.reset_all()
        sys.exit()

    def _steer_left(self):
        self.bp.set_motor_position(self.PORT_STEER,-70)

    def _steer_right(self):
        self.bp.set_motor_position(self.PORT_STEER,70)
    
    def _reset_steer(self):
        self.bp.set_motor_positiob(self.PORT_STEER,1)

    def _fast_forward(self):
        self.bp.set_motor_power(self.PORT_MOTOR_LEFT,250)
        self.bp.set_motor_power(self.PORT_MOTOR_RIGHT,250)

    def _slow_forward(self):
        self.bp.set_motor_power(self.PORT_MOTOR_LEFT,50)
        self.bp.set_motor_power(self.PORT_MOTOR_RIGHT,50)

    def _stop_car(self):
        self.bp.set_motor_power(self.PORT_MOTOR_LEFT,0)
        self.bp.set_motor_power(self.PORT_MOTOR_RIGHT,0)
