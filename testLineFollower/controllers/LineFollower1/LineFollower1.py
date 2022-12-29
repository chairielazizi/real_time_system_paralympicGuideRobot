# You may need to import some classes of the controller module. Ex: 
#  from controller import Robot, Motor, DistanceSensor 
 
from controller import Robot 
 
def run_robot(robot):  
    # get the time step of the current world. 
    time_step = 1 
    max_speed = 3.28 #epuck max 6.28
    # You should insert a getDevice-like function in order to get the 
    # instance of a device of the robot. Something like: 
    #  motor = robot.getDevice('motorname') 
    #  ds = robot.getDevice('dsname') 
    #  ds.enable(timestep) 
     
    left_motor = robot.getMotor('left wheel motor') 
    right_motor =  robot.getMotor('right wheel motor') 
    left_motor.setPosition(float('inf')) 
    right_motor.setPosition(float('inf')) 
    left_motor.setVelocity(0.0) 
    right_motor.setVelocity(0.0) 
     
    left_ir = robot.getDistanceSensor('LeftR') 
    left_ir.enable(time_step) 
     
    right_ir = robot.getDistanceSensor('RightR') 
    right_ir.enable(time_step) 
 
    # Main loop: 
    # - perform simulation steps until Webots is stopping the controller 
    while robot.step(time_step) != -1: 
         # Read the sensors: 
    # Enter here functions to read sensor data, like: 
    #  val = ds.getValue() 
    # Process sensor data here. 
    # Enter here functions to send actuator commands, like: 
    #  motor.setPosition(10.0) 
        left_ir_value = left_ir.getValue() 
        right_ir_value = right_ir.getValue() 
        middle_ir_value = 277
        print ("left: {} right: {}" .format(left_ir_value, right_ir_value)) 
 
        if  left_ir_value < middle_ir_value and right_ir_value < middle_ir_value:  
            left_speed = max_speed 
            right_speed = max_speed   
            print ("Forward left: {} right: {}" .format(left_speed, right_speed)) 
        if  right_ir_value < middle_ir_value and left_ir_value > middle_ir_value:  
            left_speed = max_speed * 0.5 
            right_speed = max_speed  
            print ("RIGHT Movement left: {} right: {}" .format(left_speed, right_speed)) 
        if  left_ir_value < middle_ir_value  and right_ir_value > middle_ir_value :  
            left_speed = max_speed  
            right_speed = max_speed * 0.5 
            print ("LEFT Movement left: {} right: {}" .format(left_speed, right_speed)) 
                             
        left_motor.setVelocity(left_speed) 
        right_motor.setVelocity(right_speed) 
         
if __name__ == "__main__": 
    my_robot = Robot() 
    run_robot(my_robot) 