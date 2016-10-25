#!/usr/bin/python

import rospy

class flow(object):

	def speed_gate(self):
		rospy.loginfo("**Beginning speed gate**")
		rospy.loginfo("**Speed gate complete**")

	def scan_the_code(self, data):
		rospy.loginfo("**Beginning scan the code challenge**")
		rospy.loginfo("**Scan the code challenge complete**")

	def detect_and_deliver(self, color1, color2, color3):
		rospy.loginfo("**Beginning detect and deliver challenge**")

		rospy.loginfo("**Detect and deliver challenge complete**")

		#odom = Odometry()


	def __init__(self):

		self.current_challenge_no = 1

		self.challenge_1 = rospy.get_param('~challenge_1', 'none')
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
		self.deliver_color_2 = rospy.get_param('~deliver_color_2', 'none')
		self.deliver_color_3 = rospy.get_param('~deliver_color_3', 'none')
		self.deliver_color_4 = rospy.get_param('~deliver_color_4', 'none')
		self.deliver_shape_1 = rospy.get_param('~deliver_shape_1', 'none')
		self.deliver_shape_2 = rospy.get_param('~deliver_shape_2', 'none')
		self.deliver_shape_3 = rospy.get_param('~deliver_shape_3', 'none')
		self.deliver_shape_4 = rospy.get_param('~deliver_shape_4', 'none')


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