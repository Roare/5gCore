# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g

from flask_restful import Resource,reqparse
parser = reqparse.RequestParser()
parser.add_argument('MCC')

class ONENONUEN2MSGSUB(Resource):

    def delete(self,n2NotifySubscriptionId):
    	args = parser.parse_args()
    	print(n2NotifySubscriptionId)
        return "visit AMF Communication service operation(http method: delete) : /namf-comm/v1/non-ue-n2-messages/subscriptions/<int:n2NotifySubscriptionId>"
