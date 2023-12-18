import sys
from lxml import etree


def modify_parameter(XML_input_filename, XML_output_filename, param, value):
    root = etree.parse(XML_input_filename)
    user_params = root.xpath("//PhysiCell_settings//user_parameters//" + param)
    for user_param in user_params:
        user_param.text = str(value)
    with open(XML_output_filename, 'wb') as fd:
        fd.write(etree.tostring(root, encoding='UTF-8'))
        
    print("Done")

def process_parameters():
    if len(sys.argv) < 2:
        print("Please specify name for the input file")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Please specify name for the output file")
        sys.exit(1)
    
    if len(sys.argv) < 4:
        print("Please specify name for the parameter to modify")
        sys.exit(1)
        
    if len(sys.argv) < 5:
        print("Please specify value for the parameter to modify")
        sys.exit(1)
        
    print("Modifying parameter value in XML : ")
    XML_input_filename = sys.argv[1]
    print("- Input XML file : %s" % XML_input_filename)
    XML_output_filename = sys.argv[2]
    print("- Output XML file : %s" % XML_output_filename)
    parameter_name = sys.argv[3]
    print("- Parameter name : %s" % parameter_name)
    parameter_value = float(sys.argv[4])
    print("- Parameter value : %.5f" % parameter_value)
    
    return XML_input_filename, XML_output_filename, parameter_name, parameter_value


if __name__ == "__main__":
    XML_input, XML_output, parameter, value = process_parameters()
    modify_parameter(XML_input, XML_output, parameter, value)
