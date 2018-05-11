import fdfgen
import arcpy
import json
from PIL import Image
from pdfjinja import PdfJinja
import os


def get_layer(db, fc):
    return arcpy.MakeFeatureLayer_management(db + "\\" + fc, "temp_layer")


def get_domain_fields(layer):
    domains = []
    fields = arcpy.ListFields(layer)
    for field in fields:
        if field.domain:
            domains.append(field.baseName)
    return domains


def adjust_domain_structure(domains, object_data):
    for item in domains:
        if object_data[item]:
            value = object_data[item]
            object_data[item] = {}
            object_data[item][value] = True


def format_data_to_object(layer):
    path_to_json = "temp.json"
    arcpy.FeaturesToJSON_conversion(layer, path_to_json)
    return json.load(open(path_to_json))


def fill_out_form(data, domains, pdftemplate):
    pdfPath = os.path.dirname("gis_to_pdf_form.py")

    pdf_doc = arcpy.mapping.PDFDocumentCreate(pdfPath)
    for record in data['features']:
        record_pdf = "bob"
        pdf_doc.appendPages(record_pdf)


def process_each_record(data, domains, pdftemplate):
    for record in data:
        record_attributes = record["attributes"]
        adjust_domain_structure(domains, record_attributes)
        fill_out_form(record_attributes, domains, pdftemplate)


def main():
    db_connection = "C:\\Users\\jswagger\\Desktop\\Example.gdb"
    fc_name = "Example_Trees"
    pdf_template = "C:\\Users\\jswagger\\Desktop\\example_template.pdf"
    layer = get_layer(db_connection, fc_name)
    domains = get_domain_fields(layer)
    object_data = format_data_to_object(layer)
    process_each_record(object_data["features"], domains, pdf_template)


if __name__ == '__main__':
    main()
