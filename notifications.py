from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import xml.etree.ElementTree as et
from prettytable import *


class create_notification_832:

    def __init__(self, formatted_segments, file):
        self.formatted_segments = formatted_segments
        self.file = file

    def parse_edi_email(self, formatted_segments):

        recipients = ["Routing100@gpalogisticsgroup.com", "edisupport@2253apparelco.com",
                      "lgabriel@celebritypinkusa.com", "mperez@celebritypinkusa.com", "mrocha@celebritypinkusa.com",
                      "mjimenez@2253apparelco.com"]
        # recipients = ["cmaya@gpalogisticsgroup.com"]

        table = PrettyTable(['Item Number'])

        # variables specific to the translation
        for seg in formatted_segments:
            if seg[0] == 'ISA':
                control_number = seg[13]
            if seg[0] == 'LIN':
                style = seg[3]
                item_number = seg[5]
                table.add_row([item_number])
            if seg[0] == "IEA":
                # Email Content
                Subject = f"ICN:{control_number} - GPA Logistics - CelebrityPink 832 Upload: " + datetime.now().strftime(
                    "%m/%d/%Y %H:%M:%S")
                client = 'CelebrityPink'
                logo = 'https://www.gpalogisticsgroup.com/wp-content/uploads/2020/06/GPA-Logistics-Logo.jpg'
                Text = f"""
                <html>
                <head>
                  <style>
                    table {{
                      font-family: Arial, sans-serif;
                      border-collapse: collapse;
                      width: 100%;
                    }}
                    th, td {{
                      border: 1px solid #dddddd;
                      text-align: left;
                      padding: 8px;
                    }}
                    th {{
                      background-color: #f2f2f2;
                    }}
                    .highlight {{
                        color: #FF9900;
                    }}
                  </style>
                </head>
                <body>
                    <p>Hello <strong>{client}</strong> team,</p>
                    <p>The following items have been successfully imported into our system.</p>
                    <br>
                  {table.get_html_string()}
                    <br>
                    <div style="font-family: Arial, sans-serif; font-size: 12px;">
                        <br>
                        <p style="margin : 0;"><strong>Thank you,</strong></p>
                        <p style="margin : 0;"><strong>GPA TEAM</strong></p>
                        <p style="margin : 0;"><strong>GPA Logistics Group, Inc.</strong></p>
                        <p style="margin : 0;">1600 S. Baker Ave.<br>
                        Ontario, CA 91761</p>
                        <hr>
                        <p style="margin : 0;"><a href="http://www.gpalogisticsgroup.com">www.gpalogisticsgroup.com</a></p>
                        <p style="margin : 0;"><a href="http://www.gpaglobal.net">www.gpaglobal.net</a></p>
                        <br>
                            <img src={logo} alt="GPA Logistics Logo" style="width:150px;">
                        <p>Shenzhen | Hong Kong | New York | <span class ="highlight">Los Angeles</span> | San Francisco | Miami | Cambridge UK | Dublin | Mexico | Vietnam | Thailand | Malaysia</p>
                    </div>

                </body>
                </html>
                """

                server = smtplib.SMTP('smtp.office365.com', 587)
                server.starttls()
                server.login('noreply@gpalogisticsgroup.com', 'Turn*17300')
                msg = MIMEMultipart()
                message = f'{Text}\n'
                msg['Subject'] = Subject
                msg['From'] = 'noreply@gpalogisticsgroup.com'
                msg['To'] = '; '.join(recipients)
                msg.attach(MIMEText(message, 'html'))
                server.send_message(msg)
                server.quit()


