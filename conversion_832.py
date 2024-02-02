import xml.etree.ElementTree as et
from datetime import datetime


class Convert_832:

    def __init__(self, formatted_segments, path, mantis_import_path, transaction_number, client_id, facility):
        self.formatted_segments = formatted_segments
        self.path = path
        self.mantis_import_path = mantis_import_path
        self.transaction_number = transaction_number
        self.client_id = client_id
        self.facility = facility

    def parse_edi(self):

        # Generate XML and build XML structure for static one time tags and values.
        root = et.Element('ItemMaintenance')
        item_maintenance_header_tag = et.SubElement(root, 'ItemMaintenanceHeader')
        facility_tag = et.SubElement(item_maintenance_header_tag, 'Facility')
        facility_tag.text = self.facility
        client_tag = et.SubElement(item_maintenance_header_tag, 'Client')
        client_tag.text = self.client_id
        maintenance_type_tag = et.SubElement(item_maintenance_header_tag, 'MaintenanceType')
        maintenance_type_tag.text = 'Add'
        effective_date_tag = et.SubElement(item_maintenance_header_tag, 'EffectiveDate')
        effective_date_tag.text = datetime.now().strftime("%Y%m%d%H%M%S")
        item_maintenance_detail_tag = et.SubElement(root, 'ItemMaintenanceDetail')
        # Formatting EDI into a nested array

        for seg in self.formatted_segments:
            if seg[0] == 'ISA':
                unique_identifier = seg[13]
            if seg[0] == 'LIN':
                item_header_tag = et.SubElement(item_maintenance_detail_tag, 'Item')
                item_number_tag = et.SubElement(item_header_tag, 'ItemNumber')
                item_number_tag.text = seg[5]
                item_upc_tag = et.SubElement(item_header_tag, 'ItemUPC')
                item_upc_tag.text = seg[5]
                style_tag = et.SubElement(item_header_tag, 'Style')
                style_tag.text = seg[3]
                color_tag = et.SubElement(item_header_tag, 'Color')
                size_tag = et.SubElement(item_header_tag, 'Size')
                size_tag.text = seg[9]
                item_description_tag = et.SubElement(item_header_tag, 'ItemDescription')
                product_group_tag = et.SubElement(item_header_tag, 'ProductGroup')
                product_group_tag.text = seg[3]
                dimension_unit_of_measure_tag = et.SubElement(item_header_tag, 'DimensionUnitOfMeasure')
                dimension_unit_of_measure_tag.text = 'IN'
                pack_quantity_tag = et.SubElement(item_header_tag, 'PackQuantity')
                pack_size_unit_of_measure_tag = et.SubElement(item_header_tag, 'PackSizeUnitOfMeasure')
                pack_size_unit_of_measure_tag.text = 'EA'
            if seg[0] == 'PID' and seg[2] == '73':
                color_tag.text = seg[5]
            if seg[0] == 'PID' and seg[2] == '74':
                size_tag.text = seg[5]
                item_description_tag.text = style_tag.text + '-' + color_tag.text + '-' + size_tag.text
            if seg[0] == 'PID' and seg[2] == 'DM':
                item_number = item_number + "-" + seg[5]
                item_number_tag.text = str(item_number).replace('\n', '')
            if seg[0] == 'G55':
                pack_quantity_tag.text = seg[13]


        # Generating File after loop
        tree = et.ElementTree(root)
        et.indent(tree, space="\t", level=0)
        tree.write(
            self.mantis_import_path + self.transaction_number + "_" + self.client_id + "_" + datetime.now().strftime(
                "%Y%m%d%H%M%S") + "_" + str(unique_identifier) + ".xml", encoding="UTF-8", xml_declaration=True)
        tree.write(self.path + "Out\\Archive\\" + self.transaction_number + "\\" + self.transaction_number + "_"
                   + self.client_id + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(unique_identifier) +
                   ".xml", encoding="UTF-8", xml_declaration=True)
