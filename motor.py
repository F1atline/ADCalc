

class async_motor():
    """class of represent the electrical asyncronious motor"""



    def __init__(self, (int)num_pair_pol, phase_volt, frequency, motor_power, \
        velocity, current, efficiency, cosfi, critical_torq, \
        start_torq, start_curr, act_stator_res, act_rotor_res, \
        react_stator_res, react_rotor_res, magnetic_curr):

        """Initialization method"""
        """description of initialization arguments:
            num_pair_pol        - number of pairs of poles electrical machine
            phase_volt          - nominal phase voltage
            frequency           - nominal current frequency
            motor_power         - nominal power of motor
            velocity            - nominal velocity of motor
            current             - nominal current of motor
            efficiency          - nominal efficiency of motor
            cosfi               - nominal cosinus efficiency of motor
            critical_torq       - critical torque of motor
            start_torq          - start up torque of motor
            start_curr          - start up torque of motor
            act_stator_res      - active stator resistance
            act_rotor_res       - active rotor resistance reduced to stator
            react_stator_res    - reactive stator resistance
            react_rotor_res     - reactive rotor resistance reduced to stator
            magnetic_curr       - nominal magnetic current of motor
        """
        self.num_pair_pol        = num_pair_pol
        self.phase_volt          = phase_volt
        self.frequency           = frequency
        self.motor_power         = motor_power
        self.velocity            = velocity
        self.current             = current
        self.efficiency          = efficiency
        self.cosfi               = cosfi
        self.critical_torq       = critical_torq
        self.start_torq          = start_torq
        self.start_curr          = start_curr
        self.act_stator_res      = act_stator_res
        self.act_rotor_res       = act_rotor_res
        self.react_stator_res    = react_stator_res
        self.react_rotor_res     = react_rotor_res
        self.magnetic_curr       = magnetic_curr

        self.radian_syncr_velocity_nom = 2 * math.pi * self.frequency / self.num_pair_pol
        self.radian_velocity_nom = self.velocity * (2 * math.pi / 60)
        self.torque_nom = self.motor_power / self.radian_velocity
        self.slip_nom = (self.radian_syncr_velocity_nom - self.radian_velocity_nom) / self.radian_syncr_velocity_nom
        self.critical_torq_rel = self.critical_torq / self.torque_nom
        self.start_torq_rel = self.start_torq / self.torque_nom
        self.start_curr_rel = self.start_curr / self.current
        reduce_coeff = self.act_stator_res / self.act_rotor_res
        self.critical_slip = self.slip_nom * (self.critical_torq_rel + sqrt((self.critical_torq_rel ** 2 - 1) + 2 * reduce_coeff * self.slip_nom * (self.critical_torq_rel - 1) ) / (1 - 2 * self.torque_nom * reduce_coeff * (self.torque_nom - 1)))
        