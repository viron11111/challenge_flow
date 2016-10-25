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


		#need a while loop that waits for a query of the next task

		self.base()
		rospy.Subscriber("joy", Joy, self.action)
		rospy.Subscriber("/odometry/filtered", Odometry, self.odom_location)
		self.pose_pub = rospy.Publisher("RC_position", PoseWithCovarianceStamped, queue_size = 1)



		rate = rospy.Rate(20)
		self.start()

		while not rospy.is_shutdown():

			br = tf2_ros.TransformBroadcaster()
			t = geometry_msgs.msg.TransformStamped()

			self.subposx += self.movex
			self.subposy += self.movey

			quat = (
				self.subrotx,
				self.subroty,
				self.subrotz,
				self.subrotw)

			euler = tf.transformations.euler_from_quaternion(quat)
			
			turn = euler[2] + self.yaw
			euler = (
				euler[0],
				euler[1],
				turn)
			#rospy.loginfo(euler)

			quat = tf.transformations.quaternion_from_euler(euler[0],euler[1], euler[2])
			self.subrotx = quat[0]
			self.subroty = quat[1]
			self.subrotz = quat[2]
			self.subrotw = quat[3]

			t.transform.translation.x = self.subposx
			t.transform.translation.y = self.subposy
			t.transform.translation.z = self.subposz
			t.transform.rotation.x = self.subrotx
			t.transform.rotation.y = self.subroty
			t.transform.rotation.z = self.subrotz
			t.transform.rotation.w = self.subrotw

			#odom = Odometry()

			t.header.stamp = rospy.Time.now()
			t.header.frame_id = "map"
			t.child_frame_id = "desired_position"
			br.sendTransform(t)	

			'''t.transform.translation.x = 0
			t.transform.translation.y = 0
			t.transform.translation.z = 0
			t.transform.rotation.x = 0
			t.transform.rotation.y = 0
			t.transform.rotation.z = 0
			t.transform.rotation.w = 1.0

			#odom = Odometry()

			t.header.stamp = rospy.Time.now()
			t.header.frame_id = "map"
			t.child_frame_id = "odom"
			br.sendTransform(t)	'''

			rate.sleep()

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