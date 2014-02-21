#!/usr/bin/env python
import roslib; roslib.load_manifest('mln_interface')

from mln_interface.srv import *
from mln_interface.msg import *
import rospy

from mlnQueryTool import MLNInfer

def handle_mln_query(req):
	inf = MLNInfer()

	results = inf.run(req.query.mlnFiles, req.query.db, req.query.method, req.query.queries, req.query.engine, req.query.output_filename,
				              saveResults=req.query.saveResults, maxSteps=5000, logic=req.query.logic, grammar=req.query.grammar)
	tuple_list = []
	for atom, p in results.iteritems():
		tuple_list.append(AtomProbPair(atom, p))

	return MLNInterfaceResponse(MLNResponse(tuple_list))

def mln_interface_server():
    rospy.init_node('mln_interface_server')
    s = rospy.Service('mln_interface', MLNInterface, handle_mln_query)
    print "MLN is ready to be queried."
    rospy.spin()

if __name__ == "__main__":
    mln_interface_server()


