import xml.etree.ElementTree as et
from datetime import datetime


class Convert_943:

    def __init__(self, formatted_segments, path, mantis_import_path, transaction_number, client_id, facility):
        self.formatted_segments = formatted_segments
        self.path = path
        self.mantis_import_path = mantis_import_path
        self.transaction_number = transaction_number
        self.client_id = client_id
        self.facility = facility

    def parse_edi(self):

        # Building XML Structure and defining static values
        for seg in self.formatted_segments:
            if seg[0] == 'W06':
                # Building XML Structure and defining static values
                root = et.Element('Transfer')
                transfer_header_tag = et.SubElement(root, 'TransferHeader')
                facility_tag = et.SubElement(transfer_header_tag, 'Facility')
                facility_tag.text = self.facility
                client_tag = et.SubElement(transfer_header_tag, 'Client')
                client_tag.text = self.client_id
                depositor_order_number_tag = et.SubElement(transfer_header_tag, 'DepositorOrderNumber')
                order_status_tag = et.SubElement(transfer_header_tag, 'OrderStatus')
                order_status_tag.text = 'New'
                shipment_id_tag = et.SubElement(transfer_header_tag, 'ShipmentID')
                purchase_order_number_tag = et.SubElement(transfer_header_tag, 'PurchaseOrderNumber')
                dates_tag = et.SubElement(transfer_header_tag, 'Dates')
                purchase_order_date_tag = et.SubElement(dates_tag, 'PurchaseOrderDate')
                estimated_delivery_date_tag = et.SubElement(dates_tag, 'EstimatedDeliveryDate')
                reference_information_tag = et.SubElement(transfer_header_tag, 'ReferenceInformation')
                bill_of_lading_number_tag = et.SubElement(reference_information_tag, 'BillOfLadingNumber')
                transportation_information_tag = et.SubElement(transfer_header_tag, 'TransportationInformation')
                transportation_method_tag = et.SubElement(transportation_information_tag, 'TransportationMethod')
                shipment_method_of_payment_tag = et.SubElement(transportation_information_tag,
                                                               'ShipmentMethodOfPayment')
                carrier_code_tag = et.SubElement(transportation_information_tag, 'CarrierCode')
                routing_tag = et.SubElement(transportation_information_tag, 'Routing')
                transfer_detail_tag = et.SubElement(root, 'TransferDetail')
                purchase_order_number_tag.text = seg[2]
                purchase_order_date_tag.text = seg[3]
                shipment_id_tag.text = seg[4]
            if seg[0] == 'G62':
                estimated_delivery_date_tag.text = seg[2]
            if seg[0] == 'W27':
                transportation_method_tag.text = seg[1]
                carrier_code_tag.text = seg[2]
                routing_tag.text = seg[3]
                try:
                    shipment_method_of_payment_tag.text = seg[4]
                except:
                    continue
            if seg[0] == 'N9' and seg[1] == 'BM':
                bill_of_lading_number_tag.text = seg[2]
            if seg[0] == 'W04':
                # Generating dynamic XML tags and assigning values
                item_tag = et.SubElement(transfer_detail_tag, 'Item')
                item_number_tag = et.SubElement(item_tag, 'ItemNumber')
                item_number_tag.text = seg[7]
                upc_tag = et.SubElement(item_tag, 'ItemUpc')
                upc_tag.text = seg[7]
                item_description_tag = et.SubElement(item_tag, 'ItemDescription')
                lot_number_tag = et.SubElement(item_tag, 'LotNumber')
                shipped_quantity_tag = et.SubElement(item_tag, 'ShippedQuantity')
                shipped_quantity_tag.text = seg[1]
                quantity_unit_of_measure_tag = et.SubElement(item_tag, 'QuantityUnitOfMeasure')
                quantity_unit_of_measure_tag.text = 'EA'
                item_purchase_order_number_tag = et.SubElement(item_tag, 'PurchaseOrderNumber')
                stock_po_number_tag = et.SubElement(item_tag, 'StockPONumber')
                order_line_number_tag = et.SubElement(item_tag, 'OrderLineNumber')
            if seg[0] == "N1" and seg[1] == "SF":
                facility_tag.text = seg[4]
            if seg[0] == 'G69':
                item_description_tag.text = seg[1]
            if seg[0] == 'N9' and seg[1] == 'ER':
                depositor_order_number_tag.text = seg[2]
            if seg[0] == 'N9' and seg[1] == 'PO':
                item_purchase_order_number_tag.text = seg[2]
                stock_po_number_tag.text = seg[2]
            if seg[0] == 'N9' and seg[1] == 'LI':
                order_line_number_tag.text = seg[2]
            if seg[0] == 'N9' and seg[1] == 'LT':
                if seg[2] == '02':
                    lot_number_tag.text = seg[2]
                else:
                    lot_number_tag.text = 'WH'
            if seg[0] == 'SE':
                # Generating File after loop
                tree = et.ElementTree(root)
                et.indent(tree, space="\t", level=0)
                tree.write(self.mantis_import_path + self.transaction_number + "_" + self.client_id + "_" + str(
                    depositor_order_number_tag.text).replace("/", "_") + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml", encoding="UTF-8", xml_declaration=True)
                tree.write(self.path + "Out\\Archive\\" + self.transaction_number + "\\" + self.transaction_number + "_"
                           + self.client_id + str(depositor_order_number_tag.text).replace("/", "_") + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml", encoding="UTF-8", xml_declaration=True)

