import datetime
import time

HOTEL = 0
DATE = 1
CHILDREN = 3
RESERVATION_STATUS = 8


def import_data(filename='booking.txt'):
    """
    Import data from a file to a list. The columns are marked as follows:
    hotel;arrival_date;booked_nights;adults;children;babies;meal;country;reservation_status;reservation_status_date
    Expected returned data format:
        [["Resort Hotel", "01/22/2017", 4, 2, 0, 0, "YES", "PL", "Check-Out", "09/20/2022"],
        ["City Hotel", "01/22/2017", 2, 2, 0, 0,
            "NO", "FR", "Cancelled", "09/20/2022"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing accomodation booking data
    :rtype: list
    """
    with open(filename, "r") as file:
        bookings = []
        for line in file:
            booking = line.strip().split(";")
            bookings.append(booking)
        return bookings


def export_data(bookings, filename='booking.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list booking: booking data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    modes = ["a", "w"]
    if mode in modes:
        text_file = open(filename, mode)
        for line in range(0, len(bookings)):
            row = ";".join(bookings[line])
            if line == len(bookings) - 1:
                text_file.writelines(row)
            else:
                text_file.writelines(row + "\n")
    else:
        raise ValueError('Wrong write mode')


def get_rows_by_booking_status(rows, status):
    """
    Get booking rows by status

    :param list: booking data
    :param str status: status to filter by e.g. Canceled, Checked-out

    :raises ValueError: if given status is not present in the list. Error message: 'Status is not present in list'
    :returns: all rows of given status
    :rtype: list
    """
    status_list = set([])
    for booking in rows:
        if booking[RESERVATION_STATUS] not in status_list:
            status_list.add(booking[RESERVATION_STATUS])
    if status not in status_list:
        raise ValueError('Status is not present in list')
    filtered_status = []
    for booking in rows:
        if booking[RESERVATION_STATUS] == status:
            filtered_status.append(booking)
    return filtered_status


def get_rows_by_date(rows, date_in, date_out):
    """
    Get rows filtred by specific date

    :param list rows: rows data, date in, date out
    :returns: list of booking in date range betwee date_in and date_out
    :rtype: list
    """
    date_in = convert_to_timestamp(date_in)
    date_out = convert_to_timestamp(date_out)
    for booking in rows:
        if date_in > convert_to_timestamp(booking[DATE]):
            pass


def convert_to_timestamp(date_str):
    date_list = date_str.strip().split("/")
    month, day, year = date_list
    date_t = datetime.datetime(int(year), int(month), int(day))
    date = time.mktime(date_t.timetuple())
    # date = datetime.timestamp(date_t)
    return date


def get_date_out():
    pass


def children_number_in_date(rows, date, hotel):
    """
    Thos method should return amount of children in selected date and specific hotel

    :param list rows: booking data, date, hotel name
    :returns: number of chidren
    :rtype: int
    """
    children_amount = 0
    for booking in rows:
        if booking[DATE] == date and booking[HOTEL] == hotel:
            print(int(booking[CHILDREN]))
            children_amount += int(booking[CHILDREN])
    return children_amount


def display_reservation(rows, date):
    """
    Method return table representation of reservation in format:

    hotel | check in   | check out  | adults | children | babies | status
    Ibis  | 20/09/2022 | 25/09/2022 | 2      | 0        | 0      | checked-in


    Please get check out date based on arrival_date and booked nights
    """
    for booking in rows:
        pass


# export_data(import_data(), "new_booking.txt", "q")
# print(get_rows_by_booking_status(import_data(), "CheOut"))
# print(children_number_in_date(import_data(), "09/18/2022", "Resort Hotel"))
# print(convert_to_timestamp("01/22/2017"))
