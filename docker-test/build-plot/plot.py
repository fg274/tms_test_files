# this script takes a file of dates and builds a plot
import matplotlib.pyplot as plt
import argparse
import numpy as np



def file_extract_year_months(filename, pyear)->dict:
	# takes a file of dates and outputs a dictionary where:
	# month_year -> how many fotos made
	year_month = {}
	with open(filename, 'rt', encoding='utf-8') as stream:
			for date in stream:
				# remove \n character at the end of string
				date = date.strip()
				if date == "":
					continue
				day, month, year = date.split(".")

				if year not in year_month:
					month_sum = {"01":0,"02":0,"03":0,
				  				"04":0, "05":0, "06":0,
								"07":0, "08":0, "09":0,
								"10":0, "11":0, "12":0}
					year_month[year] = month_sum 

				year_month[year][month] += 1
				
	return year_month


def make_plot_for_data(pfile, ppath, pyear, pname):
	year_month = file_extract_year_months(pfile, pyear)

	plt.rcParams.update({
		'text.usetex': True,
		'font.family': 'serif',
		})

	if pyear != "":
		if pyear not in year_month:
			year_month = {pyear:
								{"01":0,"02":0,"03":0,
				  				"04":0, "05":0, "06":0,
								"07":0, "08":0, "09":0,
								"10":0, "11":0, "12":0}}
		else:	
			year_month = {pyear:year_month[pyear]}

	for year in year_month:
		month_sum = year_month[year]	
		fig1_y_pic_p_year = []
		fig1_x_years = []
		plot_data = [(month, month_sum[month]) for month in month_sum]
		plot_data_sorted = sorted(plot_data)
		fig1_x_years = [month[0] for month in plot_data_sorted]
		fig1_y_pic_p_year = [month[1] for month in plot_data_sorted]
		plt.xlabel(f"year {year}")
		plt.ylabel("number of pictures")
		plt.grid()
		plt.ylim(0)
		plt.plot(fig1_x_years, fig1_y_pic_p_year, 'o:')

		path = ppath
		if ppath != "" and ppath[:-1] != "/":
			path += "/"
		name = "plot"
		if pname != "":
			name = pname
		plt.savefig(f"{path}{name}_{year}.svg")
		plt.clf()




if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		prog='plot.py',
		description='takes a file of dates and returns a plot')
	parser.add_argument('-f', '--file', 
					 required=True, 
					 help="PATH to inout file")
	parser.add_argument('-p', '--path', 
					 required=True, 
					 help="the absolut path, where the plot is saved")
	parser.add_argument('-y', '--year', 
					 required=False, 
					 help="plot will only look at data from this year")
	parser.add_argument('-n', '--name', 
					 required=False, 
					 help="if name specified, will safe plot under name_year.svg")
	args = parser.parse_args()

	pfile = str(args.file)
	ppath = str(args.path)
	pyear = str(args.year)
	pname = str(args.name)
	if args.year == None:
		pyear = ""
	if args.name == None:
		pname = ""
	make_plot_for_data(pfile, ppath, pyear, pname)
