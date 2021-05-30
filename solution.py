from seed import res
from datetime import datetime

__dateformat__ = '%Y-%m-%d %H:%M:%S'


def dash_line(val):
    return '-'.join(['' for i in range(val)])

    
def get_ordered_login_length(data_res):
    """get ordered login length function is 
    to get the list of length for each login consequtive

    parameters
    ----------
    data_res :  list of str
                List of date string

    Returns
    -------
    list
        Return list of tuples
                
    """

    # checking if parameter is not a list
    if type(data_res) !=  list:
        raise Exception('Data res type is not list')

    # checking if the list length is 0
    if len(data_res) <= 0:
        return None

    # temporary result variable
    pairs = []

    '''
    sort the data from seed with sorted function.
        sorted function using TimSort Algorithm which have
        O(n log n)
    '''
    sorted_data = sorted(data_res, key = lambda x: datetime.strptime(x, __dateformat__))


    # marker counter
    count_seq = 0
    # start date marker
    start_seq = None

    # loop for each data in data res after sorted 
    # start from 1 to n + 1
    for i in range(1, len(sorted_data) + 1):

        # get the prev date in sorted_data
        prev_item = datetime.strptime(sorted_data[i-1], __dateformat__)
        # delta value before process
        delta = 0

        if i < len(sorted_data):

            # get the current date item
            curr_item = datetime.strptime(sorted_data[i], __dateformat__)

            # get the delta in days
            delta = (curr_item.date() - prev_item.date()).days

            # checking if the delta is less than 2
            # then it mean login in same day or next day
            if delta < 2:
                if count_seq == 0:
                    start_seq = prev_item
                count_seq += 1
          
        # if the sequence is stop or the iterator value
        # is more than len of the sorted_data (res)
        if delta >= 2 or i >= len(sorted_data):

            # checking if this step is a sequence
            if not start_seq:
                start_seq = prev_item


            # get the delta length in day from 
            # start date to prev date that one equence
            # or single item
            length = (prev_item.date() - start_seq.date()).days
            # if it single item then the length will 0
            # mean just 1 day, else the length + 1
            # add the start_seq date as a day
            length = 1 if length == 0 else length + 1


            # append the result to the pairs list
            pairs.append(
                (str(start_seq.date()), str(prev_item.date()), length))
            # reset the counter and start date marker
            start_seq = None
            count_seq = 0

    # return the result in sorted by the length using TimSort
    # the TimSort complexity is O(n log n)
    return sorted(pairs, key = lambda x : x[2], reverse = True)


# main method to print the table
if __name__ == '__main__':
    # call the table length sorter
    # assign the result to result variable
    result = get_ordered_login_length(res)

    # print the header
    print('|{:<20}|{:<20}|{:<6}|'.format('START','END','LENGTH'))
    # print the line
    print('|{:<20}|{:<20}|{:<6}|'.format(dash_line(20),dash_line(20),dash_line(6)))

    # print the data in the result variable
    for v in result:
        print('|{:<20}|{:<20}|{:<6}|'.format(v[0],v[1],v[2]))

