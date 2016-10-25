#!/usr/bin/python

import rospy
from chally_flow.msg import solutions
import operator

class flow(object):

	def speed_gate(self):
		#rospy.loginfo("**Beginning speed gate**")
		rospy.loginfo("**Speed gate complete**")

	def scan_the_code(self):
		rospy.loginfo("**Beginning scan the code challenge**")
		rospy.loginfo("**Scan the code challenge complete**")

	def detect_and_deliver(self, target_color, target_shape):
		#rospy.loginfo("**Beginning detect and deliver challenge**")
		if target_color != 'none':
			if target_color != 'green' and target_color != 'blue' and target_color != 'red':
				rospy.logerr("'%s' is not a valid color for self.target_deliver_color.  Valid colors are: 'red' 'green' 'blue'", target_color)
			else:
				#number = len(self.detect_deliver_grouped)
				for key in range(len(self.detect_deliver_grouped)):
					if self.detect_deliver_grouped[key][1][0] == target_color:
						rospy.loginfo(self.detect_deliver_grouped[key][1][1])#self.detect_deliver_grouped[0][1][0])
					#rospy.loginfo("working")
		elif target_color != 'none':
			ropy.loginfo("solving for color")

		#rospy.loginfo("**Detect and deliver challenge complete**")

		#odom = Odometry()


	def __init__(self):

		self.current_challenge_no = 1
		self.challenge_order = {}
		self.detect_deliver_shapes = {}
		self.detect_deliver_colors = {}
		self.detect_deliver_grouped = {}
		self.target_deliver_color = 'green'
		self.target_deliver_shape = 'none'

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

		self.deliver_color_1 = rospy.get_param('~deliver_color_1', 'green')
		self.deliver_color_2 = rospy.get_param('~deliver_color_2', 'green')
		self.deliver_color_3 = rospy.get_param('~deliver_color_3', 'red')
		self.deliver_color_4 = rospy.get_param('~deliver_color_4', 'blue')
		self.deliver_shape_1 = rospy.get_param('~deliver_shape_1', 'cross')
		self.deliver_shape_2 = rospy.get_param('~deliver_shape_2', 'circle')
		self.deliver_shape_3 = rospy.get_param('~deliver_shape_3', 'triangle')
		self.deliver_shape_4 = rospy.get_param('~deliver_shape_4', 'cross')

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

		self.detect_deliver_grouped['shape1'] = color1
		self.detect_deliver_grouped['shape2'] = color2
		self.detect_deliver_grouped['shape3'] = color3
		self.detect_deliver_grouped['shape4'] = color4

		self.detect_deliver_grouped = sorted(self.detect_deliver_grouped.items(), key=operator.itemgetter(0))		
		#rospy.loginfo(self.detect_deliver_grouped)

		self.solutions_pub = rospy.Publisher('solutions', solutions, queue_size=1)

		sols = solutions()

		rate = rospy.Rate(5)

		#sols.d_and_d_color = 'green'

		while not rospy.is_shutdown():

			for key, value in self.challenge_order.iteritems():
				if self.challenge_order[key]  == 'speed_gates':
					self.speed_gate()
				elif self.challenge_order[key] == 'detect_deliver':
					self.detect_and_deliver(self.target_deliver_color, self.target_deliver_shape)
				elif self.challenge_order[key] == 'scan_the_code':
					self.scan_the_code()	

			self.solutions_pub.publish(sols)

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