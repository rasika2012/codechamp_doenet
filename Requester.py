##################################################
## Simple Aplication to access Doenets
##################################################
## License under GPL3 Version
##################################################
## Author: Rasika Maduranga
## Copyright: Copyright 2019, GCE AL Result App
## Credits: [jpura fot]
## License: GPL3
## Version: 0.0.2
## Email: rasikat77@gmail.com
## Status: Educational purpose only
##################################################
import requests

class Doenets:
    """
    Doenet class is designed for acces GCE AL 2018

    """

    """
    Path to result 
    """
    path = "https://doenets.lk/result/alresult.jsf?frm=frm&frm%3Ausername=@@@@&frm%3AbtnSubmit=&javax.faces.ViewState=MgzdVoQmvPvjp3Bl6xFiDBwAHJGX0LClVRevz5%2F9cm9T13tcn49Gcbpv1viVmu%2F3ErGVPWDTfsEiHaTlp%2Bz6am%2FJj0qeDcGtb%2FcwjBMUEfrBsfRjmPu%2B1N5gcJXYUpJ8V04JOyOiLA4ifbYGTDRbmaPtr06SsKC4Mqm%2BqJw732f%2BqeUxfRvUzAQuLjE8u7gvX7poihDrclfeA3VRQMA3piJbQgqGs6mShnNuIt2CgkNGoSjkM6UeruOenpM4MCjb%2FUuL%2F7SNCwxdnkT7YbMWQ1GWTZnXducybrkZLY0V%2BltkzRKkyrbteDCw5sAdeyn%2FetA5ZGXXXdv5j3hULPFvr8UZkKtqgTFvBgP5Pm43ZlVOr5v3DQyJ8PCZcz4i2m3KRTIbGyLi1yPgTNo%2ByDj7xR%2F09Aeo0Rck03iT3BToftTdwxVHGjDLQ%2FOuXFRdKrVkJlqi106NPiX8umeh%2BA0aBC5QSHMCHhpAK9Mz9TqK2%2FotM84%2BWhw9uy%2FQo80vaRUaWGUh6qDG9VjUc0ONdHX2kxfYfOLsahDS3dI%2Fuwqbv8RXfSngnXYCQR6V9CGDjfO2OZLD2y4nKpYOtR2HGSC5yr%2BExwaCDLbAcW7ffPVvYKl7qPmJxu0Nh2Wpl%2BBuvgL3rVMa2IQmwrH%2BMCD%2F7%2FZa6b13v81aIIpujuODNUol44ThGZ5jVoBzp0pM7BsFWlCW3Ya7f97TumLDlcSp3Leg72tco1gEzg%2B45YxnCQGZHikfRtfh36ywya47BOkfuoMcDtZ61z47hKeD7qV0Dfe3HbbdfQ2As7RGTJ9xqpurLvc%3D"

    def __init__(self):
        pass

    def read_result(self, index):
        """
        Send index to doenet and get html form result and extrack details

        :param index: index number (string | int)
        :return: result
        """
        r = requests.get(Doenets.path.replace("@@@@", str(index)))

        txt = (r.text.split("\n"))
        ex_name = False
        ex_DR = False
        ex_IR = False
        ex_Z = False
        ex_stream = False
        sub = False
        res = {"res": {}}
        subject = ""
        for line in txt:
           
            try:
                    
                # Name of the student
                if "Name :</td><td role=\"gridcell\" style=\"text-align:left;border-left:none\">" in line:
                    ex_name = True
                elif ex_name:
                    res['Name'] = line.replace("\t", "").replace("  ", "")
                    ex_name = False
                    res['Index'] = str(index)

                # DR of the student
                elif "District Rank :</td><td role=\"gridcell\"" in line:
                    ex_DR = True
                elif ex_DR:
                    res['District Rank'] = line.replace("\t", "").replace("  ", "")
                    ex_DR = False

                # IR of the student
                elif "Island Rank :</td><td role=\"gridcell\" style=\"" in line:
                    ex_IR = True
                elif ex_IR:
                    res['Island Rank'] = line.replace("\t", "").replace("  ", "")
                    ex_IR = False

                # Z Score of the student
                elif "Z-Score :</td><td role=\"gridcell\" style" in line:
                    ex_Z = True
                elif ex_Z:
                    res['Z-Score'] = line.replace("\t", "").replace("  ", "")
                    ex_Z = False

                # Subject Streame of the student
                elif " Subject Stream :</td><td role=\"gridcell\"" in line:
                    ex_stream = True
                elif ex_stream:
                    res['Subject Stream'] = line.replace("\t", "").replace("  ", "")
                    ex_stream = False

                # Extract Subject info from respond
                elif "<br /><div id=\"j_idt16:j_idt26\" class=\"ui-datatable ui-widget\"><div class=\"ui-datatable-tablewrapper\"><table role=\"grid\">" in line:
                    for wrd in line.split("<td role=\"gridcell\">"):
                        for p in (wrd.split("</td>")):
                            if "<" not in p:
                                if p != '':
                                    if sub == True:
                                        res["res"][subject] = p
                                        sub = False
                                    else:
                                        subject = p
                                        sub = True
            except:
                print("Network Error:Try Again")
        
        return res

