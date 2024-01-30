from datetime import date, datetime
import sys
import psycopg2


class Convert_997:

    def __init__(self, formatted_segments, transaction_number):
        self.formatted_segments = formatted_segments
        self.transaction_number = transaction_number

    def produce_997(self, formatted_segments, transaction_number):
        # Load in the edi file based on function that checks directory of file out of Class structure

        counter = 1000
        count = 0
        # Database settings
        connection = psycopg2.connect(
            host='localhost',
            database='sequencer',
            user='Admin',
            password='@Dm1n'
        )

        # Pulling control number from database
        cursor = connection.cursor()
        cursor.execute("SELECT sequence_number FROM public.sequence where client='Roxy'")
        data = cursor.fetchone()
        sequence_number = int(data[0]) + 1
        cursor.execute("update sequence set sequence_number =" + str(sequence_number) + " where client='Roxy'")
        connection.commit()

        # Generating values for 997
        header_string = 'ISA*00*          *00*          *ZZ*GPALOGISTICS   *ZZ*BWGROXYPROD    *' + datetime.now().strftime("%y%m%d") + '*' + datetime.now().strftime("%H%M") + '*X*00401*' + str(sequence_number) + '*0*P*>~' \
                        'GS*FA*GPALOGISTICS*BWGROXYPROD*' + datetime.now().strftime("%Y%m%d") + '*' + datetime.now().strftime("%H%M") + '*' + str(sequence_number)[-4:] + '*U*004010~'

        for seg in formatted_segments:
            if seg[0] == 'GS':
                AK101 = seg[1]
                AK102 = seg[6]
            if seg[0] == 'ST':
                counter = counter + 1
                count = count + 1
                AK202 = seg[2]
                string = 'ST*997*' + str(counter) + '~' \
                         'AK1*' + AK101 + '*' + AK102 + '~' \
                         'AK2*' + transaction_number + '*' + AK202 + '~' \
                         'AK5*A~' \
                         'AK9*A*1*1*1~' \
                         'SE*6*' + str(counter) + '~'
                header_string = header_string + string
        footer_string = 'GE*' + str(count) + '*' + str(sequence_number)[-4:] + '~' \
                        'IEA*1*' + str(sequence_number) + '~'
        header_string = header_string + footer_string

        # Generating 997
        with open("C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\Out\\997_88_" + str(
                sequence_number) + "_" + datetime.now().strftime(
                "%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(header_string)
        with open("C:\\FTP\\GPAEDIProduction\\WN1-Roxy\\Out\\Archive\\997\\997_88_" + str(
                sequence_number) + "_" + datetime.now().strftime(
                "%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(header_string)