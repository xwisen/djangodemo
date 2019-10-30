from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render

import json

basepath="~"

class CharlesViews():
    def __init__(self):
        pass
    def get_money(request):
        # import pdb; pdb.set_trace()
        if request.method == "":
            return HttpResponse("It's null !")
        if request.method == "GET" or request.method == "POST":
            # if request.body
            if "DeviceType" in "{}".format(request.body):
                with open("{}".format("{}/cmb/DeviceType_AB_GeneralBill.aspx".format(basepath)), "r", encoding="utf-8") as f1:
                    cfg = json.load(f1)
                    f1.close()

                return HttpResponse(json.dumps(cfg))
        if request.method == "GET" or request.method == "POST":
            # if request.body
            if "QUERYTRANSREDFLAG" in "{}".format(request.body):
                with open("{}".format("{}/cmb/QUERYTRANSREDFLAG_AB_GeneralBill.aspx".format(basepath)), "r", encoding="utf-8") as f1:
                    cfg = json.load(f1)
                    f1.close()

                return HttpResponse(json.dumps(cfg))
            if "QUERYCARDBALANCE" in "{}".format(request.body):
                with open("{}".format("{}/cmb/QUERYCARDBALANCE_AB_GeneralBill.aspx".format(basepath)), "r", encoding="utf-8") as f1:
                    cfg = json.load(f1)
                    f1.close()

                return HttpResponse(json.dumps(cfg))
            if "QUERYTRXINFOLIST" in "{}".format(request.body):
                with open("{}".format("{}/cmb/04-AB_GeneralBill.aspx".format(basepath)), "r", encoding="utf-8") as f1:
                    cfg = json.load(f1)
                    f1.close()

                return HttpResponse(json.dumps(cfg))
            return HttpResponse("It's default !")

