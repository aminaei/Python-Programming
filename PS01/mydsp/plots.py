"""


  Due Date: September 19, 2017

  Code: plots.py
  Created by: Ali Minaei

"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

class plots:
    ###################################################################################
    # fit_norm(data) – Return tuple with estimator of mean and variance: (μ, σ^2 ).
    # The numpy functions numpy.mean and numpy.var will be helpful here.
    ###################################################################################

    def fit_norm(data):
        data_mean = np.mean(data,dtype='int64')
        data_var = np.var(data,dtype='int64')

        # print("mean = ",data_mean)
        # print("var = ", data_var)

        return (data_mean,data_var)


    ###################################################################################
    # plot_data(data, n1, n2)
    # Plot a histogram of specified data. Overlay the plot with two normal distributions.
    # n1 and n2 are tuples describing the normal distributions’ mean and variance (e.g. the
    # output of fit_norm()).
    ###################################################################################
    def plot_data(data, n1, n2):


        # convert RMS to dB is done in the driver.py
        # data_db = 20*np.log10(data)

        #  sigma is varaince but we need std: sqrt(sigma)
        # mu,sigma = plots.fit_norm(data_db)
        mu = n1
        sigma = np.sqrt(n2)
        print("mu = ",mu," sigma = ",sigma)

        fig = plt.figure(2)
        # fig, ax = plt.subplots(1,1)
        ax = fig.add_subplot(111)

        # the histogram of the data
        n, bins, patches = plt.hist(data, 50)


        ax2 = plt.twinx()
        y = mlab.normpdf( bins, mu, sigma)

        ax2.plot(bins,y,linewidth=1)
        ax2.set_ylim(0, 0.14)

        ax.set_title('Pressure distribution with PDFs')
        ax.set_xlabel('Pressure RMS (20log10(RMS)) dB rel.')
        ax.set_ylabel('Counts')
        ax2.set_ylabel('PDF')
        # #ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
        plt.tight_layout()
        # plt.grid(True)
