#!/usr/bin/env python
import roslib; roslib.load_manifest('mln_interface')

import sys

import rospy
from mln_interface.srv import *
from mln_interface.msg import *

def mln_interface_client(mlnFiles, db, method, queries, engine, output_filename, saveResults=False, logic="FirstOrderLogic", grammar="PRACGrammar"):
    rospy.wait_for_service('mln_interface')
    try:
        mln_interface = rospy.ServiceProxy('mln_interface', MLNInterface)
        resp1 = mln_interface(MLNQuery(mlnFiles, db, method, queries, engine, output_filename, saveResults, logic, grammar))
        return resp1.response.results
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [mlnFiles db]"%sys.argv[0]

if __name__ == "__main__":
   	mlnFiles = "etc/wts.pybpll.smoking-train-smoking.mln"
	db = "etc/smoking-test-smaller.db"
	queries = "Smokes"
	output_filename = "results.txt"
        print (mln_interface_client(mlnFiles, db, "MC-SAT", queries, "PRACMLNs", "results.txt"))

