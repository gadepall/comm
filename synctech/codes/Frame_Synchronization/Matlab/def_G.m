function G=def_G()
G=[kron(ones(1,16),[0 1]);kron(ones(1,8),[0 0 1 1]);kron(ones(1,4),[0 0 0 0 1 1 1 1])];
G=[G;kron([0 1 0 1], ones(1,8));kron([0 1], ones(1,16));ones(1,32)];

