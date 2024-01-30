import os
import xml.etree.ElementTree as et
from datetime import date, datetime
import psycopg2


# Database settings
connection = psycopg2.connect(
    host='localhost',
    database='sequencer',
    user='Admin',
    password='@Dm1n'
)

class Convert_945:

    def __init__(self, XML):
        self.XML = XML

    def parse_edi(self):
        # Load in the edi file based on function that checks directory of file out of Class structure

        raw_file = self.XML

        ## Load in the XML based on function that checks directory of file out of Class structure
        oak = et.parse(self.XML)
        rooted = oak.getroot()
        counter = 0
        header_string = ''
        body_string = ''
        body_header_string = ''
        segment_count = 0
        bill_of_lading_number = ''
        skip = True
        box_weight = ''
        shipment_weight_present = False
        total_shipment_weight = 0

        carriers = {
            'Ground': '03',
            'Next Day Air Saver': '13',
            '2nd Day Air': '02',
            '3 Day Select': '12',
            'Next Day Air': '01',
            'Worldwide Express': '07',
            'Standard': '11',
            'SurePost 1LB or greater': '93',
            'SurePost Media Mail': '95',
            'SurePost Less than 1LB': '92',
            'Worldwide Saver': '65'
        }

        if counter == 0:
            for element in rooted.iter():
                if element.tag == 'ShipmentDetail':
                    for ShipmentDetail_child_element in element:
                        if ShipmentDetail_child_element.tag == 'Container':
                            for Container_sub_element in ShipmentDetail_child_element:
                                if Container_sub_element.tag == 'TrackingNumber':
                                    if Container_sub_element.text is None:
                                        skip = False
        for element in rooted.iter():
            if element.tag == 'ShipmentHeader':
                for ReceiptHeader_child_element in element:
                    if ReceiptHeader_child_element.tag == 'ShipmentID':
                        shipment_id = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'DepositorOrderNumber':
                        depositor_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PurchaseOrderNumber':
                        purchase_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'MasterReferenceNumber':
                        master_reference_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalQuantityShipped':
                        total_quantity_shipped = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentWeight':
                        total_shipment_weight = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PackWeightUnitOfMeasure':
                        header_pack_weight_unit_of_measure = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentVolume':
                        total_shipment_volume = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'VolumeUnitOfMeasure':
                        volume_unit_of_measure = ReceiptHeader_child_element.text
            if element.tag == 'ShipTo':
                for ShipTo_child_element in element:
                    if ShipTo_child_element.tag == 'Name':
                        ship_to_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Code':
                        ship_to_code = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address1':
                        ship_to_address1 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address2':
                        ship_to_address2 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'City':
                        ship_to_city = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'State':
                        ship_to_state = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ZipCode':
                        ship_to_zipcode = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Country':
                        ship_to_country = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactName':
                        ship_to_contact_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactPhone':
                        ship_to_contact_phone = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactEmail':
                        ship_to_contact_email = ShipTo_child_element.text
            if element.tag == 'MarkFor':
                for ShipTo_child_element in element:
                    if ShipTo_child_element.tag == 'Name':
                        mark_for_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Code':
                        mark_for_code = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address1':
                        mark_for_address1 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address2':
                        mark_for_address2 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'City':
                        mark_for_city = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'State':
                        mark_for_state = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ZipCode':
                        mark_for_zipcode = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Country':
                        mark_for_country = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactName':
                        mark_for_contact_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactPhone':
                        mark_for_contact_phone = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactEmail':
                        mark_for_contact_email = ShipTo_child_element.text
            if element.tag == 'Dates':
                for Dates_child_element in element:
                    if Dates_child_element.tag == 'PurchaseOrderDate':
                        purchase_order_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ShipDate':
                        ship_date = Dates_child_element.text.replace('-', '')
                    elif Dates_child_element.tag == 'EstimatedDeliveryDate':
                        estimated_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ScheduledDeliveryDate':
                        scheduled_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'PickupDate':
                        pick_up_date = Dates_child_element.text
            if element.tag == 'ReferenceInformation':
                for ReferenceInformation_child_element in element:
                    if ReferenceInformation_child_element.tag == 'BillOfLadingNumber' and skip is False:
                        bill_of_lading_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ProbillNumber':
                        probill_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ContainerNumber':
                        waybill_holding = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'SealNumber':
                        seal_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ReferenceNumber':
                        reference_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'LoadNumber':
                        load_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'FreightCharges':
                        if ReferenceInformation_child_element.text is None:
                            freight_charge = '0'
                        else:
                            freight_charge = ReferenceInformation_child_element.text
                            freight_charge = freight_charge.replace(",", "")
                    elif ReferenceInformation_child_element.tag == 'E52':
                        if ReferenceInformation_child_element.text == 'ROUT':
                            majors_order = 1
                        else:
                            majors_order = 0
                            carrier_code = ReferenceInformation_child_element.text
            if element.tag == 'TransportationInformation':
                carrier_code_majors = ''
                routing_majors = ''
                for TransporationInformation_child_element in element:
                    if TransporationInformation_child_element.tag == 'ShipmentMethodOfPayment':
                        if TransporationInformation_child_element.text is None:
                            shipment_method_of_payment = 'CC'
                        else:
                            shipment_method_of_payment = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'CarrierCode':
                        carrier_code_majors = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'Routing':
                        routing_majors = TransporationInformation_child_element.text
                        if TransporationInformation_child_element.text in carriers:
                            routing_majors = carriers.get(TransporationInformation_child_element.text) + '-' + TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'SpecialHandlingCode':
                        special_handling_code = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'E53':
                        routing = TransporationInformation_child_element.text
                    if majors_order == 1:
                        carrier_code = carrier_code_majors
                        routing = routing_majors

        cursor = connection.cursor()
        cursor.execute("SELECT sequence_number FROM public.sequence where client='Roxy'")
        data = cursor.fetchone()
        sequence_number = int(data[0]) + 1
        cursor.execute("update sequence set sequence_number =" + str(sequence_number) + " where client='Roxy'")
        connection.commit()
        header_string = 'ISA*00*          *00*          *ZZ*GPALOGISTICS   *ZZ*BWGROXYPROD    *' + datetime.now().strftime("%y%m%d") + '*' + datetime.now().strftime("%H%M") + '*X*00401*' + str(sequence_number) + '*0*P*>~' \
                        'GS*SW*GPALOGISTICS*BWGROXYPROD*' + datetime.now().strftime("%Y%m%d") + '*' + datetime.now().strftime("%H%M") + '*' + str(sequence_number)[-4:] + '*X*004010~' \
                        'ST*945*1001~' \
                        'W06*N*' + depositor_order_number + '*' + ship_date + '*' + bill_of_lading_number + '*' + probill_number + '*' + purchase_order_number + '~' \
                        'N1*ST*' + ship_to_name + '*92*' + ship_to_code.replace("!", "") + '~' \
                        'N3*' + ship_to_address1 + '~' \
                        'N4*' + ship_to_city + '*' + ship_to_state + '*' + ship_to_zipcode + '*' + ship_to_country + '~' \
                        'N9*AO*' + load_number + '~'  \
                        'G62*10*' + ship_date + '~' \
                        'W27*LT*' + carrier_code + '*' + routing + '*' + shipment_method_of_payment + '*~' \
                        'G72*ITA*15******' + freight_charge.replace(".", "") + '~'
        for element in rooted.iter():
            if element.tag == 'ShipmentDetail':
                for ShipmentDetail_child_element in element:
                    if ShipmentDetail_child_element.tag == 'Container':
                        counter = counter + 1
                        style = ''
                        color = ''
                        size = ''
                        for Container_sub_element in ShipmentDetail_child_element:
                            if Container_sub_element.tag == 'SSCC':
                                sscc = Container_sub_element.text
                                if len(sscc) != 20:
                                    raise Exception("This UCC is invalid as it does not meet the 20 character requirement.")
                            if Container_sub_element.tag == 'TrackingNumber':
                                if Container_sub_element.text is None:
                                    tracking_number = ''
                                else:
                                    tracking_number = Container_sub_element.text
                            if Container_sub_element.tag == 'BoxWeight':
                                box_weight = Container_sub_element.text
                                if box_weight == None:
                                    pass
                                else:
                                    body_header_string = 'LX*' + str(counter) + '~' \
                                                         'PO4******' + str(box_weight) + '*LB*' + '~' \
                                                         'MAN*GM*' + str(sscc) + '**CP*' + tracking_number + '~'
                                    header_string = header_string + body_header_string
                                    segment_count = segment_count + 3
                                    if shipment_weight_present is False:
                                        total_shipment_weight = float(total_shipment_weight) + float(box_weight)
                            if Container_sub_element.tag == 'CaseWeight' and box_weight == None:
                                case_weight = Container_sub_element.text
                                body_header_string = 'LX*' + str(counter) + '~' \
                                                     'PO4******' + str(case_weight) + '*LB*' + '~' \
                                                     'MAN*GM*' + str(sscc) + '**CP*' + tracking_number + '~'
                                header_string = header_string + body_header_string
                                segment_count = segment_count + 3
                                if shipment_weight_present is False:
                                    total_shipment_weight = float(total_shipment_weight) + float(case_weight)
                            if Container_sub_element.tag == 'Item':
                                ordered_quantity = ''
                                shipped_quantity = ''
                                case_upc = ''
                                for Item_sub_element in Container_sub_element:
                                    if Item_sub_element.tag == 'OrderLineNumber':
                                        order_line_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'OrderedQuantity':
                                        ordered_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemNumber':
                                        item_number = Item_sub_element.text
                                        split = item_number.split("-")
                                        style = split[0]
                                    elif Item_sub_element.tag == 'ItemUPC':
                                        item_upc = Item_sub_element.text
                                    elif Item_sub_element.tag == 'CaseUPC':
                                        case_upc = Item_sub_element.text
                                    elif Item_sub_element.tag == 'GTIN':
                                        gtin = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ReceivedQuantity':
                                        received_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ShippedQuantity':
                                        shipped_quantity = Item_sub_element.text
                                        if "." in shipped_quantity:
                                            print("caught")
                                    elif Item_sub_element.tag == 'QuantityUnitOfMeasure':
                                        quantity_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemDescription':
                                       item_description = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ProductGroup':
                                        product_group = Item_sub_element.text
                                    elif Item_sub_element.tag == 'AlternateItemNumber':
                                        alternate_item_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'LotNumber':
                                        lot_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'SKU':
                                        sku = Item_sub_element.text
                                    elif Item_sub_element.tag == 'Color':
                                        color = Item_sub_element.text
                                    elif Item_sub_element.tag == 'Size':
                                        size = Item_sub_element.text
                                    elif Item_sub_element.tag == 'E57':
                                        label_code = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ProductType':
                                        product_type = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemLength':
                                        item_length = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemWidth':
                                        item_width = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemHeight':
                                        item_height = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackQuantity':
                                        pack_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'InnerPackQuantity':
                                        inner_pack_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackSize':
                                        pack_size = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackSizeUnitOfMeasure':
                                        pack_size_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackWeight':
                                        pack_weight = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackWeightUnitOfMeasure':
                                        detail_pack_weight_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PurchaseOrderNumber':
                                        detail_purchase_order_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackVolume':
                                        pack_volume = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackVolumeUnitOfMeasure':
                                        pack_volume_unit_of_measure = Item_sub_element.text
                        # Generating dynamic values.
                                    body_string = 'W12*CC*' + str(ordered_quantity) + '*' + str(shipped_quantity) + '**EA**UP*' + str(case_upc) + '*********' + str(color) + '****' + str(size) + '~' \
                                                  'N9*LI*' + str(order_line_number) + '~'
                                segment_count = segment_count + 2
                                header_string = header_string + body_string
        if total_shipment_weight == 0:
            raise Exception("This order has no total shipment weight")
        segment_count = segment_count + 11
        footer_string = 'W03*' + str(total_quantity_shipped) + '*' + str(total_shipment_weight) + '*LB*1*CF~' \
                        'SE*' + str(segment_count) + '*1001~' \
                        'GE*1*' + str(sequence_number)[-4:] + '~' \
                        'IEA*1*' + str(sequence_number) +'~'
        completed_string = header_string + footer_string
        with open("C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\Out\\945_88_" + str(sequence_number) + "_" +
                  datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)
        with open("C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\Out\\Archive\\945\\945_88_" + str(sequence_number) + "_" +
                  datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)
