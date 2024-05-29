import logging.handlers
import os

from conversion_832 import *
from conversion_940 import *
from conversion_943 import *
from conversion_944 import *
from conversion_945 import *
from conversion_997 import *
from notifications import *


# Database settings
connection = psycopg2.connect(
    host='localhost',
    database='sequencer',
    user='Admin',
    password='@Dm1n'
)

# Pulling environment information from database
cursor = connection.cursor()
cursor.execute("SELECT environment_path, mantis_path FROM public.settings")
data = cursor.fetchone()
environment = data[0]
mantis_path = data[1]


client_root_dir = "WN1-Roxy\\"
client_id = "88"
facility = "WN1"
path = environment + client_root_dir
mantis_import_path = mantis_path
files = os.listdir(path + "In\\")


def main():
    for file in files:
        filename = str(file).split("_")
        rem_extension = file.split(".")
        try:
            if rem_extension[1] == "xml":
               pass
            else:
                with open(str(path + "\\In\\" + file), 'r', errors="ignore") as edi_file:
                    lines = edi_file.readlines()
                    unformatted_segments = []
                    for line in lines:
                        segment = line.split('~')
                        for individual_segment in segment:
                            elements = individual_segment.split('*')
                            unformatted_segments.append(elements)
                    formatted_segments = [x for x in unformatted_segments if x != ['\n']]
            try:
                if filename[1] == "832":
                    conversion = Convert_832(formatted_segments, path, mantis_import_path, filename[1], client_id, facility)
                    conversion.parse_edi()
                    conversion_997 = Convert_997(formatted_segments, path, mantis_import_path, filename[1], client_id, facility, connection)
                    conversion_997.produce_997()
                    os.replace(path + "In\\" + file, path + "In\\Archive\\" + filename[1] + "\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[1] == "940":
                    conversion = Convert_940(formatted_segments, path, mantis_import_path, filename[1], client_id, facility)
                    conversion.parse_edi()
                    conversion_997 = Convert_997(formatted_segments, path, mantis_import_path, filename[1], client_id, facility, connection)
                    conversion_997.produce_997()
                    send_email = create_notification_940(formatted_segments)
                    send_email.parse_edi_email()
                    os.replace(path + "In\\" + file, path + "In\\Archive\\" + filename[1] + "\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[1] == "943":
                    conversion = Convert_943(formatted_segments, path, mantis_import_path, filename[1], client_id, facility)
                    conversion.parse_edi()
                    conversion_997 = Convert_997(formatted_segments, path, mantis_import_path, filename[1], client_id, facility, connection)
                    conversion_997.produce_997()
                    # send_email = create_notification_943(formatted_segments)
                    # send_email.parse_edi_email()
                    os.replace(path + "In\\" + file, path + "In\\Archive\\" + filename[1] + "\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[0] == "944":
                    conversion = Convert_944(path + "In\\" + file, path, mantis_import_path, filename[0], client_id, connection)
                    conversion.parse_xml()
                    os.replace(path + "In\\" + file, path + "In\\Archive\\" + filename[0] + "\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml")
                if filename[0] == "945":
                    conversion = Convert_945(path + "In\\" + file, path, mantis_import_path, filename[0], client_id, connection)
                    conversion.parse_xml()
                    os.replace(path + "In\\" + file, path + "In\\Archive\\" + filename[0] + "\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml")

            except BaseException:
                logger = logging.getLogger()
                fileHandler = logging.FileHandler(
                    path + "Logs\\" + file + ".log")
                get_client_name = str(client_root_dir).split("-")
                client_name = str(get_client_name[1]).split("\\")
                server = str(path).split("\\")
                smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.office365.com", 587),
                                                            fromaddr="noreply@gpalogisticsgroup.com",
                                                            toaddrs=["cmaya@gpalogisticsgroup.com", "gpaops20@gpalogisticsgroup.com", "reyna.diaz@gpalogisticsgroup.com", "gpaops18@gpalogisticsgroup.com"],
                                                            subject=str(client_name[0]) + "-" + server[4] + ": " + file + " Failed to process.",
                                                            credentials=('noreply@gpalogisticsgroup.com', 'Turn*17300'),
                                                            secure=())
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                fileHandler.setFormatter(formatter)
                logger.addHandler(fileHandler)
                logger.addHandler(smtp_handler)
                logger.exception("An exception was triggered")
                os.replace(path + "In\\" + file, path + "In\\err_" + file)
        except IndexError:
            pass
        except PermissionError:
            pass


if __name__ == '__main__':
    main()
