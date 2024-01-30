import logging
import logging.handlers
from datetime import date, datetime

from conversion_832 import *
from conversion_940 import *
from conversion_943 import *
from conversion_944 import *
from conversion_945 import *
from conversion_997 import *

path = "C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\In\\"
files = os.listdir(path)


def main():
    for file in files:
        filename = str(file).split("_")
        rem_extension = file.split(".")
        try:
            if rem_extension[1] == "xml":
               pass
            else:
                with open(str(path + file), 'r', errors="ignore") as edi_file:
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
                    conversion = Convert_832(formatted_segments)
                    conversion.parse_edi(formatted_segments)
                    conversion_997 = Convert_997(formatted_segments, filename[0])
                    conversion_997.produce_997(formatted_segments, filename[0])
                    os.replace(path + file, path + "Archive\\832\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[1] == "940":
                    conversion = Convert_940(formatted_segments)
                    conversion.parse_edi(formatted_segments)
                    conversion_997 = Convert_997(formatted_segments, filename[0])
                    conversion_997.produce_997(formatted_segments, filename[0])
                    os.replace(path + file, path + "Archive\\940\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[1] == "943":
                    conversion = Convert_943(formatted_segments)
                    conversion.parse_edi(formatted_segments)
                    conversion_997 = Convert_997(formatted_segments, filename[0])
                    conversion_997.produce_997(formatted_segments, filename[0])
                    os.replace(path + file, path + "Archive\\943\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt")
                if filename[0] == "944":
                    conversion = Convert_944(path + file)
                    conversion.parse_edi()
                    os.replace(path + file, path + "Archive\\944\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml")
                if filename[0] == "945":
                    conversion = Convert_945(path + file)
                    conversion.parse_edi()
                    os.replace(path + file, path + "Archive\\945\\" + rem_extension[0] + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml")
            except BaseException:
                logger = logging.getLogger()
                fileHandler = logging.FileHandler(
                    "C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\Logs\\" + filename[0] + "_" + filename[1] + "_" + datetime.now().strftime("%Y%m%d") + ".log")
                smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.office365.com", 587),
                                                            fromaddr="noreply@gpalogisticsgroup.com",
                                                            toaddrs=["cmaya@gpalogisticsgroup.com", "michael.garcia@gpalogisticsgroup.com", "gpaops20@gpalogisticsgroup.com", "reyna.diaz@gpalogisticsgroup.com"],
                                                            subject=filename[0] + " failed to process for client " + filename[1],
                                                            credentials=('noreply@gpalogisticsgroup.com', 'Turn*17300'),
                                                            secure=())
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                fileHandler.setFormatter(formatter)
                logger.addHandler(fileHandler)
                logger.addHandler(smtp_handler)
                logger.exception("An exception was triggered")
                os.replace(path + file, path + "\\err_" + file)
        except IndexError:
            pass
        except PermissionError:
            pass


if __name__ == '__main__':
    main()

