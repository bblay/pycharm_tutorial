from collections import defaultdict


def process_data_file(fpath, max_lines):
    """
    Do a thing.
    
    :param str fpath: 
    :param int | None max_lines: Number of lines to process, or None to process all. 
    """
    result = defaultdict(int)
    for i, line in enumerate(open(fpath, 'rt')):
        if i >= max_lines:
            print 'max lines reached'
            break
        split = line.split(',')
        foo = split[0]
        bar = int(split[1])
        result[foo] += bar
    print i, 'lines read'
    return result