class create_notification_940:

    def __init__(self, formatted_segments):
        self.formatted_segments = formatted_segments

    def parse_edi_email(self):

        recipients = ["88roxy@gpalogisticsgroup.com", "edisupport@2253apparelco.com", "customerservice@brandworksus.com"]
        # recipients = ["cmaya@gpalogisticsgroup.com"]

        table = PrettyTable(['OrderNumber', 'CustomerName', 'RequestedShipDate', 'CancelDate'])

        # variables specific to the translation
        count = 0
        for seg in self.formatted_segments:
            if seg[0] == 'ISA':
                control_number = seg[13]
            if seg[0] == "W05":
                depositor_order_number = seg[2]
            if seg[0] == "N1" and seg[1] == "OB":
                customer_name = seg[4]
            if seg[0] == "G62" and seg[1] == "01":
                cancel_date = seg[2]
                cancel_date = '-'.join([cancel_date[:4], cancel_date[4:6], cancel_date[6:]])
            if seg[0] == "G62" and seg[1] == "02":
                requested_ship_date = seg[2]
                requested_ship_date = '-'.join([requested_ship_date[:4], requested_ship_date[4:6], requested_ship_date[6:]])
            if seg[0] == "W20":
                quantity = seg[1]
            if seg[0] == "SE":
                count = count + 1
                table.add_row([depositor_order_number, customer_name, requested_ship_date, cancel_date])
            if seg[0] == "IEA":
                # Email Content
                Subject = f"ICN:{control_number} - GPA Logistics - Roxy 940 Upload: " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                client = 'Roxy'
                logo = 'https://www.gpalogisticsgroup.com/wp-content/uploads/2020/06/GPA-Logistics-Logo.jpg'
                Text = f"""
                <html>
                <head>
                  <style>
                    table {{
                      font-family: Arial, sans-serif;
                      border-collapse: collapse;
                      width: 100%;
                    }}
                    th, td {{
                      border: 1px solid #dddddd;
                      text-align: left;
                      padding: 8px;
                    }}
                    th {{
                      background-color: #f2f2f2;
                    }}
                    .highlight {{
                        color: #FF9900;
                    }}
                  </style>
                </head>
                <body>
                    <p>Hello <strong>{client}</strong> team,</p>
                    <p>The following {count} orders have been successfully imported into our system.</p>
                    <br>
                  {table.get_html_string()}
                    <br>
                    <div style="font-family: Arial, sans-serif; font-size: 12px;">
                        <br>
                        <p style="margin : 0;"><strong>Thank you,</strong></p>
                        <p style="margin : 0;"><strong>GPA TEAM</strong></p>
                        <p style="margin : 0;"><strong>GPA Logistics Group, Inc.</strong></p>
                        <p style="margin : 0;">1600 S. Baker Ave.<br>
                        Ontario, CA 91761</p>
                        <hr>
                        <p style="margin : 0;"><a href="http://www.gpalogisticsgroup.com">www.gpalogisticsgroup.com</a></p>
                        <p style="margin : 0;"><a href="http://www.gpaglobal.net">www.gpaglobal.net</a></p>
                        <br>
                            <img src={logo} alt="GPA Logistics Logo" style="width:150px;">
                        <p>Shenzhen | Hong Kong | New York | <span class ="highlight">Los Angeles</span> | San Francisco | Miami | Cambridge UK | Dublin | Mexico | Vietnam | Thailand | Malaysia</p>
                    </div>

                </body>
                </html>
                """

                server = smtplib.SMTP('smtp.office365.com', 587)
                server.starttls()
                server.login('noreply@gpalogisticsgroup.com', 'Turn*17300')
                msg = MIMEMultipart()
                message = f'{Text}\n'
                msg['Subject'] = Subject
                msg['From'] = 'noreply@gpalogisticsgroup.com'
                msg['To'] = '; '.join(recipients)
                msg.attach(MIMEText(message, 'html'))
                server.send_message(msg)
                server.quit()


