# COVID-19-data-plot
Python script which download the official Protezione Civile data (https://github.com/pcm-dpc/COVID-19) and allow you to plot whatever you want.

DISCAIMER:
This is just an amateur python script I wrote in order to plot and analyse by myself the data provided by the official italian Protezione Civile (https://github.com/pcm-dpc/COVID-19) about the Covid spreading. I'm not the owner and I am not associated by any mean to those data.

Of course you are free to modify and share this content as you want. However, I would appreciate if you cite me if you do, thank you.



FUNCTIONS:
The main program is the plot_data.py, in which you can modify whatever you want to make it plot all the data you want, perform some fit and so on.
It does not require anything particular to run, expect the python packages in the header.

The data_download.py script it's just a script that automatically grabs the data file from the official repository. This can also be done manually by downloading the repository and unzip it. Then of course you have to pay attention to where you save them and modify the plot_data.py working directory accordingly.
It's designed to run on Ubuntu (needs the svg package), so you may have trouble with other OS.

I separated the two programs because you just need to update the data (at most) once a day, and there is no need to do this operation everytime you want to change/execute the data analysis. Feel free to merge them togher in you need.




Feel free to contact me to report any needs or bugs.
https://sites.google.com/view/a-moscatello/home

Andrea Moscatello. 
11/04/2020
