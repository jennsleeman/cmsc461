require 'csv'
require 'erb'

#Example command
# ruby parser.rb file.csv
# Creates text file called a.txt


# erb tutorial: http://www.stuartellis.eu/articles/erb/

# Get csv files
file = ARGV[0]

#row lowerbound, START FROM 1
lb = 1
#sentinel value -1, print all rows
ub = 4

template_file = File.open("template.erb", "rb")
template = template_file.read
renderer = ERB.new(template)

target_file = open('a.txt', 'w')

# Loop through each row
# http://ruby-doc.org/stdlib-1.9.2/libdoc/csv/rdoc/CSV.html
# Be sure to look up header_converters
CSV.foreach(file,
  {:force_quotes=>true, :headers => true, :header_converters =>:symbol}) do |row|
	# $. is row number
	if(ub == -1 || ($. >= lb && $. <= ub))
		target_file.write(renderer.result(binding))
	end
end

template_file.close()
target_file.close()
