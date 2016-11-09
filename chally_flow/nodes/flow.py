#!/usr/bin/python

import rospy
from chally_flow.msg import solutions
import operator
from random import randint
import random 
import math


class flow(object):

	def speed_gate(self):
		#rospy.loginfo("**Beginning speed gate**")
		rospy.loginfo("**Speed gate complete**")

	def scan_the_code(self):
		rospy.loginfo("**Beginning scan the code challenge**")
		rospy.loginfo("**Scan the code challenge complete**")

	def detect_and_deliver(self, target_color, target_shape):
		if target_color != 'none' and target_shape == 'none':
			rospy.loginfo("solving with color")
			if target_color != 'green' and target_color != 'blue' and target_color != 'red':
				rospy.logerr("'%s' is not a valid color for self.target_deliver_color.  Valid colors are: 'red' 'green' 'blue'", target_color)
				self.sols.d_and_d_confidence = 0.0
			else:
				#number = len(self.detect_deliver_grouped)
				no_of_sols = 0.0
				counter = 0
				guess_holder = []
				highest_confidence = 0.0
				key_holder = 0
				for key in range(len(self.detect_deliver_grouped)):
					if self.detect_deliver_grouped[key][1][0] == target_color:
						no_of_sols += 1.0
						counter += 1
						confidence = self.detect_deliver_grouped[key][1][2]
						if confidence >= highest_confidence:
							highest_confidence = confidence
							key_holder = key

						rospy.loginfo("confidence: %f", confidence)
						guess_holder.append(self.detect_deliver_grouped[key][1][1])
				#rospy.loginfo(guess_holder[randint(0,counter-1)])#self.detect_deliver_grouped[0][1][0])   randint(0,counter)    
				self.sols.d_and_d_color = target_color
				self.sols.d_and_d_shape = self.detect_deliver_grouped[key_holder][1][1]
				self.sols.d_and_d_confidence = (self.detect_deliver_grouped[key_holder][1][2]/.25)/no_of_sols
					#rospy.loginfo("working")
		elif target_color == 'none' and target_shape != 'none':
			rospy.loginfo("solving with shape")
			if target_shape != 'circle' and target_shape != 'triangle' and target_shape != 'cross':
				rospy.logerr("'%s' is not a valid shape for self.target_deliver_shape.  Valid shapes are: 'circle' 'triangle' 'cross'", target_shape)
				self.sols.d_and_d_confidence = 0.0
			else:
				no_of_sols = 0.0
				counter = 0
				guess_holder = []
				highest_confidence = 0.0
				key_holder = 0
				for key in range(len(self.detect_deliver_grouped)):
					if self.detect_deliver_grouped[key][1][1] == target_shape:
						no_of_sols += 1.0
						counter += 1
						confidence = self.detect_deliver_grouped[key][1][2]
						if confidence >= highest_confidence:
							highest_confidence = confidence
							key_holder = key
						rospy.loginfo("confidence: %f", confidence)
						guess_holder.append(self.detect_deliver_grouped[key][1][0])
				self.sols.d_and_d_color = self.detect_deliver_grouped[key_holder][1][0]
				self.sols.d_and_d_shape = target_shape 
				self.sols.d_and_d_confidence = (self.detect_deliver_grouped[key_holder][1][2]/.25)/no_of_sols					
				#rospy.loginfo(self.detect_deliver_grouped[key][1][0])#self.detect_deliver_grouped[0][1][0])				
		elif target_color == 'none' and target_shape == 'none':  #Guess!!!
			rospy.loginfo("Guessing!!!")
			confidence_list = (self.detect_deliver_grouped[0][1][2], self.detect_deliver_grouped[1][1][2], 
			self.detect_deliver_grouped[2][1][2], self.detect_deliver_grouped[3][1][2])


			confidence_list_max = max(confidence_list)

			for i in range (0,3):
				if self.detect_deliver_grouped[i][1][2] == confidence_list_max:
					self.sols.d_and_d_color = self.detect_deliver_grouped[i][1][0]
					self.sols.d_and_d_shape = self.detect_deliver_grouped[i][1][1]
					self.sols.d_and_d_confidence = self.detect_deliver_grouped[i][1][2]
					#rospy.loginfo(self.sols)
					break

		elif target_color != 'none' and target_shape != 'none':
			#rospy.loginfo("solving with two knowns")
			confidence = 0.0
			for i in range(0,3):
				if self.detect_deliver_grouped[i][1][0] == target_color and self.detect_deliver_grouped[i][1][1] == target_shape:
					confidence = self.detect_deliver_grouped[i][1][2]/0.25
					#rospy.logwarn("confidence: %f",self.detect_deliver_grouped[i][1][2])
			self.sols.d_and_d_color = target_color
			self.sols.d_and_d_shape = target_shape
			self.sols.d_and_d_confidence = confidence




	def __init__(self):

		random.seed(None)

		self.current_challenge_no = 1
		self.challenge_order = {}
		self.detect_deliver_shapes = {}
		self.detect_deliver_colors = {}
		self.detect_deliver_grouped = {}
		self.target_deliver_color = 'none'
		self.target_deliver_shape = 'circle'

		self.challenge_1 = rospy.get_param('~challenge_1', 'detect_deliver')
		self.challenge_2 = rospy.get_param('~challenge_2', 'none')
		self.challenge_3 = rospy.get_param('~challenge_3', 'none')
		self.challenge_4 = rospy.get_param('~challenge_4', 'none')
		self.challenge_5 = rospy.get_param('~challenge_5', 'none')
		self.challenge_6 = rospy.get_param('~challenge_6', 'none')
		self.challenge_7 = rospy.get_param('~challenge_7', 'none')

		self.scan_code_color_1 = rospy.get_param('~code_color_1', 'none')
		self.scan_code_color_2 = rospy.get_param('~code_color_2', 'none')
		self.scan_code_color_3 = rospy.get_param('~code_color_3', 'none')

		self.deliver_color_1 = rospy.get_param('~deliver_color_1', 'none')
		self.deliver_shape_1 = rospy.get_param('~deliver_shape_1', 'none')
		self.deliver_color_2 = rospy.get_param('~deliver_color_2', 'none')
		self.deliver_shape_2 = rospy.get_param('~deliver_shape_2', 'cross')
		self.deliver_color_3 = rospy.get_param('~deliver_color_3', 'none')
		self.deliver_shape_3 = rospy.get_param('~deliver_shape_3', 'none')
		self.deliver_color_4 = rospy.get_param('~deliver_color_4', 'green')
		self.deliver_shape_4 = rospy.get_param('~deliver_shape_4', 'triangle')

		self.challenge_order['chal_1'] = self.challenge_1 
		self.challenge_order['chal_2'] = self.challenge_2 
		self.challenge_order['chal_3'] = self.challenge_3 
		self.challenge_order['chal_4'] = self.challenge_4 
		self.challenge_order['chal_5'] = self.challenge_5 
		self.challenge_order['chal_6'] = self.challenge_6 
		self.challenge_order['chal_7'] = self.challenge_7 

		value_to_remove = 'none'
		self.challenge_order = {key: value for key, value in self.challenge_order.items() if value != value_to_remove}

		color1 = [self.deliver_color_1]
		shape1 = self.deliver_shape_1
		color2 = [self.deliver_color_2]
		shape2 = self.deliver_shape_2
		color3 = [self.deliver_color_3]
		shape3 = self.deliver_shape_3
		color4 = [self.deliver_color_4]
		shape4 = self.deliver_shape_4

		color1.append(shape1)
		color2.append(shape2)
		color3.append(shape3)
		color4.append(shape4)

		color1.append(0.25)
		color2.append(0.25)
		color3.append(0.25)
		color4.append(0.25)

		self.detect_deliver_grouped['shape1'] = color1
		self.detect_deliver_grouped['shape2'] = color2
		self.detect_deliver_grouped['shape3'] = color3
		self.detect_deliver_grouped['shape4'] = color4

		self.detect_deliver_grouped = sorted(self.detect_deliver_grouped.items(), key=operator.itemgetter(0))		
		#rospy.loginfo(self.detect_deliver_grouped)

		none_shape = 0
		none_color = 0
		green_num = 0
		red_num = 0
		blue_num = 0
		circle_num = 0
		cross_num = 0
		triangle_num = 0


		for i in range(4):
			for z in range(2):
				if (self.detect_deliver_grouped[i][1][z] != 'red' and self.detect_deliver_grouped[i][1][z] != 'green' and self.detect_deliver_grouped[i][1][z] != 'blue'
				and self.detect_deliver_grouped[i][1][z] != 'circle' and self.detect_deliver_grouped[i][1][z] != 'cross' and self.detect_deliver_grouped[i][1][z] != 'triangle'
				and self.detect_deliver_grouped[i][1][z] != 'none'):
					rospy.logerr("'%s' is not a valid color or shape for detect and deliver, check deliver color/shape params. ", self.detect_deliver_grouped[i][1][z])
					rospy.signal_shutdown('Invalid input for detect and deliver params')
				else:
					if self.detect_deliver_grouped[i][1][z] == 'none' and z == 1:
						none_shape += 1
					elif self.detect_deliver_grouped[i][1][z] == 'none' and z == 0:
						none_color += 1		
					elif self.detect_deliver_grouped[i][1][z] == 'green':
						green_num += 1
					elif self.detect_deliver_grouped[i][1][z] == 'red':
						red_num += 1
					elif self.detect_deliver_grouped[i][1][z] == 'blue':
						blue_num += 1
					elif self.detect_deliver_grouped[i][1][z] == 'circle':
						circle_num += 1
					elif self.detect_deliver_grouped[i][1][z] == 'triangle':
						triangle_num += 1
					elif self.detect_deliver_grouped[i][1][z] == 'cross':
						cross_num += 1

		num_none = none_shape + none_color
		self.uncertainty = math.pow(3,num_none)

		#rospy.loginfo(self.detect_deliver_grouped)
		while(none_shape > 0 or none_color > 0):

			for i in range(4):
				shape_sum = circle_num + cross_num + triangle_num
				if shape_sum == 0:
					shape_sum = 1
				circle_percent = float(circle_num) / float(shape_sum)
				triangle_percent = float(triangle_num) / float(shape_sum)
				cross_percent = float(cross_num) / float(shape_sum)

				shape_dictionary = {'circle':circle_percent, 'triangle':triangle_percent, 'cross':cross_percent}
				shape_min = min(shape_dictionary['circle'], shape_dictionary['triangle'], shape_dictionary['cross'])

				shape_dictionary = sorted(shape_dictionary.items(), key=operator.itemgetter(0))

				color_sum = green_num + red_num + blue_num
				if color_sum == 0:
					color_sum = 1
				red_percent = float(red_num) / float(color_sum)
				green_percent = float(green_num) / float(color_sum)
				blue_percent = float(blue_num) / float(color_sum)

				color_dictionary = {'red':red_percent, 'green':green_percent, 'blue':blue_percent}
				color_min = min(color_dictionary['red'], color_dictionary['green'], color_dictionary['blue'])

				color_dictionary = sorted(color_dictionary.items(), key=operator.itemgetter(0))

				if self.detect_deliver_grouped[i][1][1] == 'none':
					for s in range (0,3):
						if shape_dictionary[s][1] == shape_min:
							self.detect_deliver_grouped[i][1][1] = shape_dictionary[s][0]
							self.detect_deliver_grouped[i][1][2] = self.detect_deliver_grouped[i][1][2]/3
							#rospy.loginfo(self.detect_deliver_grouped)
							break
					
				elif self.detect_deliver_grouped[i][1][0] == 'none':
					for s in range (0,3):
						if color_dictionary[s][1] == color_min:
							self.detect_deliver_grouped[i][1][0] = color_dictionary[s][0]
							self.detect_deliver_grouped[i][1][2] = self.detect_deliver_grouped[i][1][2]/3
							#rospy.loginfo(self.detect_deliver_grouped)
							break

				none_shape = 0
				none_color = 0
				green_num = 0
				red_num = 0
				blue_num = 0
				circle_num = 0
				cross_num = 0
				triangle_num = 0

				for i in range(4):
					for z in range(2):
						if self.detect_deliver_grouped[i][1][z] == 'none' and z == 1:
							none_shape += 1
						elif self.detect_deliver_grouped[i][1][z] == 'none' and z == 0:
							none_color += 1
						elif self.detect_deliver_grouped[i][1][z] == 'green':
							green_num += 1
						elif self.detect_deliver_grouped[i][1][z] == 'red':
							red_num += 1
						elif self.detect_deliver_grouped[i][1][z] == 'blue':
							blue_num += 1
						elif self.detect_deliver_grouped[i][1][z] == 'circle':
							circle_num += 1
						elif self.detect_deliver_grouped[i][1][z] == 'triangle':
							triangle_num += 1
						elif self.detect_deliver_grouped[i][1][z] == 'cross':
							cross_num += 1

		self.solutions_pub = rospy.Publisher('solutions', solutions, queue_size=1)

		self.sols = solutions()

		rate = rospy.Rate(5)

		#sols.d_and_d_color = 'green'

		for key, value in self.challenge_order.iteritems():
			if self.challenge_order[key]  == 'speed_gates':
				self.speed_gate()
			elif self.challenge_order[key] == 'detect_deliver':
				self.detect_and_deliver(self.target_deliver_color, self.target_deliver_shape)
			elif self.challenge_order[key] == 'scan_the_code':
				self.scan_the_code()	

		rospy.loginfo(self.sols)				

		self.solutions_pub.publish(self.sols)

		while not rospy.is_shutdown():
			rate.sleep()

		#need a while loop that waits for a query of the task info
		#publish shooter solution, docking solution.....


def main():
	rospy.init_node('challenge_flow', anonymous=False)

	flow()

	try:
		rospy.spin()
	except rospy.ROSInterruptException:
		print "Shutting down"
		pass


if __name__ == '__main__':
	main() #sys.argv