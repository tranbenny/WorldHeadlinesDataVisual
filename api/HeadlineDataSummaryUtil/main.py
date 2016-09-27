from HeadlineDataSummary.ComputeDataSummary import computeDateSummary
import time

if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d')
    computeDateSummary(date)