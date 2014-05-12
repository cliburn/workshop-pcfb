"""Intermediate example of data munging using numpy.
Task: Summarize the change in concentration over time for each cytokine.
Input: An Excel worksheet exported as a tab delimited file
Output: Figures summarizing concentrations of individual cytokines over time.
"""

import numpy
import pylab
import os

def parse_cytokine_table(filename):
    # extract data and sample and cytokine mapping dictinaries from table
    table = read_table(filename)

    warning_dict = parse_warnings(table)
    sample_mapper = parse_samples(table)
    cytokine_mapper = parse_headers(table)
    data = parse_data(table, warning_dict)
    return warning_dict, sample_mapper, cytokine_mapper, data

def read_table(filename, delimiter='\t'):
    # read data into an array of strings
    # this can also be done by standard data munging techniques
    # but would be more painful
    return numpy.loadtxt(filename, dtype='string', delimiter=delimiter)

def parse_warnings(table):
    # create a dictionary to convert missing data codes into numeric codes
    data = table[1:, 1:]
    warning_dict = {}
    idx = -1
    for x in data.ravel():
        try:
            float(x)
        except:
            if x not in warning_dict:
                warning_dict[x] = idx
                idx -= 1
    return warning_dict

def parse_samples(table):
    # create a dictionary that returns the rows where each sample has data
    samples = table[1:,0]
    sample_mapper = {}
    for i, sample in enumerate(samples):
       sample_mapper.setdefault(sample, []).append(i)
    return sample_mapper

def parse_headers(table):
    # get header information in first row
    headers = table[0,:]
    # parse header informtion to find columns for each cytokine/day combination
    cytokine_mapper = {}
    for i, label in enumerate(headers[1:]):
        cytokine, day = label.split('day')
        cytokine_mapper.setdefault(cytokine.strip(), {})[int(day)] = i
    return cytokine_mapper

def parse_data(table, warning_dict):
    # convert missing data from strings to code numbers for analysis
    data = table[1:, 1:]
    for warning in warning_dict:
        data[data==warning] = warning_dict[warning]
    data = data.astype('float')
    return data

def plot_cytokine(cytokine, cytokine_mapper, data, save=False, directory='.'):
    # generate box and whiskers plot for distribution of a single cytokine
    idx_dict = cytokine_mapper[cytokine]
    xs = data[:, sorted(idx_dict.values())]

    # collect measured values for each day in a list ignoring missing values
    ys = []
    for i in range(xs.shape[1]):
        col = xs[:,i]
        ys.append(col[col >= 0])

    # if there are any measured values, visualize the data disbution
    if numpy.sum(len(y) for y in ys) > 0:
        pylab.figure()
        pylab.boxplot(ys)
        pylab.xticks(range(1, len(idx_dict.keys())+1), idx_dict.keys())
        pylab.xlabel('Days')
        pylab.title(cytokine)

    if save:
        if not os.path.exists(directory):
            os.makedirs(directory)
        pylab.savefig(os.path.join(directory, cytokine + '.png'))

def sample_qc(warning_dict, sample_mapper, data):
    # generate a dictionary whose keys are warning labels
    # and whose values are lists of (sample, number of warnings) pairs
    qc = {}
    for warning in warning_dict:
        for sample in sample_mapper:
            idx = sample_mapper[sample]
            xs = data[idx, :]
            num_warnings =  numpy.sum(xs==warning_dict[warning])
            qc.setdefault(warning, []).append((sample, num_warnings))
    return qc            

def write_qc(qc, directory='.'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for k in sorted(qc):
        filename = k.replace(' ', '_').replace('/', '-') + '.txt'
        fo = open(os.path.join(directory, filename), 'w')
        sample_list = qc[k]
        for sample in sample_list:
            if sample[1] != 0:
                 fo.write('%s\t%d' % sample + '\n')
        fo.close()

if __name__ == '__main__':
    # parse the file
    warning_dict, sample_mapper, cytokine_mapper, data = parse_cytokine_table(
        'Cytokine_assay_31Dec08PAD.txt')

    # visualize cytokine distributions
    for cytokine in cytokine_mapper:
        plot_cytokine(cytokine, cytokine_mapper, data,
                      save=True, directory='figures')

    # Save errors by sample for QC to output files
    qc = sample_qc(warning_dict, sample_mapper, data)
    write_qc(qc, directory='qc_reports')
