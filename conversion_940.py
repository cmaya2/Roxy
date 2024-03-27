import xml.etree.ElementTree as et
from datetime import datetime


class Convert_940:

    def __init__(self, formatted_segments, path, mantis_import_path, transaction_number, client_id, facility):
        self.formatted_segments = formatted_segments
        self.path = path
        self.mantis_import_path = mantis_import_path
        self.transaction_number = transaction_number
        self.client_id = client_id
        self.facility = facility

    def parse_edi(self):

        nte_line = []
        identifier = 0

        carriers = {
            'F7-FEDEX 2DAY': 'FEDEX_2_DAY',
            'F2-FED EX COLLECT': 'Ground',
            'F6-FEDEX FREIGHT ECONOMY': 'FEDEX_FREIGHT_ECONOMY',
            'F9-FEDEX GROUND': 'FEDEX_GROUND',
            'CG-FEDEX GROUND HOME DELIVERY': 'GROUND_HOME_DELIVERY',
            'RE-FEDEX GROUND RESIDENTIAL': 'GROUND_HOME_DELIVERY',
            'CG-FEDEX SMART POST': 'SMART_POST',
            'U2-UPS 2ND DAY': '02',
            'FE-UPS FREE 2 DAY SHIPPING': '02',
            'D3-UPS 3 DAY SELECT': '12',
            'U6-UPS 3RD PARTY': 'Ground',
            'U3-UPS 3RD PARTY': 'Ground',
            'SC-2ND DAY AIR': '02',
            'U4-UPS COLLECT': 'Ground',
            'CG-UPS GROUND': '03',
            'SI-UPS GROUND': '03',
            'U5-UPS NEXT DAY SAVER': '13',
            'UPS NEXT DAY SAVER': '13',
            'ND-UPS NEXT DAY AM': '01',
            'SC-UPS 2ND DAY AIR': '02',
            'UPS SUREPOST': '93',
            'CP-UPS GROUND': '03',
            'PP-UPS SUREPOST': '93',
            'SA-2ND DAY AIR': '02',
            'UPS 2ND DAY AIR': '02',
            '03-UPS GROUND': '03',
            'FEDEX_2_DAY_AM': 'FEDEX_2_DAY_AM'
        }

        for seg in self.formatted_segments:
            if seg[0] == "ISA":
                global isa
                isa = seg[13].lstrip('0')
            if seg[0] == "W05":
                global despositor_order_number
                # Generating static XML elements.
                root = et.Element('Order')
                order_header_tag = et.SubElement(root, 'OrderHeader')
                facility_tag = et.SubElement(order_header_tag, 'Facility')
                client_tag = et.SubElement(order_header_tag, 'Client')
                client_tag.text = self.client_id
                depositor_order_number_tag = et.SubElement(order_header_tag, 'DepositorOrderNumber')
                order_status_tag = et.SubElement(order_header_tag, 'OrderStatus')
                order_status_tag.text = 'New'
                purchase_order_number_tag = et.SubElement(order_header_tag, 'PurchaseOrderNumber')
                master_reference_number_tag = et.SubElement(order_header_tag, 'MasterReferenceNumber')
                bill_to_tag = et.SubElement(order_header_tag, 'BillTo')
                bill_to_name_tag = et.SubElement(bill_to_tag, 'Name')
                bill_to_code_tag = et.SubElement(bill_to_tag, 'Code')
                bill_to_address1_tag = et.SubElement(bill_to_tag, 'Address1')
                bill_to_city_tag = et.SubElement(bill_to_tag, 'City')
                bill_to_state_tag = et.SubElement(bill_to_tag, 'State')
                bill_to_zip_code_tag = et.SubElement(bill_to_tag, 'ZipCode')
                bill_to_country_tag = et.SubElement(bill_to_tag, 'Country')
                bill_to_contact_name_tag = et.SubElement(bill_to_tag, 'ContactName')
                ship_to_tag = et.SubElement(order_header_tag, 'ShipTo')
                ship_to_name_tag = et.SubElement(ship_to_tag, 'Name')
                ship_to_code_tag = et.SubElement(ship_to_tag, 'Code')
                ship_to_address1_tag = et.SubElement(ship_to_tag, 'Address1')
                ship_to_address2_tag = et.SubElement(ship_to_tag, 'Address2')
                ship_to_city_tag = et.SubElement(ship_to_tag, 'City')
                ship_to_state_tag = et.SubElement(ship_to_tag, 'State')
                ship_to_zip_code_tag = et.SubElement(ship_to_tag, 'ZipCode')
                ship_to_country_tag = et.SubElement(ship_to_tag, 'Country')
                ship_to_contact_name_tag = et.SubElement(ship_to_tag, 'ContactName')
                ship_to_contact_email_tag = et.SubElement(ship_to_tag, 'ContactEmail')
                ship_to_contact_phone_tag = et.SubElement(ship_to_tag, 'ContactPhone')
                mark_for_tag = et.SubElement(order_header_tag, 'MarkFor')
                mark_for_name = et.SubElement(mark_for_tag, 'Name')
                mark_for_code = et.SubElement(mark_for_tag, 'Code')
                mark_for_address1_tag = et.SubElement(mark_for_tag, 'Address1')
                mark_for_city_tag = et.SubElement(mark_for_tag, 'City')
                mark_for_state_tag = et.SubElement(mark_for_tag, 'State')
                mark_for_zip_code_tag = et.SubElement(mark_for_tag, 'ZipCode')
                mark_for_country_tag = et.SubElement(mark_for_tag, 'Country')
                dates_tag = et.SubElement(order_header_tag, 'Dates')
                purchase_order_date_tag = et.SubElement(dates_tag, 'PurchaseOrderDate')
                requested_ship_date_tag = et.SubElement(dates_tag, 'RequestedShipDate')
                cancel_date_tag = et.SubElement(dates_tag, 'CancelDate')
                ship_not_before_date_tag = et.SubElement(dates_tag, 'ShipNotBeforeDate')
                reference_information_tag = et.SubElement(order_header_tag, 'ReferenceInformation')
                customer_name_tag = et.SubElement(reference_information_tag, 'CustomerName')
                client_id_tag = et.SubElement(reference_information_tag, 'ClientID')
                vendor_number_tag = et.SubElement(reference_information_tag, 'VendorNumber')
                account_number_tag = et.SubElement(reference_information_tag, 'AccountNumber')
                department_tag = et.SubElement(reference_information_tag, 'Department')
                e50_tag = et.SubElement(reference_information_tag, 'E50')
                e51_tag = et.SubElement(reference_information_tag, 'E51')
                e52_tag = et.SubElement(reference_information_tag, 'E52')
                messages_tag = et.SubElement(order_header_tag, 'Messages')
                warehouse_instructions_tag = et.SubElement(messages_tag, 'WarehouseInstructions')
                shipping_instructions_tag = et.SubElement(order_header_tag, 'ShippingInstructions')
                shipment_method_of_payment_tag = et.SubElement(shipping_instructions_tag, 'ShipmentMethodOfPayment')
                transportation_method_tag = et.SubElement(shipping_instructions_tag, 'TransportationMethod')
                carrier_code_tag = et.SubElement(shipping_instructions_tag, 'CarrierCode')
                routing_tag = et.SubElement(shipping_instructions_tag, 'Routing')
                e53_tag = et.SubElement(shipping_instructions_tag, 'E53')
                order_detail_tag = et.SubElement(root, 'OrderDetail')
                depositor_order_number_tag.text = seg[2]
                despositor_order_number = seg[2]
                purchase_order_number_tag.text = seg[3].replace("'", "")

            # Parsing and Mapping data

            if seg[0] == "N1" and seg[1] == "WH":
                lot_number = seg[4]
            if seg[0] == "N1" and seg[1] == "SF":
                facility_tag.text = seg[4]
            if seg[0] == "N1" and seg[1] == "ST":
                identifier = 1
                ship_to_name_tag.text = seg[2].replace("'", '')
                ship_to_code_tag.text = seg[4]
                ship_to_contact_name_tag.text = seg[2].replace("'", '')
            if seg[0] == "N3" and identifier == 1:
                ship_to_address1_tag.text = seg[1].replace("'", '')

                # Checking to see if Address2 line exists, skips if it doesnt.
                try:
                    ship_to_address2_tag.text = seg[2]
                except IndexError:
                    pass
            if seg[0] == "N4" and identifier == 1:
                ship_to_city_tag.text = seg[1].replace("'", '')
                ship_to_state_tag.text = seg[2]
                ship_to_zip_code_tag.text = seg[3]
                ship_to_country_tag.text = seg[4]
            if seg[0] == "PER":
                try:
                    ship_to_contact_email_tag.text = seg[6].lstrip('0')
                except IndexError:
                    pass
                try:
                    ship_to_contact_phone_tag.text = seg[4]
                except IndexError:
                    ship_to_contact_phone_tag.text = "555-555-5555"
            if seg[0] == "N1" and seg[1] == "OB":
                # Identifier variable is to group each possible variation of  N1 - N4 segments to their type
                identifier = 0
                bill_to_name_tag.text = seg[2].strip("'")
                bill_to_contact_name_tag.text = seg[2].replace("'", '')
                bill_to_code_tag.text = seg[4]
                global customer_name
                customer_name_tag.text = seg[4]
                customer_name = seg[4]
                client_id_tag.text = seg[2]
            if seg[0] == "N3" and identifier == 0:
                bill_to_address1_tag.text = seg[1].replace("'", '')
            if seg[0] == "N4" and identifier == 0:
                bill_to_city_tag.text = seg[1].replace("'", '')
                bill_to_state_tag.text = seg[2]
                bill_to_zip_code_tag.text = seg[3]
                bill_to_country_tag.text = 'US'
            if seg[0] == "N1" and seg[1] == "WH":
                e51_tag.text = seg[2] + '_' + seg[3] + '_' + seg[4]
            if seg[0] == "N1" and seg[1] == "Z7":
                identifier = 2
                mark_for_name.text = seg[2]
                mark_for_code.text = seg[4]
            if seg[0] == "N3" and identifier == 2:
                mark_for_address1_tag.text = seg[1].replace("'", '')
            if seg[0] == "N4" and identifier == 2:
                mark_for_city_tag.text = seg[1].replace("'", '')
                mark_for_state_tag.text = seg[2]
                mark_for_zip_code_tag.text = seg[3]
                mark_for_country_tag.text = 'US'
            if seg[0] == "N9" and seg[1] == "DP":
                department_tag.text = seg[2]
                e50_tag.text = seg[3]
            if seg[0] == "N9" and seg[1] == "AI":
                vendor_number_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "DX":
                e50_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "4F":
                account_number_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "XY":
                master_reference_number_tag.text = seg[2]
            if seg[0] == "G62" and seg[1] == "04":
                purchase_order_date = seg[2]
                purchase_order_date = '-'.join(
                    [purchase_order_date[:4], purchase_order_date[4:6], purchase_order_date[6:]])
                purchase_order_date_tag.text = purchase_order_date
            if seg[0] == "G62" and seg[1] == "01":
                cancel_date = seg[2]
                cancel_date = '-'.join([cancel_date[:4], cancel_date[4:6], cancel_date[6:]])
                cancel_date_tag.text = cancel_date
            if seg[0] == "G62" and seg[1] == "02":
                requested_ship_date = seg[2]
                requested_ship_date = '-'.join(
                    [requested_ship_date[:4], requested_ship_date[4:6], requested_ship_date[6:]])
                requested_ship_date_tag.text = requested_ship_date
                ship_not_before_date = seg[2]
                ship_not_before_date = '-'.join(
                    [ship_not_before_date[:4], ship_not_before_date[4:6], ship_not_before_date[6:]])
                ship_not_before_date_tag.text = ship_not_before_date
            if seg[0] == "NTE":
                nte_line.append(str(seg[2]).replace("'", ""))
            if seg[0] == "W66":

                # joining all NTE segments and applying it to the warhouse_instructions tag with a limit of 410 characters
                nte_full_line = ' '.join(nte_line)

                warehouse_instructions_tag.text = nte_full_line[:410]

                # Clearing nte_line for next iteration
                nte_line = []
                shipment_method_of_payment_tag.text = seg[1]
                transportation_method_tag.text = seg[2]
                carrier_code_tag.text = seg[10]
                e52_tag.text = seg[10]
                e53_tag.text = seg[5]
                routing_tag.text = carriers.get(seg[5])
                if routing_tag.text == None:
                    routing_tag.text = 'ROUT'
            if seg[0] == "W01":
                order_line_tag = et.SubElement(order_detail_tag, 'OrderLine')
                order_line_number_tag = et.SubElement(order_line_tag, 'OrderLineNumber')
                item_number_tag = et.SubElement(order_line_tag, 'ItemNumber')
                item_upc_tag = et.SubElement(order_line_tag, 'ItemUPC')
                buyer_item_number_tag = et.SubElement(order_line_tag, 'BuyerItemNumber')
                ordered_quantity_tag = et.SubElement(order_line_tag, 'OrderedQuantity')
                quantity_unit_of_measure_tag = et.SubElement(order_line_tag, 'QuantityUnitOfMeasure')
                item_description_tag = et.SubElement(order_line_tag, 'ItemDescription')
                lot_number_tag = et.SubElement(order_line_tag, 'LotNumber')
                lot_number_tag.text = lot_number
                size_tag = et.SubElement(order_line_tag, 'Size')
                style_tag = et.SubElement(order_line_tag, 'Style')
                style_tag.text = seg[5]
                color_tag = et.SubElement(order_line_tag, 'Color')
                pack_quantity_tag = et.SubElement(order_line_tag, 'PackQuantity')
                e57_tag = et.SubElement(order_line_tag, 'E57')
                e58_tag = et.SubElement(order_line_tag, 'E58')
                e59_tag = et.SubElement(order_line_tag, 'E59')
                e62_tag = et.SubElement(order_line_tag, 'E62')
                ordered_quantity_tag.text = seg[1]
                quantity_unit_of_measure_tag.text = seg[2]
                item_number_tag.text = seg[7]
                item_upc_tag.text = seg[7]
            if seg[0] == "G69":
                item_description_tag.text = seg[1].replace("'", '')
            if seg[0] == "N9" and seg[1] == "VN":
                buyer_item_number_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "VC":
                color_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "SZ":
                size_tag.text = seg[2]
            if seg[0] == "N9" and seg[1] == "LI":
                order_line_number_tag.text = seg[2]
            if seg[0] == "W20":
                pack_quantity_tag.text = seg[1]
            if seg[0] == "AMT" and seg[1] == "D340":
                e57_tag.text = seg[2]
            if seg[0] == "AMT" and seg[1] == "G821":
                e58_tag.text = seg[2]
            if seg[0] == "AMT" and seg[1] == "H850":
                e59_tag.text = seg[2]
            if seg[0] == "AMT" and seg[1] == "ZZZZ":
                e62_tag.text = seg[2]
            if seg[0] == "SE":
                tree = et.ElementTree(root)
                et.indent(tree, space="\t", level=0)
                tree.write(self.mantis_import_path + self.transaction_number + "_" + self.client_id + "_" +
                           str(depositor_order_number_tag.text) + "_" + str(isa) + "_" + str(customer_name_tag.text) +
                           "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml", encoding="UTF-8",
                           xml_declaration=True)
                tree.write(self.path + "Out\\Archive\\" + self.transaction_number + "\\" + self.transaction_number + "_"
                           + self.client_id + "_" + str(depositor_order_number_tag.text) + "_" + str(isa) + "_" +
                           str(customer_name_tag.text) + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml",
                           encoding="UTF-8", xml_declaration=True)
