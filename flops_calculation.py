
input_shape = (3 ,300 ,300) # Format:(channels, rows,cols)
conv_filter = (64 ,3 ,3 ,3)  # Format: (num_filters, channels, rows, cols)
stride = 1
padding = 1
activation = 'relu'

if conv_filter[1] == 0:
    n = conv_filter[2] * conv_filter[3] # vector_length
else:
    n = conv_filter[1] * conv_filter[2] * conv_filter[3]  # vector_length

flops_per_instance = n + ( n -1)    # general defination for number of flops (n: multiplications and n-1: additions)

num_instances_per_filter = (( input_shape[1] - conv_filter[2] + 2 * padding) / stride) + 1  # for rows
num_instances_per_filter *= ((input_shape[1] - conv_filter[2] + 2 * padding) / stride) + 1  # multiplying with cols

flops_per_filter = num_instances_per_filter * flops_per_instance
total_flops_per_layer = flops_per_filter * conv_filter[0]  # multiply with number of filters

if activation == 'relu':
    # Here one can add number of flops required
    # Relu takes 1 comparison and 1 multiplication
    # Assuming for Relu: number of flops equal to length of input vector
    total_flops_per_layer += conv_filter[0] * input_shape[1] * input_shape[2]


if total_flops_per_layer / 1e9 > 1:   # for Giga Flops
    print(total_flops_per_layer/ 1e9 ,'{}'.format('GFlops'))
else:
    print(total_flops_per_layer / 1e6 ,'{}'.format('MFlops'))