class create_notification_943:

    def __init__(self, formatted_segments):
        self.formatted_segments = formatted_segments

    def parse_edi_email(self):

        # recipients = ["walnutinbounds@gpalogisticsgroup.com"]
        recipients = ["cmaya@gpalogisticsgroup.com"]

        table = PrettyTable(['ContainerNumber', 'PurchaseOrderNumber'])

        # variables specific to the translation
        count = 0
        for seg in self.formatted_segments:
            if seg[0] == 'ISA':
                control_number = seg[13]
            if seg[0] == 'W06':
                purchase_order_number = seg[2]
            if seg[0] == "N9" and seg[1] == "ER":
                depositor_order_number = seg[2]
            if seg[0] == "SE":
                count = count + 1
                table.add_row([depositor_order_number, purchase_order_number])
            if seg[0] == "IEA":
                # Email Content
                Subject = f"ICN:{control_number} - GPA Logistics - Roxy 943 Upload: " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                client = 'Roxy'
                logo = 'https://www.gpalogisticsgroup.com/wp-content/uploads/2020/06/GPA-Logistics-Logo.jpg'
                Text = f"""
                <html>
                <head>
                  <style>
                    table {{
                      font-family: Arial, sans-serif;
                      border-collapse: collapse;
                      width: 100%;
                    }}
                    th, td {{
                      border: 1px solid #dddddd;
                      text-align: left;
                      padding: 8px;
                    }}
                    th {{
                      background-color: #f2f2f2;
                    }}
                    .highlight {{
                        color: #FF9900;
                    }}
                  </style>
                </head>
                <body>
                    <p>Hello <strong>{client}</strong> team,</p>
                    <p>The following container has been successfully imported into our system.</p>
                    <br>
                  {table.get_html_string()}
                    <br>
                    <div style="font-family: Arial, sans-serif; font-size: 12px;">
                        <br>
                        <p style="margin : 0;"><strong>Thank you,</strong></p>
                        <p style="margin : 0;"><strong>GPA TEAM</strong></p>
                        <p style="margin : 0;"><strong>GPA Logistics Group, Inc.</strong></p>
                        <p style="margin : 0;">1600 S. Baker Ave.<br>
                        Ontario, CA 91761</p>
                        <hr>
                        <p style="margin : 0;"><a href="http://www.gpalogisticsgroup.com">www.gpalogisticsgroup.com</a></p>
                        <p style="margin : 0;"><a href="http://www.gpaglobal.net">www.gpaglobal.net</a></p>
                        <br>
                            <img src={logo} alt="GPA Logistics Logo" style="width:150px;">
                        <p>Shenzhen | Hong Kong | New York | <span class ="highlight">Los Angeles</span> | San Francisco | Miami | Cambridge UK | Dublin | Mexico | Vietnam | Thailand | Malaysia</p>
                    </div>

                </body>
                </html>
                """

                server = smtplib.SMTP('smtp.office365.com', 587)
                server.starttls()
                server.login('noreply@gpalogisticsgroup.com', 'Turn*17300')
                msg = MIMEMultipart()
                message = f'{Text}\n'
                msg['Subject'] = Subject
                msg['From'] = 'noreply@gpalogisticsgroup.com'
                msg['To'] = '; '.join(recipients)
                msg.attach(MIMEText(message, 'html'))
                server.send_message(msg)
                server.quit()


class create_notification_945:

    def __init__(self, XML, file):
        self.XML = XML
        self.file = file

    def parse_xml_email(self, file):

        filename = file.split(".")[0]
        depositor_order_number = filename.split("_")[3]

        oak = et.parse(self.XML)
        rooted = oak.getroot()

        for element in rooted.iter():
            if element.tag == 'ShipmentHeader':
                for ReceiptHeader_child_element in element:
                    if ReceiptHeader_child_element.tag == 'TotalCartonCount':
                        total_carton_count = ReceiptHeader_child_element.text
            if element.tag == 'ShipTo':
                for ShipTo_child_element in element:
                    if ShipTo_child_element.tag == 'Name':
                        ship_to_name = ShipTo_child_element.text

        completed_string = depositor_order_number + '                 ' + total_carton_count + '            ' + ship_to_name + "\n"

        with open("C:\\FTP\\GPAEDIProduction\\WN1-CelebrityPink\\Logs\\email\\945_pending_email_orders.txt", "a") as completed_file:
            completed_file.write(completed_string)
